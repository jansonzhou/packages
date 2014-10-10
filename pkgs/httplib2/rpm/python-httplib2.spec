%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname httplib2


%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif
Version:        0.9
Release:        1%{?dist}
Summary:        A comprehensive HTTP client library

Group:          System Environment/Libraries
License:        MIT
URL:            http://code.google.com/p/httplib2/
Source0:        http://httplib2.googlecode.com/files/httplib2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
BuildRequires: 	python-devel >= 2.5
Requires:       python >= 2.5
%endif
BuildArch:      noarch

%description
A comprehensive HTTP client library that supports many features left out of
other HTTP libraries.

%prep
%setup -q -n httplib2-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/*

%changelog
