%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname rackspace-cloudservers
%define srcname cloudservers

Summary:		Python language bindings for Cloud Servers API 

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:			python-%{pkgname}
%endif

Version:		1.0
Release:		1%{?dist}
License:		MIT
Group:			Development/Libraries
URL:			http://pypi.python.org/pypi/python-cloudservers
Source:			http://pypi.python.org/packages/source/p/python-cloudservers/python-cloudservers-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
#BuildRequires:	python26-devel
Requires:		python26 python26-httplib2 python26-argparse python26-prettytable
%endif
%if 0%{?fedora} >= 8
#BuildRequires:  python-devel >= 2.5
Requires:		python >= 2.5 python-httplib2 python-argparse python-prettytable
%endif

BuildArch:		noarch
BuildRoot: 		%{_tmppath}/%{name}-buildroot

%description
Linux or Windows Servers in minutes
With Cloud Servers™ you get what you want when you need it. 
Make a new server for staging and four new servers for production. 
Delete one, create three more. You only pay for what you use! 

%prep
%setup -q -n python-%{srcname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.rst docs
%{python_sitelib}/*
/usr/bin/*

%changelog
* Thu Dec 17 2010 Marat Komarov <marat@scalr.net> 1.0-1
- Initial package build
