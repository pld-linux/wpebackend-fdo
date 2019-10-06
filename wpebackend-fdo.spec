Summary:	A WPE backend designed for Linux desktop systems
Name:		wpebackend-fdo
Version:	1.4.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://wpewebkit.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	63553c3f43593c2a8c587c32e88fdf3c
URL:		https://wpewebkit.org/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	libwpe-devel
BuildRequires:	wayland-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A WPE backend designed for Linux desktop systems.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
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

%changelog
