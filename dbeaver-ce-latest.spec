Name:           dbeaver-ce-latest
Version:        6.0.0
Release:        1%{?dist}
Summary:        Free multi-platform database tool.

License:        ASL 2.0
URL:            https://dbeaver.io
Source0:        https://dbeaver.io/files/dbeaver-ce-latest-linux.gtk.x86_64.tar.gz
BuildArch:      noarch

Requires:       java-1.8.0-openjdk

BuildRequires:  maven-local

%description
Free multi-platform database tool for developers, SQL programmers, database administrators and analysts. Supports all popular databases: MySQL, PostgreSQL, MariaDB, SQLite, Oracle, DB2, SQL Server, Sybase, MS Access, Teradata, Firebird, Derby, etc.

%package        javadoc
Summary:        javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/{name}
%files javadoc -f .mfiles-javadoc

%changelog
* Fri Mar 15 2019 Aaron <mullein@adelie.io> - 6.0.0-1
- Initial packaging
