#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	A WPE backend designed for Linux desktop systems
Summary(pl.UTF-8):	Backend WPE zaprojektowany dla biurkowych systemów linuksowych
Name:		wpebackend-fdo
Version:	1.14.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://wpewebkit.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	ab73398b1e35495977e50bee103969d2
URL:		https://wpewebkit.org/
BuildRequires:	EGL-devel
BuildRequires:	glib2-devel >= 2.0
%{?with_apidocs:BuildRequires:	hotdoc}
BuildRequires:	libepoxy-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libwpe-devel >= 1.14.0
BuildRequires:	meson >= 0.49
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	wayland-devel >= 1.15
BuildRequires:	wayland-egl-devel >= 1.15
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	libwpe >= 1.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A WPE backend designed for Linux desktop systems.

%description -l pl.UTF-8
Backend WPE zaprojektowany dla biurkowych systemów linuksowych.

%package devel
Summary:	Header files for WPEBackend-fdo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WPEBackend-fdo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libwpe-devel >= 1.14.0

%description devel
Header files for WPEBackend-fdo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WPEBackend-fdo.

%package apidocs
Summary:	API documentation for WPEBackend-fdo library
Summary(pl.UTF-8):	Dokumentacja API biblioteki WPEBackend-fdo
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for WPEBackend-fdo library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki WPEBackend-fdo.

%prep
%setup -q

%build
%meson build \
	%{?with_apidocs:-Dbuild_docs=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_libdir}/libWPEBackend-fdo-1.0.so.1.*
%attr(755,root,root) %ghost %{_libdir}/libWPEBackend-fdo-1.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWPEBackend-fdo-1.0.so
%{_includedir}/wpe-fdo-1.0
%{_pkgconfigdir}/wpebackend-fdo-1.0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_docdir}/WPEBackend-fdo
%endif
