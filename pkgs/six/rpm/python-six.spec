%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname  six

Summary:       Python 2 and 3 compatibility utilities 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif

Version:       1.8.0
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
URL:           https://pypi.python.org/pypi/six/
Source0:       https://pypi.python.org/packages/source/p/six/six-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26  
%else
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports every Python version since 2.4.  It is contained in only one Python
file, so it can be easily copied into your project. (The copyright and license
notice must be retained.)

Online documentation is at http://pythonhosted.org/six/.

Bugs can be reported to http://bitbucket.org/gutworth/six.  The code can also be
found there.

For questions about six or porting in general, email the python-porting mailing
list: http://mail.python.org/mailman/listinfo/python-porting

%prep
%setup -q -n %{pkgname}-%{version}
%{__rm} -rf tests

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

#check
#pushd test
#PYTHONPATH=../ %{__python} test_%{pkgname}.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{python_sitelib}/%{pkgname}.*
%{python_sitelib}/%{pkgname}-%{version}-py%{pyver}.egg-info

%changelog
