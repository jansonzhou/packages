%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define pkgname gevent
%define srcname gevent

Summary:        Coroutine-based network library 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:        1.0rc2
Release:        1%{?dist}
License:        MIT
Group:          Development/Languages
Source0:        https://github.com/downloads/SiteSupport/gevent/gevent-%{version}.tar.gz

BuildArch:      noarch
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
#BuildRequires:	python26-setuptools
Requires:		python26
%endif
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires:  python-setuptools, python-devel >= 2.5
Requires:		python >= 2.5
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
gevent is a coroutine-based Python networking library that uses greenlet to
provide a high-level synchronous API on top of libevent event loop.

Features include:

  * convenient API around greenlets
  * familiar synchronization primitives (gevent.event, gevent.queue)
  * socket module that cooperates
  * WSGI server on top of libevent-http
  * DNS requests done through libevent-dns
  * monkey patching utility to get pure Python modules to cooperate

%prep
%setup -q -n %{srcname}-%{version}
%{__rm} -rf tests

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{python_sitelib}/%{srcname}/*
%{python_sitelib}/%{srcname}-%{version}-py%{pyver}.egg-info

%changelog

