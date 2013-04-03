%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname google-api-client

Summary:		Google API Client Library for Python

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:			python-%{pkgname}
%endif

Version:		1.0c2
Release:		1%{?dist}
License:        ASL 2.0
Group:			Development/Libraries
URL:			http://code.google.com/p/google-api-python-client
Source:			http://google-api-python-client.googlecode.com/files/google-api-python-client-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
#BuildRequires:	python26-devel
Requires:		python26 python26-httplib2 python26-gflags
%else
#BuildRequires:  python-devel >= 2.5 to avoid errors when building on CentOS 5
Requires:		python >= 2.5 python-httplib2 python-gflags
%endif

BuildArch:		noarch
BuildRoot: 		%{_tmppath}/%{name}-buildroot

%description
The Google API Client for Python is a client library for
accessing the Plus, Moderator, and many other Google APIs.

%prep
%setup -q -n google-api-python-client-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/*
/usr/bin/*

%changelog
* Wed Jul 4 2012 Marat Komarov <marat@scalr.net> 1.0c2-1
- Initial package build

