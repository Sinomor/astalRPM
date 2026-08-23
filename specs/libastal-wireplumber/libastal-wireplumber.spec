%global dir lib/wireplumber
%global commit bcd02cbd1391e85f52c5ff63e00708b5b62f55ec
%global date 20260823

Name:           libastal-wireplumber
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        Library for audio control using wireplumber.

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/Aylur/astal/archive/%{commit}/astal-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc

BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)


%description
Library for audio control using wireplumber.

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

%{_libdir}/libastal-wireplumber.so.0*
%{_libdir}/girepository-1.0/AstalWp-0.1.typelib

# Devel files
%files devel
%{_libdir}/libastal-wireplumber.so
%{_libdir}/pkgconfig/astal-wireplumber-0.1.pc
%{_datadir}/vala/vapi/astal-wireplumber-0.1.*
%{_datadir}/gir-1.0/AstalWp-0.1.gir
%{_includedir}/astal-wp.h
%{_includedir}/astal/wireplumber/
