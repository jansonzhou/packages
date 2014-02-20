%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname euca2ools
%define srcname euca2ools

Summary:       Euca2ools provide the functionality of AWS's REST-based and Query-based APIs
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       3.0.2
Release:       1%{?dist}
License:       BSD
Group:         Development/Languages
#Source0:       https://github.com/eucalyptus/euca2ools/archive/%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:      python26, python26-lxml, python26-requestbuilder, python26-requests, python26-six
%else
Requires:      python >= 2.5, python-lxml, python-requestbuilder, python-requests, python-six
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Euca2ools are command line tools used to interact with Amazon Web
Services (AWS) as well as other services that are compatible with AWS,
such as Eucalyptus.  They aim to use the same input as similar tools
provided by AWS for each service individually along with several
enhancements that make them easier to use against both AWS and
Eucalyptus

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

