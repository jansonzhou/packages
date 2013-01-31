%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname rackspace-cloudservers
%define srcname cloudfiles

Summary:		Python language bindings for Cloud Files API 

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:			python-%{pkgname}
%endif

Version:		1.7.10
Release:		1%{?dist}
License:		MIT
Group:			Development/Libraries
URL:			https://github.com/rackspace/python-cloudfiles
Source:			python-cloudfiles.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
BuildRequires:	python26-devel
Requires:		python26
%else
BuildRequires:  python-devel >= 2.5
Requires:		python >= 2.5
%endif

BuildArch:		noarch
BuildRoot: 		%{_tmppath}/%{name}-buildroot

%description
Cloud Files™ provides unlimited online storage for files and media. 
And, in an industry first, you can deliver that content to your users 
at blazing speeds over Limelight Network's content delivery network (CDN). 

%prep
%setup -q -n python-%{srcname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING docs
%{python_sitelib}/*

%changelog

