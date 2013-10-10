%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname simplejson


%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif
Version:        3.1.1
Release:        1%{?dist}
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

Group:          System Environment/Libraries
License:        MIT
URL:           https://pypi.python.org/pypi/simplejson/
Source0:       https://pypi.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
BuildRequires: 	python-devel >= 2.5
Requires:       python >= 2.5
%endif
BuildArch:      noarch

%description
simplejson is a simple, fast, complete, correct and extensible JSON <http://json.org> 
encoder and decoder for Python 2.5+ and Python 3.3+. It is pure Python code with 
no dependencies, but includes an optional C extension for a serious speed boost.
A comprehensive HTTP client library that supports many features left out of
other HTTP libraries.

%prep
%setup -q -n simplejson-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/%{pkgname}/*
%{python_sitelib}/%{pkgname}-%{version}-py%{pyver}.egg-info

%changelog
