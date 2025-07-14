Summary:	Hardware detection library
Summary(pl.UTF-8):	Biblioteka wykrywająca sprzęt
Name:		detect
Version:	0.9.72
Release:	3
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.linux-mandrake.com/pub/harddrake/SOURCES/%{name}-%{version}.tar.bz2
# Source0-md5:	0e001355ad217ce907c5ce95673ab4a4
Patch0:		%{name}-sound.patch
Patch1:		%{name}-po.patch.bz2
# Patch1-md5:	b01b0b1f10895628ab0f40daa855d2e9
Patch2:		%{name}-ppc.patch
Patch3:		%{name}-ppc2.patch
Patch4:		%{name}-ia64-io-h.patch
Patch5:		%{name}-kver-ppc.patch
Patch6:		%{name}-0.9.72-alpha.patch
Patch7:		%{name}-0.9.72-cpu-detect-ppc.patch
Patch8:		%{name}-acam.patch
URL:		http://www.linux-mandrake.com/harddrake/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-tools
%ifarch %{ix86}
BuildRequires:	isapnptools-devel
%endif
BuildRequires:	libtool
BuildRequires:	texinfo
%ifarch %{ix86}
Requires:	isapnptools >= 1.21
%endif
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libdetect is a library for hardware detection. The API is easy to
learn. The following hardware can be detected: CPU, Memory, Disk &
partitions, Ethernet cards, Floppy drives, Modem, Mouse, SCSI, Sound
cards, Video cards, Scanners.

%description -l pl.UTF-8
libdetect to biblioteka do wykrywania sprzętu. Jej API jest łatwe do
nauczenia. Może wykryć następujący sprzęt: procesor, pamięć, dyski i
partycje, karty sieciowe, stacje dysków, modemy, myszy, SCSI, karty
dźwiękowe, karty graficzne, skanery.

%package libs
Summary:	The detect library itself, necessary to run the detect utility
Summary(pl.UTF-8):	Właściwa biblioteka, niezbędna do działania narzędzia detect
Group:		Libraries
Obsoletes:	libdetect

%description libs
Libdetect is a library for hardware detection. The API is easy to
learn. The following hardware can be detected: CPU, Memory, Disk &
partitions, Ethernet cards, Floppy drives, Modem, Mouse, SCSI, Sound
cards, Video cards, Scanners. This package contains the detect library
itself, necessary to run the detect utility.

%description libs -l pl.UTF-8
libdetect to biblioteka do wykrywania sprzętu. Jej API jest łatwe do
nauczenia. Może wykryć następujący sprzęt: procesor, pamięć, dyski i
partycje, karty sieciowe, stacje dysków, modemy, myszy, SCSI, karty
dźwiękowe, karty graficzne, skanery. Ten pakiet zawiera właściwą
bibliotekę, niezbędną do działania narzędzia wykrywającego (polecenia
detect).

%package libs-devel
Summary:	Header files for developing apps which will use detect
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów używających detect
Group:		Development/Libraries
Requires:	detect-libs = %{version}
Obsoletes:	detect-devel
Obsoletes:	libdetect-devel

%description libs-devel
Header files for developing apps which will use detect library.

%description libs-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów używających biblioteki detect.

%package libs-static
Summary:	Static detect library
Summary(pl.UTF-8):	Statyczna biblioteka detect
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}

%description libs-static
Static version of detect library.

%description libs-static -l pl.UTF-8
Statyczna wersja biblioteki detect.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%ifarch ppc
%patch -P5 -p1
%patch -P7 -p1
%endif
%ifarch alpha
%patch -P6 -p1
%endif
%patch -P8 -p1
ma acconfig.h config.h.in

%build
rm -f missing
CFLAGS="%{rpmcflags} -I%{_includedir}/isapnp"
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure
cat po/Makefile.in > po/Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang detect

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README docs/FAQ
%attr(755,root,root) %{_sbindir}/detect

%files libs -f detect.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/detect

%files libs-devel
%defattr(644,root,root,755)
%doc docs/{Programming,API,ISA-Structure,PCI-Structure}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/detect.h

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libdetect.a
