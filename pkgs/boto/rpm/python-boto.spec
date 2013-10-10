%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname boto

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:			python26-%{pkgname}
%else
Name:			python-%{pkgname}
%endif
Version:		2.13.3
Release:		1%{?dist}
Summary:		A simple lightweight interface to Amazon Web Services
License:		MIT
Group:			Development/Languages
Source:			http://pypi.python.org/packages/source/b/boto/boto-%{version}.tar.gz
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
#BuildRequires: 	python26-devel
Requires:		python26
%else
#BuildRequires: 	python-devel >= 2.5
Requires:		python >= 2.5
%endif
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports S3 (Simple Storage Service), SQS (Simple Queue Service) via
the REST API's provided by those services and EC2 (Elastic Compute Cloud)
via the Query API. The goal of boto is to provide a very simple, easy to
use, lightweight wrapper around the Amazon services.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Remove all test scripts
rm -rf $RPM_BUILD_ROOT{%{_bindir},%{python_sitelib}/tests}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Thu Aug 2 2012 Marat Komarov <marat@scalr.net> 2.5.3-1
- Packaged develop branch. commit: 3386fc67812104409570a1bef647e30d9e286a8c

* Thu Jun 23 2011 Marat Komarov <marat@scalr.net> 2.0b4-1
- Packaging the beta 4 release of boto 2.0

* Tue Jun 1 2010 Marat Komarov <marat@scalr.net> 1.9b-1
- Initial spec file from Fedora. Thanks to Robert Scheck <robert@fedoraproject.org>

