%global dir lib/astal/gtk3
%global commit 6e9ed352252f663b0be9dcbc8c60c4ea4a0dcc47
%global date 20260430

Name:           libastal-3
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        Building blocks for building desktop shells using gtk3. 

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/Aylur/astal/archive/%{commit}/astal-%{commit}.tar.gz

# Things for build
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc

# Devel
BuildRequires:  pkgconfig(astal-io-0.1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)


%description
Building blocks for building desktop shells using gtk3.

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
%{_libdir}/libastal.so.3*
%{_libdir}/girepository-1.0/Astal-3.0.typelib

# Devel files
%files devel
%{_libdir}/libastal.so
%{_libdir}/pkgconfig/astal-3.0.pc
%{_datadir}/vala/vapi/astal-3.0.vapi
%{_datadir}/gir-1.0/Astal-3.0.gir
%{_includedir}/astal.h
