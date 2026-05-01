%global dir subprojects/appmenu-glib-translator
%global commit aea4ea398b7c75494f23f5e5bdb4f495d615059f
%global date 20260430

Name:           appmenu-glib-translator
Version:        25.04
Release:        1.%{date}git%(c=%{commit}; echo ${c:0:7})%{?dist}
Summary:        GLib-based library for translating DBusMenu-exported menus into GMenuModels.

License:        LGPL-3.0-or-later
URL:            https://gitlab.com/vala-panel-project/vala-panel-appmenu
Source0:        https://gitlab.com/vala-panel-project/vala-panel-appmenu/-/archive/%{commit}/vala-panel-appmenu-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  valadoc

BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)


%description
GLib-based library for translating DBusMenu-exported menus into GMenuModels.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and VAPI files for %{name}.

%prep
%autosetup -n vala-panel-appmenu-%{commit}

%build
cd %{dir}
%meson
%meson_build

%install
cd %{dir}
%meson_install

%files
%license LICENSE
%{_libdir}/libappmenu-glib-translator.so.*
%{_libdir}/girepository-1.0/AppmenuGLibTranslator-25.04.typelib

%files devel
%{_libdir}/libappmenu-glib-translator.so
%{_libdir}/pkgconfig/appmenu-glib-translator.pc
%{_datadir}/vala/vapi/appmenu-glib-translator.*
%{_datadir}/gir-1.0/AppmenuGLibTranslator-25.04.gir
%{_includedir}/appmenu-glib-translator
