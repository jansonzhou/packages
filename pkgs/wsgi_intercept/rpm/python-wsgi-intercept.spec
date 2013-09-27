%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname wsgi-intercept 
%define srcname wsgi_intercept

Summary:       Installs a WSGI application in place of a real URI for testing 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       0.5.1
Release:       1%{?dist}
License:       MIT
Group:         Development/Languages
Source0:       http://pypi.python.org/packages/source/w/wsgi_intercept/wsgi_intercept-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 
%else
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Testing a WSGI application normally involves starting a server at a local host and port, then pointing your test code to that address. Instead, this library lets you intercept calls to any specific host/port combination and redirect them into a WSGI application importable by your test program. Thus, you can avoid spawning multiple processes or threads to test your Web app

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

