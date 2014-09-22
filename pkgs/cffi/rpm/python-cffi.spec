%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname cffi
%define srcname cffi

Summary:       C Foreign Function Interface for Python 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       0.8.6
Release:       1%{?dist}
License:       MIT
Group:         Development/Languages
Source0:       https://pypi.python.org/packages/source/c/cffi/cffi-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 
%else
Requires:       python >= 2.5
%endif
#BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
C Foreign Function Interface for Python. The goal is to provide a convenient and reliable way
to call compiled C code from Python using interface declarations written in C.

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
%{python_sitearch}/_cffi_backend.so
%{python_sitearch}/%{srcname}/*
%{python_sitearch}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog

