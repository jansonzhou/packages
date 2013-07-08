%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define module pysnmp

Summary:        SNMP engine written in Python

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{module}
%else
Name:			%{module}
%endif
Version:        4.2.4
Release:        1%{?dist}

Group:          Development/Libraries
License:        BSD
URL:            http://pysnmp.sourceforge.net/
Source0:        https://pypi.python.org/packages/source/p/pysnmp/pysnmp-%{version}.tar.gz
BuildRoot: 		%{_tmppath}/%{name}-buildroot
BuildArch:      noarch
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
BuildRequires:	python26-setuptools
Requires:		python26 python26-pyasn1 >= 0.0.8
%endif
%if 0%{?fedora} >= 8
BuildRequires:  python-setuptools
Requires:		python >= 2.6 python-pyasn1 >= 0.1.17
%endif


%description
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.


%prep
%setup -q -n %{module}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README THANKS TODO examples/ docs/
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Fri Jun 25 2010 Marat Komarov <marat@scalr.com> - 4.1.12a-1
Initial spec based on Fedora 12 srpm

