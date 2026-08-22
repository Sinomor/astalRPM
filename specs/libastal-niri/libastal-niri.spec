%global dir src/
%global commit 249eb454468bab9720a11208ac2caac4c4a0f6a1
%global date 20260822

Name:           libastal-niri
Version:        0.2.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        Library and cli tool for Niri IPC sockets.

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/sameoldlab/niri-gtk/archive/%{commit}/niri-gtk-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc

BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)


%description
Library and cli tool for Niri IPC sockets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and VAPI files for %{name}.


%prep
%autosetup -n niri-gtk-%{commit}


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

%{_bindir}/astal-niri
%{_libdir}/libastal-niri.so.*
%{_libdir}/girepository-1.0/AstalNiri-0.2.typelib

# Devel files
%files devel
%{_libdir}/libastal-niri.so
%{_libdir}/pkgconfig/astal-niri-0.2.pc
%{_datadir}/vala/vapi/astal-niri-0.2.vapi
%{_datadir}/gir-1.0/AstalNiri-0.2.gir
%{_includedir}/astal-niri.h
