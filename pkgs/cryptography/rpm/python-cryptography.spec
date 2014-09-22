%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname cryptography
%define srcname cryptography

Summary:       cryptography provides cryptographic recipes and primitive
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       0.5.4
Release:       1%{?dist}
License:       GPL
Group:         Development/Languages
Source0:       https://pypi.python.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26, python26-six, python26-cffi
%else
Requires:       python >= 2.5, python-six, python26-cffi
%endif
#BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
cryptography includes both high level recipes, and low level interfaces to common cryptographic
algorithms such as symmetric ciphers, message digests and key derivation functions

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
%{python_sitearch}/%{srcname}/*
%{python_sitearch}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog

