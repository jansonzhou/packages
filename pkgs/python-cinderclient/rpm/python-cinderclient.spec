%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname  cinderclient

Summary:       This is a client for the OpenStack Volume API. 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       1.0.1
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
URL:           https://github.com/rackspace/python-cinderclient/
Source0:       http://pypi.python.org/packages/source/p/python-cinderclient/python-cinderclient-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 python26-httplib2 python26-argparse python26-prettytable python26-pbr python26-six
#Requires:      python26-requests
%else
Requires:       python >= 2.5 python-httplib2 python-argparse python-prettytable python-pbr python-six
#Requires:      python-requests
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

There's a Python API (the cinderclient module), and a command-line script (cinder). 
Each implements 100% of the OpenStack Volume API.

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
%{python_sitelib}/%{pkgname}/*
%{python_sitelib}/python_%{pkgname}-%{version}-py%{pyver}.egg-info

%changelog
