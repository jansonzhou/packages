%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname simplejson

Summary:       Python Build Reasonableness 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       3.3.1
Release:       1%{?dist}
License:       MIT
Group:         Development/Languages
URL:           https://pypi.python.org/pypi/simplejson/
Source0:       https://pypi.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26  
%else
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

Simple, fast, extensible JSON encoder/decoder for Python

%prep
%setup -q -n %{pkgname}-%{version}
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
%{python_sitelib}/%{pkgname}/*
%{python_sitelib}/%{pkgname}-%{version}-py%{pyver}.egg-info

%changelog
