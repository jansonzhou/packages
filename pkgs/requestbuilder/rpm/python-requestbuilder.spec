%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname requestbuilder
%define srcname requestbuilder

Summary:       Command line-driven HTTP request builder
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       0.1.0
Release:       1%{?dist}
License:       ISC 
Group:         Development/Languages
Source0:       https://pypi.python.org/packages/source/r/requestbuilder/requestbuilder-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:      python26, python26-requests, python26-six, python26-argarse
%else
Requires:      python >= 2.5, python-requests, python-six, python-argparse
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Command line-driven HTTP request builder

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
%{python_sitelib}/*
%{python_sitelib}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog

