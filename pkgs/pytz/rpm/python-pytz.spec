%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname pytz
%define srcname pytz


%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif
Version:        2013.7
Release:        1%{?dist}
Summary:        World timezone definitions, modern and historical

Group:          Development/Languages
License:        MIT
Source0:        http://pypi.python.org/packages/source/p/pytz/pytz-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
Requires:       python >= 2.5
%endif
BuildArch:      noarch

%description
Description: World timezone definitions, modern and historical
pytz brings the Olson tz database into Python. This library allows accurate and cross
platform timezone calculations using Python 2.4 or higher. It also solves the issue of 
ambiguous times at the end of daylight savings, which you can read more about in
the Python Library Reference (datetime.tzinfo)

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
%{python_sitelib}/%{srcname}/*
%{python_sitelib}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog
