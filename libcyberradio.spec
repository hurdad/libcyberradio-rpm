Summary: CyberRadio Solutions Common Library
Name: libcyberradio
Version: %{VERSION}
Release: 1%{?dist}
License: Proprietary
Group: Applications/Programming
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://www.cyberradiosolutions.com
Vendor: CyberRadio Solutions, Inc.
BuildRequires: cmake, libpcap-devel, doxygen

%description
Provides a common set of software components for interacting with 
CyberRadio Solutions radios.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description devel
Development files for %{name}

%package doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description doc
Documentation for %{name}

%package examples
Summary:        Example files for %{name}
Requires:       %{name} = %{version}-%{release}
%description examples
Examples for the %{name}

%prep
%setup -n %{name}-%{version}

%build
%cmake .
%{__make} %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING README
%{_libdir}/%{name}.so

%files doc
%{_docdir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/cmake/%{name}/*.cmake

%files examples
%{_datadir}/%{name}/examples/*


