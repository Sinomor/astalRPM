%global debug_package %{nil}

Name:           aylurs-gtk-shell
Version:        3.1.2
Release:        1%{?dist}
Summary:        Aylurs's Gtk Shell (AGS), An eww inspired gtk widget system.

License:        GPL-3.0-only 
URL:            https://aylur.github.io/ags
Source0:        https://github.com/Aylur/ags/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  gjs
BuildRequires:  bash
BuildRequires:  nodejs
BuildRequires:  npm

BuildRequires:  pkgconfig(gtk4-layer-shell-0)

Recommends:     dart-sass

%description
Aylurs's Gtk Shell (AGS), An eww inspired gtk widget system.

%prep
%autosetup -n ags-%{version}
npm install

%build
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
%meson
%meson_build


%install
%meson_install

%files
%license LICENSE
%{_prefix}/bin/ags
%{_prefix}/share/ags/
