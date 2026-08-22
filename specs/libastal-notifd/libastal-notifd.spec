%global dir lib/notifd
%global commit 0876946fcea17c54626cc0119e9c54e378ea524f
%global date 20260822

Name:           libastal-notifd
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        DBus proxy library for upower daemon.

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
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)


%description
DBus proxy library for upower daemon.

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

%{_bindir}/astal-notifd
%{_libdir}/libastal-notifd.so.*
%{_libdir}/girepository-1.0/AstalNotifd-0.1.typelib

# Devel files
%files devel
%{_libdir}/libastal-notifd.so
%{_libdir}/pkgconfig/astal-notifd-0.1.pc
%{_datadir}/vala/vapi/astal-notifd-0.1.vapi
%{_datadir}/gir-1.0/AstalNotifd-0.1.gir
%{_datadir}/glib-2.0/schemas/io.astal.notifd.gschema.xml
%{_includedir}/astal-notifd.h
