# --with xmms, default off
%bcond_with	xmms

Summary:	A tool for adjusting the volume of wave files
Name:		normalize
Version:	0.7.7
Release:	15
Group:		Sound
License:	GPLv2
Url:		http://normalize.nongnu.org/
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
Patch0:		compressed-wav-files.dpatch
Patch1:		fix-flac.dpatch
Patch2:		normalize-0.7.7-audiofile-pkgconfig.patch
Patch3:		%{name}-%{version}-m4.patch
Patch4:		normalize-automake-1.13.patch
%if %with xmms
BuildRequires:	xmms-devel
%endif
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(mad)

%track
prog %{name} = {
	url = http://normalize.nongnu.org/
	version = %{version}
	regex = %{name}-(__VER__)\.tar\.bz2
}

%description
normalize is an overly complicated tool for adjusting the volume of
wave files to a standard volume level.  This is useful for things like
creating mp3 mixes, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%prep

%setup -q
%apply_patches
touch ./AUTHORS ./ABOUT-NLS ./ChangeLog
autoreconf -fi

%build
%configure2_5x \
	--with-audiofile \
%if %with xmms
	--enable-xmms
%else
	--disable-xmms
%endif
perl -pi -e 's/mkinstalldirs\s+=.*/mkinstalldirs = mkdir -p /' po/Makefile
%make

%install
%makeinstall_std
%find_lang %{name}
rm -f %{buildroot}%{_libdir}/xmms/Effect/librva.la

%files -f %{name}.lang
%doc README NEWS THANKS TODO
%{_bindir}/*
%{_mandir}/man1/normalize*
%if %with xmms
%{_libdir}/xmms/Effect/librva.so
%endif

