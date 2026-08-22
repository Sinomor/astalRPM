%global dir lib/river
%global commit 0876946fcea17c54626cc0119e9c54e378ea524f
%global date 20260822

Name:           libastal-river
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        Library and cli tool for getting status information of the river wayland compositor.

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/Aylur/astal/archive/%{commit}/astal-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  wl-vapi-gen

BuildRequires:  pkgconfig(astal-wl-0.1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
Library and cli tool for getting status information of the river wayland compositor.

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

%{_libdir}/libastal-river.so.*
%{_libdir}/girepository-1.0/AstalRiver-0.1.typelib

# Devel files
%files devel
%{_libdir}/libastal-river.so
%{_libdir}/pkgconfig/astal-river-0.1.pc
%{_datadir}/vala/vapi/astal-river-0.1.vapi
%{_datadir}/gir-1.0/AstalRiver-0.1.gir
%{_includedir}/astal-river.h
