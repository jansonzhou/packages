%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname  rackspace-novaclient

Summary:       Metapackage to install python-novaclient and Rackspace extensions
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       1.0
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages


%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
Requires:       python26-setuptools 
Requires:       python26-cinderclient 
Requires:       python26-novaclient
Requires:       python26-rackspace-auth-openstack
Requires:       python26-novaclient-os-diskconfig-ext
Requires:       python26-novaclient-rax-backup-schedule-ext
Requires:       python26-novaclient-os-networksv2-ext
Requires:       python26-novaclient-rax-default-network-flags-ext
%else
BuildRequires: 	python-setuptools
Requires:       python-setuptools 
Requires:       python-cinderclient 
Requires:       python-novaclient
Requires:       python-rackspace-auth-openstack
Requires:       python-novaclient-os-diskconfig-ext
Requires:       python-novaclient-rax-backup-schedule-ext
Requires:       python-novaclient-os-networksv2-ext
Requires:       python-novaclient-rax-default-network-flags-ext
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

This metapackage will ensure that python-novaclient and these extensions 
are installed that are compatible with the Rackspace cloud:

* rackspace-auth-openstack
* os_diskconfig_python_novaclient_ext
* rax_backup_schedule_python_novaclient_ext
* os_networksv2_python_novaclient_ext
* rax_default_network_flags_python_novaclient_ext

%prep

%install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)

%changelog


