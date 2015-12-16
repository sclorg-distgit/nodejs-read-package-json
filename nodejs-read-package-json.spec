%{?scl:%scl_package nodejs-read-package-json}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-read-package-json
Version:        1.2.7
Release:        1%{?dist}
Summary:        npm's package.json parser

Group:          System Environment/Libraries
License:        ISC
URL:            https://github.com/isaacs/read-package-json
Source0:        http://registry.npmjs.org/read-package-json/-/read-package-json-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{?scl_prefix}nodejs-devel
BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif


%description
The thing npm uses to read package.json files, with semantics, defaults and
validation.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/read-package-json
cp -pr package.json read-json.js %{buildroot}%{nodejs_sitelib}/read-package-json

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/read-package-json
%doc LICENSE README.md

%changelog
* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.2.7-2
- New upstream release 1.2.7

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 1.1.6-1
- New upstream release 1.1.6

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 1.1.3-2
- replace provides and requires with macro

* Sat Sep 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.3-1
- update to upstream release 1.1.3
- change License from BSD to ISC
- add ExclusiveArch logic

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- new upstream release 1.1.1

* Mon Jun 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2
- remove unneeded dependency fix on lru-cache

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1
- new upstream release 1.1.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-5
- restrict to compatible arches

* Thu Jun 20 2013 Tomas Hrcka <thrcka@redhat.com> - 0.3.0-4
- added patch to fix RHBZ#965469

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-4
- add macro for EPEL6 dependency generation

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-3
- fix lru-cache dep

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.0-3
- Add support for software collections

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-2
- drop outdated dependency fix

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-1
- new upstream release 0.3.0

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.2-1
- new upstream release 0.2.2

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- new upstream release 0.2.0

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- initial package generated by npm2rpm
