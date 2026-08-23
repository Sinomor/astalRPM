%global dir lib/quarrel
%global commit bcd02cbd1391e85f52c5ff63e00708b5b62f55ec
%global date 20260823

Name:           quarrel
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        A CLI argument parser with subcommand support.

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/Aylur/astal/archive/%{commit}/astal-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc

BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)


%description
A CLI argument parser with subcommand support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and VAPI files for %{name}.


%prep
%autosetup -n astal-%{commit}


%build
cd %{dir}
%meson
%meson_build

%install
cd %{dir}
%meson_install

# Just files
%files
%license LICENSE

%{_datadir}/gir-1.0/Quarrel-0.1.gir
%{_libdir}/girepository-1.0/Quarrel-0.1.typelib
%{_libdir}/libquarrel.so.0{,.*}

# Devel files
%files devel
%{_includedir}/quarrel.h
%{_libdir}/libquarrel.so
%{_libdir}/pkgconfig/quarrel-0.1.pc
%{_datadir}/vala/vapi/quarrel-0.1.vapi
