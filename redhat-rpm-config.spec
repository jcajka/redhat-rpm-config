Summary: Red Hat specific rpm configuration files.
Name: redhat-rpm-config
Version: 8.0
Release: 0.1
License: GPL
Group: Development/System
Source: redhat-rpm-config-%{version}.tar.gz
BuildArch: noarch
Requires: rpmbuild(VendorConfig) <= 4.1
BuildRoot: %{_tmppath}/%{name}-root

%description
Red Hat specific rpm configuration files.

%prep

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm
( cd ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm; tar xzf %{SOURCE0} )

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_prefix}/lib/rpm/redhat

%changelog
* Sun Jun  9 2002 Jeff Johnson <jbj@redhat.com>
- create.
