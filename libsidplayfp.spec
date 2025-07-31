%define	sv_major 0
%define	major	6
%define	libname	%mklibname sidplayfp
%define	oldlibname	%mklibname sidplayfp 0
%define	libnamedev	%mklibname -d sidplayfp
%define	develnamestatic	%mklibname sidplayfp -d -s

Summary:	A library for the sidplay2 fork with resid-fp
Name:	libsidplayfp
Version:	2.15.0
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://github.com/libsidplayfp/libsidplayfp
Source0:	https://downloads.sourceforge.net/project/sidplay-residfp/libsidplayfp/1.0/libsidplayfp-%{version}.tar.gz
Source100:	libsidplayfp.rpmlintrc
BuildRequires:	doxygen
BuildRequires:	pkgconfig(libgcrypt)

%description
We aim to improve the quality of emulating the 6581 and 8580 chips and
the surrounding C64 system in order to play SID music better.

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for %{name}
Group:	system/Libraries
%rename %{oldlibname}

%description -n %{libname}
We aim to improve the quality of emulating the 6581 and 8580 chips and
the surrounding C64 system in order to play SID music better.
This package contains the shared library.

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*
%{_libdir}/libstilview.so.%{sv_major}*

#-----------------------------------------------------------------------------

%package -n %{libnamedev}
Summary: 	Libraries and headers for %{name}
Group:	Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	sidplayfp-devel = %{version}-%{release}

%description -n %{libnamedev}
This  package contains the libraries and header files needed to develop
programs which make use of %{name}. The library documentation is available
on header files.

%files -n %{libnamedev}
%doc AUTHORS README COPYING
%doc docs/html/*
%dir %{_includedir}/sidplayfp
%dir %{_includedir}/stilview
%{_includedir}/sidplayfp/*
%{_includedir}/stilview/*.h
%{_libdir}/%{name}.so
%{_libdir}/libstilview.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/libstilview.pc

#-----------------------------------------------------------------------------

%package -n %{develnamestatic}
Summary:	Library for accessing files in FITS format for C and Fortran
Group:		Development/C
Requires:	%{libnamedev} = %version
Requires:	%libname = %version
Provides:	sidplayfp-devel-static = %{version}-%{release}

%description -n %{develnamestatic}
This package contains the static libraries used by software that uses
%{name}.

%files -n %{develnamestatic}
%{_libdir}/*.a

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%configure --enable-static \
%ifarch aarch64
					--with-simd=none \
%endif
					--with-gcrypt \
					--with-hardsid

%make_build

# Do also devel docs
%make_build doc


%install
%make_install
