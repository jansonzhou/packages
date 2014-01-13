%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname docopt
%define srcname docopt

Summary:       Pythonic argument parser, that will make you smile
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       1.6.1
Release:       1%{?dist}
License:       MIT
Group:         Development/Languages
Source0:       https://pypi.python.org/packages/source/d/docopt/docopt-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Docopt helps you create most beautiful command-line interfaces easily

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
%{python_sitelib}/%{srcname}/*
%{python_sitelib}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog

