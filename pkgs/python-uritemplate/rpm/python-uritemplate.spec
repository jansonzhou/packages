%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global pkgname uritemplate

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:			python-%{pkgname}
%endif
Version:        0.6
Release:        1%{?dist}
Summary:        implementation of RFC6570

Group:          Development/Languages
License:        Apache License (2.0)
URL:            https://github.com/uri-templates/uritemplate-py
Source0:        https://pypi.python.org/packages/source/u/uritemplate/uritemplate-%s.tar.gz
BuildRoot:      %{_tmppath}/python-%{pkgname}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:		python26
%else
Requires:		python >= 2.5
%endif

%description
This is a Python implementation of RFC6570, URI Template, and can expand templates up to and including Level 4 in that specification.

%prep
%setup -q -n python-%{pkgname}-%{version}
# Fix non-executable-script error
sed -i '/^#!\/usr\/bin\/env python$/,+1 d' %{pkgname}.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{python_sitelib}/*

%changelog
* Fri Oct 10 2014 Nick Demyanchuk <spike@scalr.com> - 0.6-1
- New upstream release

