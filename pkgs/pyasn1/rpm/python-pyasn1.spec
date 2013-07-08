%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname pyasn1

Summary:		ASN.1 tools for Python

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:			python-%{pkgname}
%endif

Version:        0.1.17
Release:        1%{?dist}
Summary:        ASN.1 tools for Python
License:        BSD
Group:          System Environment/Libraries
URL:            http://pyasn1.sourceforge.net/
Source0:        https://pypi.python.org/packages/source/p/pyasn1/pyasn1-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:		python26
%endif
%if 0%{?fedora} >= 8
BuildRequires:  python-setuptools
Requires:		python
%endif

BuildRoot: 		%{_tmppath}/%{name}-buildroot
BuildArch:      noarch


%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.


%prep
%setup -n %{pkgname}-%{version} -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE examples/*
%{python_sitelib}/*


%changelog
* Mon Jun 07 2010 Marat Komarov <marat@scalr.com> - 0.0.11a-1
Initial spec based on Fedora 12 srpm

