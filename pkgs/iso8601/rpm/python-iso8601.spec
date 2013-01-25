%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname iso8601


%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif
Version:        0.1.4
Release:        1%{?dist}
Summary:        Simple module to parse ISO 8601 dates.

Group:          System Environment/Libraries
License:        MIT
URL:            http://pypi.python.org/packages/source/i/iso8601/iso8601-${version}.tar.gz
Source0:        iso8601-0.1.4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
Requires:       python >= 2.5
%endif
BuildArch:      noarch

%description
This module parses the most common forms of ISO 8601 
date strings (e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO
%{python_sitelib}/*

%changelog
