%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global pkgname gflags

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:			python-%{pkgname}
%endif
Version:        2.0
Release:        1%{?dist}
Summary:        Commandline flags module for Python

Group:          Development/Languages
License:        BSD
URL:            http://code.google.com/p/python-gflags/
Source0:        http://python-gflags.googlecode.com/files/python-gflags-%{version}.tar.gz
BuildRoot:      %{_tmppath}/python-%{pkgname}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
#BuildRequires:	python26-setuptools
Requires:		python26
%endif
%if 0%{?fedora} || 0%{?rhel} >= 6
#BuildRequires:  python-setuptools to avoid errors when building on CentOS 5
Requires:		python >= 2.5
%endif

%description
This project is the python equivalent of google-gflags, a Google commandline
flag implementation for C++. It is intended to be used in situations where a
project wants to mimic the command-line flag handling of a C++ app that uses
google-gflags, or for a Python app that, via swig or some other means, is
linked with a C++ app that uses google-gflags.

The gflags package contains a library that implements commandline flags
processing. As such it's a replacement for getopt(). It has increased
flexibility, including built-in support for Python types, and the ability to
define flags in the source file in which they're used. (This last is its major
difference from OptParse.)

%prep
%setup -q -n python-%{pkgname}-%{version}
# Fix non-executable-script error
sed -i '/^#!\/usr\/bin\/env python$/,+1 d' %{pkgname}.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Remove ext from name
mv %{buildroot}%{_bindir}/gflags2man.py  %{buildroot}%{_bindir}/gflags2man

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{python_sitelib}/*
%{_bindir}/gflags2man

%changelog
* Thu Jul 05 2012 Marat Komarov <marat@scalr.com> - 2.0-1
- New upstream release

* Thu Nov 04 2010 Silas Sewell <silas@sewell.ch> - 1.4-3
- Switch from distribute to setuptools

* Tue Oct 26 2010 Silas Sewell <silas@sewell.ch> - 1.4-2
- Fix non-executable-script error

* Wed Oct 13 2010 Silas Sewell <silas@sewell.ch> - 1.4-1
- Initial package
