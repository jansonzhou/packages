%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname python-novaclient-rax-backup-shedule-ext 

Summary:       Adds backup-schedule extension support to python-novaclient.
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       1.2.0
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
URL:           https://github.com/rackspace/rax_backup_schedule_python_novaclient_ext
Source0:       http://pypi.python.org/packages/source/r/rax_backup_schedule_python_novaclient_ext/rax_backup_schedule_python_novaclient_ext-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 
%else
BuildRequires: 	python-setuptools
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

Adds backup-schedule extension support to python-novaclient.

%prep
%setup -q -n python-%{pkgname}-%{version}
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
/usr/bin/*
%{python_sitelib}/*

%changelog


