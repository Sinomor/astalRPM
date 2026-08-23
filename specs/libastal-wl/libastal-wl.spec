%global dir lib/wl
%global commit bcd02cbd1391e85f52c5ff63e00708b5b62f55ec
%global date 20260823

Name:           libastal-wl
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        Provides a central library to manage wayland objects for other astal libraries.


License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/Aylur/astal/archive/%{commit}/astal-%{commit}.tar.gz

# Things for build
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  wl-vapi-gen

# Devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)


%description
Provides a central library to manage wayland objects for other astal libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and VAPI files for %{name}.

# Building
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
%{_libdir}/libastal-wl.so.*
%{_libdir}/girepository-1.0/AstalWl-0.1.typelib

# Devel files
%files devel
%{_libdir}/libastal-wl.so
%{_libdir}/pkgconfig/astal-wl-0.1.pc
%{_datadir}/vala/vapi/astal-wl-0.1.vapi
%{_datadir}/gir-1.0/AstalWl-0.1.gir
%{_includedir}/astal-wl.h
