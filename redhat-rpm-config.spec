Summary: Red Hat specific rpm configuration files.
Name: redhat-rpm-config
Version: 7.3.91
Release: 1
License: GPL
Group: Development/System
Source: redhat-rpm-config-%{version}.tar.gz
BuildArch: noarch
Requires: rpmbuild(VendorConfig) <= 4.1
BuildRoot: %{_tmppath}/%{name}-root

%description
Red Hat specific rpm configuration files.

%prep

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm
( cd ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm; tar xzf %{SOURCE0}; mv %{name}-%{version} redhat; rm -f redhat/*.spec )

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_prefix}/lib/rpm/redhat

%changelog
* Wed Jun 12 2002 Elliot Lee <sopwith@redhat.com> 7.3.91-1
- Update

* Sun Jun  9 2002 Jeff Johnson <jbj@redhat.com>
- create.
