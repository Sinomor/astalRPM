Name:           libastal-meta
Version:        0.1.0
Release:        1%{?dist}
Summary:        Libastal meta package, including all libastal services

License:        LGPL-2.1-only
URL:            https://aylur.github.io/astal
BuildArch:      noarch

Requires:       libastal-3
Requires:       libastal-4
Requires:       libastal-apps
Requires:       libastal-auth
Requires:       libastal-battery
Requires:       libastal-bluetooth
Requires:       libastal-brightness
Requires:       libastal-cava
Requires:       libastal-greetd
Requires:       libastal-hyprland
Requires:       libastal-io
Requires:       libastal-mpris
Requires:       libastal-network
Requires:       libastal-niri
Requires:       libastal-notifd
Requires:       libastal-powerprofiles
Requires:       libastal-river
Requires:       libastal-tray
Requires:       libastal-wireplumber
Requires:       libastal-wl

%description
Libastal meta package, including all libastal services.

%package        devel
Summary:        Libastal meta package for all astal development files
Requires:       %{name} = %{version}-%{release}

Requires:       libastal-3-devel
Requires:       libastal-4-devel
Requires:       libastal-apps-devel
Requires:       libastal-auth-devel
Requires:       libastal-battery-devel
Requires:       libastal-bluetooth-devel
Requires:       libastal-brightness-devel
Requires:       libastal-cava-devel
Requires:       libastal-greetd-devel
Requires:       libastal-hyprland-devel
Requires:       libastal-io-devel
Requires:       libastal-mpris-devel
Requires:       libastal-network-devel
Requires:       libastal-niri-devel
Requires:       libastal-notifd-devel
Requires:       libastal-powerprofiles-devel
Requires:       libastal-river-devel
Requires:       libastal-tray-devel
Requires:       libastal-wireplumber-devel
Requires:       libastal-wl-devel

%description    devel
Libastal meta package for all astal development files.
