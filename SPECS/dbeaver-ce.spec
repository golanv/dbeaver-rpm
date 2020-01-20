Name:		dbeaver-ce
Version:	6.3.3
Release:	1%{?dist}
Summary:	Universal Database Manager and SQL Client

License:	ASL 2.0	
URL:		https://dbeaver.io
Source0:	https://github.com/dbeaver/dbeaver/archive/%{version}.tar.gz#/dbeaver-%{version}.tar.gz
Source1:	dbeaver.desktop
#Patch0:		dbeaver-workspacepath.patch
#Patch1:		dbeaver-driverspath.patch
Requires:      java >= 1.8
BuildRequires: maven
BuildRequires: dos2unix
BuildRequires: java-devel >= 1.8
#ExcludeArch: ppc64le
#ExcludeArch: s390x
#%%{ix86} 
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
/usr/bin/dos2unix plugins/org.jkiss.dbeaver.model/src/org/jkiss/dbeaver/model/DBConstants.java
/usr/bin/dos2unix plugins/org.jkiss.dbeaver.core.application/src/org/jkiss/dbeaver/core/application/DBeaverApplication.java
#%%patch0 -p0
#%%patch1 -p0
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
* Mon Jan 20 2020 Golanv <mullein@adelie.io 6.3.3
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
