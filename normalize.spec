%define name normalize
%define version 0.7.7
%define release %mkrel 11

# --with xmms, default off
%bcond_with	xmms

Summary:	A tool for adjusting the volume of wave files
Name:		normalize
Version:	0.7.7
Release:	11
Source0:	%{name}-%{version}.tar.bz2
Patch0:		compressed-wav-files.dpatch
Patch1:		fix-flac.dpatch
Patch2:		normalize-fix-local-config.patch
License:	GPLv2+
URL:		http://normalize.nongnu.org/
Group:		Sound
%if %with xmms
BuildRequires:	xmms-devel
%endif
BuildRequires:  audiofile-devel
BuildRequires:  mad-devel
BuildRequires:  gettext-devel
BuildRequires:  automake1.8 libtool autoconf2.5

%description
normalize is an overly complicated tool for adjusting the volume of
wave files to a standard volume level. This is useful for things like
creating mp3 mixes, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_5x --with-audiofile \
%if %with xmms
	--enable-xmms
%else
	--disable-xmms
%endif
perl -pi -e 's/mkinstalldirs\s+=.*/mkinstalldirs = mkdir -p /' po/Makefile
%make

%install
%makeinstall_std
%{find_lang} %{name}
rm -f %{buildroot}%{_libdir}/xmms/Effect/librva.la

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc README NEWS THANKS TODO
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*
%if %with xmms
%{_libdir}/xmms/Effect/librva.so
%endif

