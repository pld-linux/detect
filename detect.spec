Summary:	Hardware detection library
Name:		detect
Version:	0.9.72
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.linux-mandrake.com/pub/harddrake/SOURCES/%{name}-%{version}.tar.bz2
Patch0:		%{name}-sound.patch.bz2
Patch1:		%{name}-po.patch.bz2
Patch2:		%{name}-ppc.patch.bz2
Patch3:		%{name}-ppc2.patch.bz2
Patch4:		%{name}-ia64-io-h.patch.bz2
Patch5:		%{name}-kver-ppc.patch.bz2
Patch6:		%{name}-0.9.72-alpha.patch.bz2
Patch7:		%{name}-0.9.72-cpu-detect-ppc.patch.bz2
URL:		http://www.linux-mandrake.com/harddrake/
%ifarch %{ix86}
BuildRequires:	isapnptools-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	texinfo
%ifarch %{ix86}
Requires:	isapnptools >= 1.21
Requires:	detect-lst
%endif
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libdetect is a library for hardware detection. The API is easy to
learn. The following hardware can be detected: CPU, Memory, Disk &
partitions, Ethernet cards, Floppy drives, Modem, Mouse, SCSI, Sound
cards, Video cards, Scanners.

%package libs
Summary:	The detect library itself. Necessary to run the detect utility.
Group:		Libraries
Provides:	libdetect

%description libs
Libdetect is a library for hardware detection. The API is easy to
learn. The following hardware can be detected: CPU, Memory, Disk &
partitions, Ethernet cards, Floppy drives, Modem, Mouse, SCSI, Sound
cards, Video cards, Scanners. This package contains the detect library
itself, necessary to run the detect utility.

%package libs-devel
Summary:	Header files and libraries for developing apps which will use detect
Group:		Development/Libraries
Requires:	detect-libs = %{version}
Provides:	detect-devel, libdetect-devel
Obsoletes:	detect-devel

%description libs-devel
Detect is a library for hardware detection. The API is easy to learn.
The following hardware can be detected: CPU, Memory, Disk &
partitions, Ethernet cards, Floppy drives, Modem, Mouse, SCSI, Sound
cards, Video cards, Scanners.

%package libs-static
Summary:	Header files and static libraries for developing apps which will use detect
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description libs-static
Detect is a library for hardware detection. The API is easy to learn.
he following hardware can be detected: CPU, Memory, Disk & partitions,
Ethernet cards, Floppy drives, Modem, Mouse, SCSI, Sound cards, Video
cards, Scanners.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n detect
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%ifarch ppc
%patch5 -p1
%patch7 -p1
%endif
%ifarch alpha
%patch6 -p1
%endif

%build
rm -f missing
CFLAGS="%{rpmcflags} -I%{_includedir}/isapnp"
%{__libtoolize}
%{__gettextize}
aclocal
%{__autoconf}
%{__automake}
autoheader
%configure
cat po/Makefile.in > po/Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
#make install \
#	prefix=$RPM_BUILD_ROOT%{prefix} \
#	mandir=$RPM_BUILD_ROOT%{_mandir} \
#	libdir=$RPM_BUILD_ROOT%{_libdir} \
#	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
#	datadir=$RPM_BUILD_ROOT%{_datadir} \
#	includedir=$RPM_BUILD_ROOT%{_includedir}

#not installed by make install script

cd $RPM_BUILD_ROOT%{prefix}/lib && {
ln -s libdetect.so.0.0.0 libdetect.so.0
ln -s libdetect.so.0.0.0 libdetect.so
}


%find_lang detect

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO VERSION docs/FAQ
%attr(755,root,root) %{_sbindir}/detect

%files libs -f detect.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdetect.so.*

%files libs-devel
%defattr(644,root,root,755)
%doc docs/{Programming,API,ISA-Structure,PCI-Structure}
%{_libdir}/libdetect.la
%{_libdir}/libdetect.so
%{_includedir}/detect.h

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libdetect.a
