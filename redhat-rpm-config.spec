Summary: Red Hat specific rpm configuration files.
Name: redhat-rpm-config
Version: 8.0.16
Release: 1
License: GPL
Group: Development/System
Source: redhat-rpm-config-%{version}.tar.gz
BuildArch: noarch
#Requires: rpmbuild(VendorConfig) <= 4.1
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
* Tue Dec 17 2002 Bill Nottingham <notting@redhat.com> 8.0.16-1
- make -g in rpmrc conditional on debug_package

* Mon Dec 16 2002 Elliot Lee <sopwith@redhat.com> 8.0.15-1
- Rename -debug subpackages to -debuginfo

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 8.0.14-1
- tweak debug package stuff so that we are overloading %%install
  instead of %%post

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 8.0.13-1
- turn on internal rpm dep generation by default

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 8.0.12-1
- New release with debug packages on

* Tue Dec  3 2002 Bill Nottingham <notting@redhat.com> 8.0.8-1
- turn debug packages off
- override optflags with no -g

* Fri Nov 22 2002 Elliot Lee <sopwith@redhat.com> 8.0.7-1
- turn on debug packages

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 8.0.6-1
- Pass __strip and __objdump macros

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 8.0.5-1
- Update macros to specify find-provides/find-requires

* Thu Oct 31 2002 Elliot Lee <sopwith@redhat.com> 8.0.4-1
- Remove tracking dependency

* Wed Oct 16 2002 Phil Knirsch <pknirsch@redhat.com> 8.0.3-2
- Added fix for outdated config.[sub|guess] files in %configure section

* Wed Oct 16 2002 Elliot Lee <sopwith@redhat.com> 8.0.3-1
- New release that blows up on unpackaged files and missing doc files.

* Thu Oct  3 2002 Jeremy Katz <katzj@redhat.com> 8.0.2
- don't redefine everything in macros, just what we need to

* Mon Sep 16 2002 Alexander Larsson <alexl@redhat.com> 8.0.1
- Add debug package support to %__spec_install_post

* Tue Sep  3 2002 Bill Nottingham <notting@redhat.com> 8.0-1
- bump version

* Wed Aug 28 2002 Elliot Lee <sopwith@redhat.com> 7.3.94-1
- Update macrofiles

* Wed Jul 31 2002 Elliot Lee <sopwith@redhat.com> 7.3.93-1
- Add _unpackaged_files_terminate_build and 
_missing_doc_files_terminate_build to macros

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-6
- find-lang.sh fix from 67368
- find-requires fix from 67325

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-5
- Add /etc/rpm/macros back to make #67951 go away

* Wed Jun 26 2002 Jens Petersen <petersen@redhat.com> 7.3.92-4
- fix %%configure targeting for autoconf-2.5x (#58468)
- include ~/.rpmmacros in macrofiles file path again

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 7.3.92-3
- automated rebuild

* Fri Jun 21 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-2
- Don't define _arch

* Thu Jun 20 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-1
- find-lang error detection from Havoc

* Wed Jun 12 2002 Elliot Lee <sopwith@redhat.com> 7.3.91-1
- Update

* Sun Jun  9 2002 Jeff Johnson <jbj@redhat.com>
- create.
