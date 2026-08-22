%define _lto_cflags %{nil}
%global _lto_cflags %{nil}

Name:           libcava
Version:        1.0.0 
Release:        1%{?dist}
Summary:        Fork to provide cava as a shared library, e.g. used by waybar. Cava is not provided as executable.

License:        MIT
URL:            https://github.com/LukashonakV/cava
Source0:        https://github.com/LukashonakV/cava/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sndio)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpipewire-0.3)

%description
Fork to provide cava as a shared library, e.g. used by waybar. Cava is not provided as executable.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n cava-%{version}
ls example_files/config
ls output/shaders/bar_spectrum.frag

%build
%meson -Dcava_font=false \
    -Dc_args="%{build_cflags}" \
    -Dc_link_args="%{build_ldflags}"
%meson_build


%install
%meson_install

# just filesss
%files
%license LICENSE
%{_libdir}/libcava.so.*

# devellll
%files devel
%{_includedir}/cava/
%{_libdir}/pkgconfig/libcava.pc
%{_libdir}/libcava.so
