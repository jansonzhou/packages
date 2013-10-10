%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname keystoneclient
%define srcname python-keystoneclient

Summary:       Client library for OpenStack identity API(Keystone)
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       0.2.2
Release:       1%{?dist}
License:       ASL
Group:         Development/Languages
Source0:       https://pypi.python.org/packages/source/p/python-keystoneclient/python-keystoneclient-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
Requires:       python26-requests
Requires:       python26-argparse
Requires:       python26-iso8601
Requires:       python26-pbr
Requires:       python26-six
Requires:       python26-babel
Requires:       python26-netaddr
%else
Requires:       python >= 2.5
Requires:       python-setuptools
Requires:       python-argparse
Requires:       python-requests
Requires:       python-iso8601
Requires:       python-pbr
Requires:       python-six
Requires:       python-babel
Requires:       python-netaddr
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Python bindings to the OpenStack Identity API (Keystone)

%prep
%setup -q -n %{srcname}-%{version}
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
%{python_sitelib}/%{pkgname}/*
%{python_sitelib}/python_%{pkgname}-%{version}-py%{pyver}.egg-info
/usr/bin/*

%changelog
