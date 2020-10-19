Name:		dbeaver-ce
Version:	7.2.3
Release:	1%{?dist}
Summary:	Universal Database Manager and SQL Client

License:	ASL 2.0	
URL:		https://dbeaver.io
Source0:        https://github.com/dbeaver/dbeaver/archive/%{version}.tar.gz
Source1:	dbeaver.desktop
Requires:      java >= 1.8
BuildRequires: maven
BuildRequires: dos2unix
BuildRequires: java-devel >= 1.8
ExclusiveArch: x86_64

%description
Universal Database Manager and SQL Client

%global debug_package %{nil} 

%ifarch %ix86
%global sourcedir x86
%else
%global sourcedir x86_64
%endif

%prep
%setup -q -n dbeaver-%{version}
cp %{SOURCE1} %{_builddir}/

%build

mvn package
mkdir -p usr/share
mv product/standalone/target/products/org.jkiss.dbeaver.core.product/linux/gtk/%{sourcedir}/dbeaver usr/share/

%check

%install
mv %{_builddir}/dbeaver-%{version}/usr %{buildroot}/
mkdir -p %{buildroot}%{_datarootdir}/applications
mv %{_builddir}/dbeaver.desktop %{buildroot}%{_datarootdir}/applications/

%files
%dir %{_datarootdir}/dbeaver
%{_datarootdir}/dbeaver/*
%{_datarootdir}/dbeaver/.eclipseproduct
%{_datarootdir}/applications/dbeaver.desktop

%changelog
* Mon Oct 19 2020 Golanv <mullein@adelie.io> 7.2.3-1
- Version bump to 7.2.3
* Sun Oct 4 2020 Golanv <mullein@adelie.io> 7.2.2-1
- Version bump to 7.2.2
* Mon Sep 21 2020 Golanv <mullein@adelie.io> 7.2.1-1
- Version bump to 7.2.1
* Wed Sep 2 2020 Golanv <mullein@adelie.io> 7.2.0-1
- Version bump to 7.2.0
* Tue Aug 18 2020 Golanv <mullein@adelie.io> 7.1.5-1
- Version bump to 7.1.5
* Thu Aug 6 2020 Golanv <mullein@adelie.io> 7.1.4-1
- Version bump 7.1.4
* Tue Jul 21 2020 Golanv <mullein@adelie.io> 7.1.3-1
- Version bump to 7.1.3
* Mon Jul 06 2020 Golanv <mullein@adelie.io> 7.1.2-1
- Version bump to 7.1.2 
* Tue Jun 30 2020 Golanv <mullein@adelie.io> 7.1.1-1
- Version bump to 7.1.1
* Tue Jun 09 2020 Golanv <mullein@adelie.io> 7.1.0-1
- Version bump to 7.1.0
* Mon May 18 2020 Golanv <mullein@adelie.io> 7.0.5-1
- Version bump to 7.0.5
* Mon May 04 2020 Golanv <mullein@adelie.io> 7.0.4-1
- Version bump to 7.0.4
* Sun Apr 19 2020 Golanv <mullein@adelie.io> 7.0.3-1
- Version bump to 7.0.3
* Tue Apr 07 2020 Golanv <mullein@adelie.io> 7.0.2-1
- Version bump to 7.0.2
* Mon Mar 23 2020 Golanv <mullein@adelie.io> 7.0.1-1
- Version bump to 7.0.1
* Mon Mar 02 2020 Golanv <mullein@adelie.io> 7.0.0
- Version bump
* Mon Feb 17 2020 Golanv <mullein@adelie.io> 6.3.5
- Version bump
* Mon Jan 20 2020 Golanv <mullein@adelie.io> 6.3.3
- Version bump
* Wed Jan 8 2020 Golanv <mullein@adelie.io> 6.3.2
- Version bump
* Sun Dec 1 2019 Golanv <mullein@adelie.io> 6.3.0
- Version bump
* Mon Nov 18 2019 Golanv <mullein@adelie.io> 6.2.5
- Version bump
* Mon Nov 04 2019 Golanv <mullein@adelie.io> 6.2.4
- Updates dbeaver.desktop file
- Version bump
* Mon Oct 21 2019 Golanv <mullein@adelie.io> 6.2.3
- Version bump
* Mon Oct 07 2019 Golanv <mullein@adelie.io>
- Bump to upstream
