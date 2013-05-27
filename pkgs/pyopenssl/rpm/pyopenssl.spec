%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define pkgname pyOpenSSL
%define srcname pyOpenSSL

Summary:       Python wrapper module around the OpenSSL library
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          %{pkgname}
%else
Name:          %{pkgname}
%endif

Version:       0.13
Release:       1%{?dist}
License:       APL2
Group:         Development/Languages
Source0:       https://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
BuildRequires:  python-setuptools
Requires:       python >= 2.5
%endif
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
High-level wrapper around a subset of the OpenSSL library, includes
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes
...  and much more ;)

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
%{python_sitearch}/OpenSSL/*
%{python_sitearch}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog

