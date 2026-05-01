%global debug_package %{nil}

Name:           wl-vapi-gen
Version:        1.1.0
Release:        1%{?dist}
Summary:        Generate vala bindings for wayland protocols.

License:        MIT
URL:            https://codeberg.org/kotontrion/wl-vapi-gen
Source0:        https://codeberg.org/kotontrion/wl-vapi-gen/archive/%{version}.tar.gz

BuildArch:     noarch

BuildRequires: python3 
BuildRequires: meson

Requires: python3

%description
Generate vala bindings for wayland protocols

%prep
%autosetup -n %{name}


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%{_bindir}/wl-vapi-gen
%{_datadir}/pkgconfig/wl-vapi-gen.pc 
