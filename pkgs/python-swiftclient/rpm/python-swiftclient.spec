%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname  swiftclient

Summary:       Python bindings to the OpenStack Object Storage API.
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       1.2.0
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
URL:           https://github.com/openstack/python-swiftclient/
Source0:       http://pypi.python.org/packages/source/p/python-swiftclient/python-swiftclient-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 
%else
BuildRequires: 	python-setuptools
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

This is a python client for the Swift API. 
There's a Python API (the swiftclient module), and a command-line script (swift).

%prep
%setup -q -n python-%{pkgname}-%{version}
%{__rm} -rf tests

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
/usr/bin/*
%{python_sitelib}/*

%changelog


