#
# Conditional build:
%bcond_without	pcre8		# 8-bit character support
%bcond_without	pcre16		# 16-bit character support
%bcond_without	pcre32		# 32-bit character support
%bcond_without	static_libs	# static libraries build
%bcond_without	tests		# don't perform "make check"

Summary:	Perl-Compatible Regular Expression library
Summary(pl.UTF-8):	Biblioteka perlowych wyrażeń regularnych
Summary(pt_BR.UTF-8):	Biblioteca de expressões regulares versão
Name:		pcre2
Version:	10.44
Release:	1
License:	BSD (see LICENCE)
Group:		Libraries
Source0:	https://github.com/PhilipHazel/pcre2/releases/download/pcre2-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	9d1fe11e2e919c7b395e3e8f0a5c3eec
URL:		http://www.pcre.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	readline-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE stands for the Perl Compatible Regular Expression library. PCRE2
is a re-working of the original PCRE library to provide an entirely
new API.

%description -l pl.UTF-8
PCRE (Perl-Compatible Regular Expression) oznacza bibliotekę wyrażeń
regularnych kompatybilnych z perlowymi. PCRE2 to przetworzenie
oryginalnej biblioteki PCRE w celu udostępnienia zupełnie nowego API.

%package common-devel
Summary:	Header files for PCRE2 libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek PCRE2
Group:		Development/Libraries

%description common-devel
Header files for PCRE2 libraries.

%description common-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek PCRE2.

%package 8
Summary:	PCRE2 library with 8-bit character support
Summary(pl.UTF-8):	Biblioteka PCRE2 z obsługą znaków 8-bitowych
Group:		Libraries

%description 8
PCRE2 (Perl compatible regular expressions) C library with 8-bit
character support.

%description 8 -l pl.UTF-8
Biblioteka C PCRE2 (perlowych wyrażeń regularnych) z obsługą znaków
8-bitowych.

%package 8-devel
Summary:	Development files for PCRE2 library with 8-bit character support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki PCRE2 z obsługą znaków 8-bitowych
Group:		Development/Libraries
Requires:	%{name}-8 = %{version}-%{release}
Requires:	%{name}-common-devel = %{version}-%{release}

%description 8-devel
Development files for PCRE2 library with 8-bit character support.

%description 8-devel -l pl.UTF-8
Pliki programistyczne biblioteki PCRE2 z obsługą znaków 8-bitowych.

%package 8-static
Summary:	Static PCRE2 library with 8-bit character support
Summary(pl.UTF-8):	Biblioteka statyczna PCRE2 z obsługą znaków 8-bitowych
Group:		Development/Libraries
Requires:	%{name}-8-devel = %{version}-%{release}

%description 8-static
Static PCRE2 library with 8-bit character support.

%description 8-static -l pl.UTF-8
Biblioteka statyczna PCRE2 z obsługą znaków 8-bitowych.

%package posix
Summary:	POSIX compatible inferface to PCRE2 library with 8-bit character support
Summary(pl.UTF-8):	Zgodny z POSIX interfejs do biblioteki PCRE2 z obsługą znaków 8-bitowych
Group:		Libraries
Requires:	%{name}-8 = %{version}-%{release}

%description posix
POSIX compatible inferface to PCRE2 library with 8-bit character
support.

%description posix -l pl.UTF-8
Zgodny z POSIX interfejs do biblioteki PCRE2 z obsługą znaków
8-bitowych.

%package posix-devel
Summary:	Development files for PCRE2 POSIX library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki PCRE2 POSIX
Group:		Development/Libraries
Requires:	%{name}-8-devel = %{version}-%{release}
Requires:	%{name}-posix = %{version}-%{release}

%description posix-devel
Development files for PCRE2 POSIX.

%description posix-devel -l pl.UTF-8
Pliki programistyczne biblioteki PCRE2 POSIX.

%package posix-static
Summary:	Static PCRE2 POSIX library
Summary(pl.UTF-8):	Biblioteka statyczna PCRE2 POSIX
Group:		Development/Libraries
Requires:	%{name}-posix-devel = %{version}-%{release}

%description posix-static
Static PCRE2 POSIX library.

%description posix-static -l pl.UTF-8
Biblioteka statyczna PCRE2 POSIX.

%package 16
Summary:	PCRE2 library with 16-bit character support
Summary(pl.UTF-8):	Biblioteka PCRE2 z obsługą znaków 16-bitowych
Group:		Libraries

%description 16
PCRE2 (Perl compatible regular expressions) C library with 16-bit
character support.

%description 16 -l pl.UTF-8
Biblioteka C PCRE2 (perlowych wyrażeń regularnych) z obsługą znaków
16-bitowych.

%package 16-devel
Summary:	Development files for PCRE2 library with 16-bit character support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki PCRE2 z obsługą znaków 16-bitowych
Group:		Development/Libraries
Requires:	%{name}-16 = %{version}-%{release}
Requires:	%{name}-common-devel = %{version}-%{release}

%description 16-devel
Development files for PCRE2 library with 16-bit character support.

%description 16-devel -l pl.UTF-8
Pliki programistyczne biblioteki PCRE2 z obsługą znaków 16-bitowych.

%package 16-static
Summary:	Static PCRE2 library with 16-bit character support
Summary(pl.UTF-8):	Biblioteka statyczna PCRE2 z obsługą znaków 16-bitowych
Group:		Development/Libraries
Requires:	%{name}-16-devel = %{version}-%{release}

%description 16-static
Static PCRE2 library with 16-bit character support.

%description 16-static -l pl.UTF-8
Biblioteka statyczna PCRE2 z obsługą znaków 16-bitowych.

%package 32
Summary:	PCRE2 library with 32-bit character support
Summary(pl.UTF-8):	Biblioteka PCRE2 z obsługą znaków 32-bitowych
Group:		Libraries

%description 32
PCRE2 (Perl compatible regular expressions) C library with 32-bit
character support.

%description 32 -l pl.UTF-8
Biblioteka C PCRE2 (perlowych wyrażeń regularnych) z obsługą znaków
32-bitowych.

%package 32-devel
Summary:	Development files for PCRE2 library with 32-bit character support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki PCRE2 z obsługą znaków 32-bitowych
Group:		Development/Libraries
Requires:	%{name}-32 = %{version}-%{release}
Requires:	%{name}-common-devel = %{version}-%{release}

%description 32-devel
Development files for PCRE2 library with 32-bit character support.

%description 32-devel -l pl.UTF-8
Pliki programistyczne biblioteki PCRE2 z obsługą znaków 32-bitowych.

%package 32-static
Summary:	Static PCRE2 library with 32-bit character support
Summary(pl.UTF-8):	Biblioteka statyczna PCRE2 z obsługą znaków 32-bitowych
Group:		Development/Libraries
Requires:	%{name}-32-devel = %{version}-%{release}

%description 32-static
Static PCRE2 library with 32-bit character support.

%description 32-static -l pl.UTF-8
Biblioteka statyczna PCRE2 z obsługą znaków 32-bitowych.

%package grep
Summary:	Grep using Perl Compatible Regular Expressions
Summary(pl.UTF-8):	Grep używający perlowych wyrażeń regularnych
Group:		Applications/Text
Requires:	%{name}-8 = %{version}-%{release}

%description grep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%description grep -l pl.UTF-8
pgrep jest programem działającym podobnie do grepa, ale używających
perlowych wyrażeń regularnych, a nie posiksowych.

%package test
Summary:	A program for testing Perl-compatible regular expressions
Summary(pl.UTF-8):	Program do testowania kompatybilnych z perlem wyrażeń regularnych
Group:		Applications/Text
%{?with_pcre8:Requires:	%{name}-8 = %{version}-%{release}}
%{?with_pcre16:Requires:	%{name}-16 = %{version}-%{release}}
%{?with_pcre32:Requires:	%{name}-32 = %{version}-%{release}}

%description test
pcretest is a program which you can use to test regular expression.

%description test -l pl.UTF-8
pcretest jest programem, za pomocą którego można sprawdzić poprawność
wyrażenia regularnego.

%package doc-html
Summary:	Documentation for PCRE2 in HTML format
Summary(pl.UTF-8):	Dokumentacja dla PCRE2 w formacie HTML
Group:		Applications/Text
BuildArch:	noarch

%description doc-html
Documentation for PCRE2 in HTML format.

%description doc-html -l pl.UTF-8
Dokumentacja dla PCRE2 w formacie HTML.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
%ifnarch x32
	--enable-jit \
%endif
	%{?with_pcre8:--enable-pcre2-8} \
	%{?with_pcre16:--enable-pcre2-16} \
	%{?with_pcre32:--enable-pcre2-32} \
	--enable-pcre2grep-libbz2 \
	--enable-pcre2grep-libz \
	--enable-pcre2test-libreadline

%{__make}

%if %{with tests}
# tests need big stack
#ulimit -s 32768
%{__make} -j1 check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpcre2*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/pcre2

%clean
rm -rf $RPM_BUILD_ROOT

%post   8 -p /sbin/ldconfig
%postun 8 -p /sbin/ldconfig

%post   posix -p /sbin/ldconfig
%postun posix -p /sbin/ldconfig

%post	16 -p /sbin/ldconfig
%postun	16 -p /sbin/ldconfig

%post	32 -p /sbin/ldconfig
%postun	32 -p /sbin/ldconfig

%files common-devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING LICENCE NEWS README
%attr(755,root,root) %{_bindir}/pcre2-config
%{_includedir}/pcre2.h
%{_mandir}/man1/pcre2-config.1*
%{_mandir}/man3/pcre2.3*
%{_mandir}/man3/pcre2_*.3*
%{_mandir}/man3/pcre2api.3*
%{_mandir}/man3/pcre2build.3*
%{_mandir}/man3/pcre2callout.3*
%{_mandir}/man3/pcre2compat.3*
%{_mandir}/man3/pcre2convert.3*
%{_mandir}/man3/pcre2demo.3*
%{_mandir}/man3/pcre2jit.3*
%{_mandir}/man3/pcre2limits.3*
%{_mandir}/man3/pcre2matching.3*
%{_mandir}/man3/pcre2partial.3*
%{_mandir}/man3/pcre2pattern.3*
%{_mandir}/man3/pcre2perform.3*
%{_mandir}/man3/pcre2posix.3*
%{_mandir}/man3/pcre2sample.3*
%{_mandir}/man3/pcre2serialize.3*
%{_mandir}/man3/pcre2syntax.3*
%{_mandir}/man3/pcre2unicode.3*

%if %{with pcre8}
%files 8
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcre2-8.so.0

%files 8-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-8.so
%{_pkgconfigdir}/libpcre2-8.pc

%if %{with static_libs}
%files 8-static
%defattr(644,root,root,755)
%{_libdir}/libpcre2-8.a
%endif

%files posix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-posix.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcre2-posix.so.3

%files posix-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-posix.so
%{_includedir}/pcre2posix.h
%{_pkgconfigdir}/libpcre2-posix.pc

%if %{with static_libs}
%files posix-static
%defattr(644,root,root,755)
%{_libdir}/libpcre2-posix.a
%endif
%endif

%if %{with pcre16}
%files 16
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-16.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcre2-16.so.0

%files 16-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-16.so
%{_pkgconfigdir}/libpcre2-16.pc

%if %{with static_libs}
%files 16-static
%defattr(644,root,root,755)
%{_libdir}/libpcre2-16.a
%endif
%endif

%if %{with pcre32}
%files 32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-32.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcre2-32.so.0

%files 32-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre2-32.so
%{_pkgconfigdir}/libpcre2-32.pc

%if %{with static_libs}
%files 32-static
%defattr(644,root,root,755)
%{_libdir}/libpcre2-32.a
%endif
%endif

%if %{with pcre8}
%files grep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcre2grep
%{_mandir}/man1/pcre2grep.1*
%endif

%files test
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcre2test
%{_mandir}/man1/pcre2test.1*

%files doc-html
%defattr(644,root,root,755)
%doc doc/html/*
