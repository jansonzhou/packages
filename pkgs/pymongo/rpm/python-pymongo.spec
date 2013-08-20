%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname pymongo

Summary:       Python interface to the MongoDB document-oriented database
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       2.6
Release:       1%{?dist}
License:       Apache License, Version 2.0
Group:         Development/Languages
URL:           https://github.com/mongodb/mongo-python-driver
Source0:       https://pypi.python.org/packages/source/p/pymongo/pymongo-2.6.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
BuildRequires: 	python-devel >= 2.5
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

Python interface to the MongoDB document-oriented database
MongoDB is a high-performance, open source, schema-free
document-oriented data store. Pymongo provides an interface
to easily access it from Python.

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

