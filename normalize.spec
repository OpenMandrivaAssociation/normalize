%define name normalize
%define version 0.7.7
%define release %mkrel 1

Summary:   A tool for adjusting the volume of wave files
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source0:   %{name}-%{version}.tar.bz2
License:   GPL
URL:	   http://normalize.nongnu.org/
Group:     Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: xmms-devel
BuildRequires: audiofile-devel
BuildRequires: mad-devel
BuildRequires: gettext-devel
BuildRequires: automake1.8 libtool autoconf2.5

%description
normalize is an overly complicated tool for adjusting the volume of
wave files to a standard volume level.  This is useful for things like
creating mp3 mixes, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%prep
rm -rf $RPM_BUILD_ROOT    

%setup -q

%build
touch ./AUTHORS ./ABOUT-NLS ./ChangeLog
mkdir -p config
echo "mkdir -p" > config/mkinstalldirs
libtoolize -c -f
aclocal-1.8
automake-1.8 -a -c
autoconf
%configure2_5x --with-audiofile
perl -pi -e 's/mkinstalldirs\s+=.*/mkinstalldirs = mkdir -p /' po/Makefile
%make

%install
rm -rf %buildroot
%makeinstall_std
%{find_lang} %{name}
rm -f %buildroot%_libdir/xmms/Effect/librva.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc README NEWS THANKS TODO
%_bindir/*
%_mandir/man1/normalize*
%_libdir/xmms/Effect/librva.so


