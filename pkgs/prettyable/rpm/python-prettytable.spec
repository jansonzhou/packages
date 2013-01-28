%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname prettytable


%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif
Version:        0.5
Release:        1%{?dist}
Summary:        Tabular data in a visually appealing ASCII tables

Group:          System Environment/Libraries
License:        MIT
Source0:        http://pypi.python.org/packages/source/P/PrettyTable/prettytable-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
BuildRequires: 	python26-devel
Requires:       python26
%else
BuildRequires: 	python-devel >= 2.5
Requires:       python >= 2.5
%endif
BuildArch:      noarch

%description
Library to represent tabular data in visually appealing ASCII tables
PrettyTable is a simple Python library designed to make it quick and
easy to represent tabular data in visually appealing ASCII tables. It
was inspired by the ASCII tables used in the PostgreSQL shell
psql. PrettyTable allows for selection of which columns are to be
printed, independent alignment of columns (left or right justified or
centred) and printing of "sub-tables" by specifying a row range.

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
* Thu Dec 23 2010 Marat Komarov <marat@scalr.net> - 0.5-1
- Initial build

