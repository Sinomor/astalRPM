# Identifying arch (thankfully dart-sass provides multiple arch prebuilt binaries)
%ifarch x86_64
%global dart_arch x64
%endif
%ifarch aarch64
%global dart_arch arm64
%endif
%ifarch armv7hl
%global dart_arch arm
%endif
%ifarch riscv64
%global dart_arch riscv64
%endif
%global debug_package %{nil}

Name:           dart-sass
Version:        1.99.0
Release:        1%{?dist}
Summary:        CSS preprocessor

License:        MIT
URL:            https://sass-lang.com
Source0:        https://github.com/sass/dart-sass/releases/download/%{version}/dart-sass-%{version}-linux-%{dart_arch}.tar.gz

ExclusiveArch:  x86_64 aarch64 armv7hl riscv64

%description
CSS preprocessor written in Dart.

%prep
%autosetup -n dart-sass
cp src/LICENSE LICENSE

%build

%install
mkdir -p %{buildroot}%{_libdir}/dart-sass/src
mkdir -p %{buildroot}%{_bindir}

install -Dm755 sass %{buildroot}%{_libdir}/dart-sass/sass

cp -r src/ %{buildroot}%{_libdir}/dart-sass/
ln -sr %{_libdir}/dart-sass/sass %{buildroot}%{_bindir}/sass

%files
%license LICENSE
%{_bindir}/sass
%{_libdir}/dart-sass/
