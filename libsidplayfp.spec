%define major       0
%define libname    %mklibname sidplayfp %{major}
%define libnamedev  %mklibname -d sidplayfp
%define develnamestatic %mklibname sidplayfp -d -s

Name:           libsidplayfp
Version:        1.5.3
Release:        1
License:        GPLv2
Url:		http://sourceforge.net/projects/sidplay-residfp
Source0:	http://downloads.sourceforge.net/project/sidplay-residfp/libsidplayfp/1.0/libsidplayfp-%{version}.tar.gz
Group:		System/Libraries
Summary:        A library for the sidplay2 fork with resid-fp

%description
We aim to improve the quality of emulating the 6581
8580 chips and the surrounding C64 system in order
to play SID music better.

%package -n     %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
We aim to improve the quality of emulating the 6581
8580 chips and the surrounding C64 system in order
to play SID music better. 


%package -n     %{libnamedev}
Summary:        Libraries and headers for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       sidplayfp-devel = %{version}-%{release}

%description -n %{libnamedev}
%{libnamedev} contains the libraries and header files needed to
develop programs which make use of %{name}.
The library documentation is available on header files.



%package -n	%{develnamestatic}
License:	GPLv2
Summary:	Library for accessing files in FITS format for C and Fortran
Group:		System/Libraries
Requires:	%{libnamedev} = %version
Requires:	%libname = %version
Provides:       sidplayfp-devel-static = %{version}-%{release}

%description -n %{develnamestatic}
This package contains the headers required for compiling software that uses
the %{name} library


%prep
%setup -q

%build
%configure --enable-static
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}%{_prefix}

find %{buildroot} -type f -name '*.la' -exec rm -f {} \;

%files 
%doc AUTHORS README COPYING
#%{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/*.so.*


%files -n %{libnamedev}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{develnamestatic}
%{_libdir}/*.a
