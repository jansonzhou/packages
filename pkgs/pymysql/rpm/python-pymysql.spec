%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global _use_internal_dependency_generator 0

%global upstream_name PyMySQL

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-pymysql
%else
Name:		    python-pymysql
%endif

Version:        0.5
Release:        1%{?dist}
Summary:        A pure python MySQL client

Group:          Development/Languages
License:        MIT
URL:            https://github.com/petehunt/PyMySQL/
Source0:        http://pypi.python.org/packages/source/P/PyMySQL/PyMySQL-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A pure python MySQL client

%prep
%setup -q -n %{upstream_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/pymysql
%{python_sitearch}/%{upstream_name}/*
%{python_sitearch}/%{upstream_name}-%{version}-*.egg-info

%changelog
* Thu May 17 2012 Oleg Suharev <oleg@scalr.com> - 0.5-1
- Initial build
