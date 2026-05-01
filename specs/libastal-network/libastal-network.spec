%global dir lib/network
%global commit 6e9ed352252f663b0be9dcbc8c60c4ea4a0dcc47
%global date 20260430

Name:           libastal-network
Version:        0.1.0 
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        NetworkManager wrapper library.

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal 
Source0:        https://github.com/Aylur/astal/archive/%{commit}/astal-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc

BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)


%description
NetworkManager wrapper library.

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

%{_libdir}/libastal-network.so.*
%{_libdir}/girepository-1.0/AstalNetwork-0.1.typelib

# Devel files
%files devel
%{_libdir}/libastal-network.so
%{_libdir}/pkgconfig/astal-network-0.1.pc
%{_datadir}/vala/vapi/astal-network-0.1.vapi
%{_datadir}/gir-1.0/AstalNetwork-0.1.gir
%{_includedir}/astal-network.h
