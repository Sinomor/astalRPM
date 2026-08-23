%global dir lib/battery
%global commit bcd02cbd1391e85f52c5ff63e00708b5b62f55ec
%global date 20260823

Name:           libastal-battery
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

BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)


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

%{_bindir}/astal-battery
%{_libdir}/libastal-battery.so.*
%{_libdir}/girepository-1.0/AstalBattery-0.1.typelib

# Devel files
%files devel
%{_libdir}/libastal-battery.so
%{_libdir}/pkgconfig/astal-battery-0.1.pc
%{_datadir}/vala/vapi/astal-battery-0.1.vapi
%{_datadir}/gir-1.0/AstalBattery-0.1.gir
%{_includedir}/astal-battery.h


