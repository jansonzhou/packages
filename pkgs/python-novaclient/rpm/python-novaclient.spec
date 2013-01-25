%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname  novaclient

Summary:       Client library for OpenStack Nova API
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       2.10.0
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
URL:           https://github.com/rackspace/python-novaclient/
Source0:       http://pypi.python.org/packages/source/p/python-novaclient/python-novaclient-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 python26-httplib2 python26-argparse python26-prettytable python26-iso8601
%else
BuildRequires: 	python-setuptools
Requires:       python >= 2.5 python-httplib2 python-argparse python-prettytable python-iso8601
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

This is a client for the OpenStack Nova API. 
There's a Python API (the novaclient module), and a command-line script (nova). 
Each implements 100% of the OpenStack Nova API.

%prep
%setup -q -n python-%{pkgname}-%{version}
%{__rm} -rf tests

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

#check
#pushd test
#PYTHONPATH=../ %{__python} test_%{pkgname}.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
/usr/bin/*
/usr/novaclient/*
%{python_sitelib}/%{pkgname}/*
%{python_sitelib}/python_%{pkgname}-%{version}-py%{pyver}.egg-info

%changelog
