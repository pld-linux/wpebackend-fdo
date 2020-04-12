# TODO: apidocs (BR: hotdoc, like libwpe.spec)
Summary:	A WPE backend designed for Linux desktop systems
Summary(pl.UTF-8):	Backend WPE zaprojektowany dla biurkowych systemów linuksowych
Name:		wpebackend-fdo
Version:	1.6.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://wpewebkit.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	456afeed22f6749f7b2a97c11660835d
Patch0:		%{name}-libdir.patch
URL:		https://wpewebkit.org/
BuildRequires:	EGL-devel
BuildRequires:	cmake >= 3.3
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libwpe-devel >= 1.6.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	wayland-devel >= 1.10
BuildRequires:	wayland-egl-devel >= 1.10
Requires:	libwpe >= 1.6.0
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
Requires:	libwpe-devel >= 1.6.0

%description devel
Header files for WPEBackend-fdo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WPEBackend-fdo.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
