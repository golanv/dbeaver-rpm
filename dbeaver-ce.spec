Name:		dbeaver-ce
Version:	6.2.2
Release:	1%{?dist}
Summary:	Free multi-platform database tool.

License:	ASL 2.0	
URL:		https://dbeaver.io
Source0:	https://github.com/dbeaver/dbeaver/archive/%{version}.tar.gz#/dbeaver-%{version}.tar.gz
Source1:	dbeaver.desktop
#Patch0:		dbeaver-workspacepath.patch
#Patch1:		dbeaver-driverspath.patch
Requires:	java-1.8.0-openjdk
BuildRequires: maven
BuildRequires: dos2unix
BuildRequires: java-1.8.0-openjdk-devel
#ExcludeArch: ppc64le
#ExcludeArch: s390x
#%%{ix86} 
ExclusiveArch: x86_64

%description
Free multi-platform database tool

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
* Mon Oct 07 2019 Golanv mullein@adelie.io
- Bump to upstream
