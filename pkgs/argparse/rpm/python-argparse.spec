%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname  argparse

Summary:       Python command-line parsing library
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       1.0.1
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
URL:           http://code.google.com/p/argparse/
Source0:       http://argparse.googlecode.com/files/argparse-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
BuildRequires: 	python-devel >= 2.5
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

The argparse module makes it easy to write user friendly command line interfaces.

The program defines what arguments it requires, and argparse will figure 
out how to parse those out of sys.argv. The argparse module also automatically 
generates help and usage messages and issues errors when users give the program 
invalid arguments.

%prep
%setup -q -n %{pkgname}-%{version}
%{__rm} -rf doc/source

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
%doc README.txt doc/*
%{python_sitelib}/%{pkgname}.py*
%{python_sitelib}/%{pkgname}-%{version}-py%{pyver}.egg-info/

%changelog

