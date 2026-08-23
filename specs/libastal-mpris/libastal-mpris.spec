%global dir lib/mpris
%global commit bcd02cbd1391e85f52c5ff63e00708b5b62f55ec
%global date 20260823

Name:           libastal-mpris
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        Library and cli tool for controlling media players.

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/Aylur/astal/archive/%{commit}/astal-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc

BuildRequires:  pkgconfig(quarrel-0.1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)


%description
Library and cli tool for controlling media players.

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

%{_bindir}/astal-mpris
%{_libdir}/libastal-mpris.so.*
%{_libdir}/girepository-1.0/AstalMpris-0.1.typelib

# Devel files
%files devel
%{_libdir}/libastal-mpris.so
%{_libdir}/pkgconfig/astal-mpris-0.1.pc
%{_datadir}/vala/vapi/astal-mpris-0.1.vapi
%{_datadir}/gir-1.0/AstalMpris-0.1.gir
%{_includedir}/astal-mpris.h
