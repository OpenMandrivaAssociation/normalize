# --with xmms, default off
%bcond_with	xmms

Summary:   A tool for adjusting the volume of wave files
Name:      normalize
Version:   0.7.7
Release:   12
Source0:   http://savannah.nongnu.org/download/%name/%{name}-%{version}.tar.bz2
Patch0:		compressed-wav-files.dpatch
Patch1:		fix-flac.dpatch
Patch2:		normalize-0.7.7-audiofile-pkgconfig.patch
Patch3:   	%{name}-%{version}-m4.patch
Patch4:		normalize-automake-1.13.patch
License:   GPL
URL:	   http://normalize.nongnu.org/
Group:     Sound
%if %with xmms
BuildRequires: xmms-devel
%endif
BuildRequires: audiofile-devel
BuildRequires: mad-devel
BuildRequires: gettext-devel
BuildRequires: automake1.8 libtool autoconf2.5

%track
prog %name = {
	url = http://normalize.nongnu.org/
	version = %version
	regex = %name-(__VER__)\.tar\.bz2
}

%description
normalize is an overly complicated tool for adjusting the volume of
wave files to a standard volume level.  This is useful for things like
creating mp3 mixes, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%prep

%setup -q
%apply_patches

%build
touch ./AUTHORS ./ABOUT-NLS ./ChangeLog
libtoolize --install --copy --force --automake
aclocal -I m4
autoconf
autoheader
automake --add-missing --copy --foreign
%configure2_5x --with-audiofile \
%if %with xmms
	--enable-xmms
%else
	--disable-xmms
%endif
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
%if %with xmms
%_libdir/xmms/Effect/librva.so
%endif



%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.7-10mdv2011.0
+ Revision: 666619
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.7-9mdv2011.0
+ Revision: 606824
- rebuild

* Wed Jan 13 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.7-8mdv2010.1
+ Revision: 490983
- added two debian patches from normalize-audio_0.7.7-6.diff.gz

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.7.7-7mdv2010.0
+ Revision: 426253
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.7.7-6mdv2009.1
+ Revision: 351635
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.7.7-5mdv2009.0
+ Revision: 223347
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.7.7-3mdv2008.1
+ Revision: 153285
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Aug 04 2007 Anssi Hannula <anssi@mandriva.org> 0.7.7-2mdv2008.0
+ Revision: 58960
- add xmms build option for the xmms plugin, disable by default


* Tue Jan 23 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.7-1mdv2007.0
+ Revision: 112550
- New version 0.7.7

* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 0.7.6-7mdv2007.1
+ Revision: 108135
- Import normalize

* Fri Jan 12 2007 G�tz Waschk <waschk@mandriva.org> 0.7.6-7mdv2007.1
- rebuild

* Sun Oct 02 2005 Couriousous <couriousous@mandriva.org> 0.7.6-7mdk
- Try to fix x86_64 build ( aka autotools breakage )

* Wed Oct 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.6-6mdk
- rebuild

