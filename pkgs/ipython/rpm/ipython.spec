%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname ipython
%define srcname ipython

Summary:       IPython: Productive Interactive Computing
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       0.13.1
Release:       1%{?dist}
License:       BSD
Group:         Development/Languages
Source0:       https://pypi.python.org/packages/source/i/ipython/ipython-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 
%else
BuildRequires: 	python-setuptools
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
IPython provides a rich toolkit to help you make the most out of using Python interactively. Its main components are:

Powerful interactive Python shells (terminal- and Qt-based).
A web-based interactive notebook environment with all shell features plus support for embedded figures, animations and rich media.
Support for interactive data visualization and use of GUI toolkits.
Flexible, embeddable interpreters to load into your own projects.
A high-performance library for high level and interactive parallel computing that works in multicore systems, clusters, supercomputing and cloud scenarios.

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
/usr/bin
%{python_sitelib}/%{srcname}/*
%{python_sitelib}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog

