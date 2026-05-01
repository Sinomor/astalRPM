Name:           sndio
Version:        1.10.0
Release:        1%{?dist}
Summary:        A small audio and MIDI framework

License:        ISC
URL:            https://sndio.org
Source0:        https://github.com/ratchov/sndio/archive/refs/tags/v%{version}.tar.gz
Source1:        sndio.sysusers

BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(alsa)

%description
A small audio and MIDI framework.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for the sndio audio and MIDI framework.

%prep
%autosetup

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir}
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
%make_install
install -m 0644 -D %{SOURCE1} %{buildroot}%{_sysusersdir}/sndio.conf
mkdir -p %{buildroot}%{_sharedstatedir}/sndios

%pre
%sysusers_create_compat %{SOURCE1}

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/aucat
%{_bindir}/midicat
%{_bindir}/sndioctl
%{_bindir}/sndiod
%{_libdir}/libsndio.so.7*
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_sysusersdir}/sndio.conf
%dir %attr(0700, sndiod, sndiod) %{_sharedstatedir}/sndios

%files devel
%{_includedir}/sndio.h
%{_libdir}/libsndio.so
%{_libdir}/pkgconfig/sndio.pc
%{_mandir}/man3/*
