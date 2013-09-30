%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname  pbr

Summary:       Python Build Reasonableness 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       1.0.1
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
URL:           https://pypi.python.org/pypi/pbr/
Source0:       https://pypi.python.org/packages/source/p/pbr/pbr-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26  
%else
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

PBR is a library that injects some useful and sensible default behaviors into your setuptools run

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
