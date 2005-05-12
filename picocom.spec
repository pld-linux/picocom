# TODO:
# - build documentation, don't take the included ones
Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (ähnlich Telix)
Summary(es):	Paquete de comunicaciones modo texto a la Telix
Summary(fi):	Tietoliikenneohjelma, kuten Telix
Summary(fr):	Package de communication en mode terminal à la Telix
Summary(pl):	Program komunikacyjny (podobny do Teliksa)
Summary(pt_BR):	Pacote de comunicações modo texto a la Telix
Summary(ru):	ëÏÍÍÕÎÉËÁÃÉÏÎÎÙÊ ĞÁËÅÔ ÔÉĞÁ Telix ÄÌÑ ÔÅËÓÔÏ×ÏÇÏ ÒÅÖÉÍÁ
Summary(tr):	Telix benzeri, TTY kipi iletişim paketi
Summary(uk):	ëÏÍÕÎ¦ËÁÃ¦ÊÎÉÊ ĞÁËÅÔ ÔÉĞÕ Telix ÄÌÑ ÔÅËÓÔÏ×ÏÇÏ ÒÅÖÉÍÕ
Summary(zh_CN):	Ò»¸öÎÄ±¾½çÃæµÄµ÷ÊÔ½âµ÷Æ÷¿ØÖÆÆ÷ºÍÖÕ¶ËÄ£ÄâÆ÷¡£
Name:		picocom
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://efault.net/npat/hacks/picocom/dist/%{name}-%{version}.tar.gz
# Source0-md5:	08fcc5f6bb9e7676a2569386d5ea9f70
Source1:	%{name}-ttyS0.desktop
Source2:	%{name}-ttyS1.desktop
Source3:	%{name}.png
URL:		http://efault.net/npat/hacks/picocom/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As its name suggests, picocom is a minimal dumb-terminal emulation
program. It is, in principle, very much like minicom, only it's pico
instead of mini! It was designed to serve as a simple, manual, modem
configuration, testing, and debugging tool. It has also served (quite
well) as a low-tech "terminal-window" to allow operator intervention
in PPP connection scripts (something like the MS Windows "open
terminal window before / after dialing" feature). It could also prove
useful in many other similar tasks. It is ideal for embedded systems
since its memory footprint is minimal (less than 20K, when stripped).
Apart from being a handy little tool, picocom source distribution
includes a simple, easy to use, and thoroughly documented
terminal-management library, which could serve other projects as well.
This library hides the termios(3) calls, and provides a less complex
and safer (though certainly less feature-rich) interface.

%description -l pl
Jak sama nazwa sugeruje picocom to minimalny program do emulacji
prymitywnego terminala "dumb". Jest bardzo podobny do minicoma, ale
jest "pico" zamiast "mini". Zosta³ zaprojektowany aby s³u¿yæ za prosty
program do rêcznej konfiguracji i testów modemów oraz narzêdzie do
rozwi±zywania problemów. S³u¿y³ te¿ (dosyæ dobrze) jako "okno
terminala" umo¿liwiajace administratorowi interweniowanie w skryptach
po³±czeñ PPP (co¶ w rodzaju "otwórz okno terminala przed / po
dzwonieniu" z MS Windows). Mo¿e siê okazaæ przydatny tak¿e przy innych
podobnych zadaniach. Jest idealny dla systemów wbudowanych, jako ¿e ma
bardzo ma³y narzut pamiêciowy (poni¿ej 20kB po zestripowaniu). Oprócz
bycia ma³ym przydatnym narzêdziem, picocom w swoich ¼ród³ach zawiera
prost±, ³atw± w u¿yciu i obszernie udokumentowan± bibliotekê
zarz±dzania terminalem, mog±c± s³u¿yæ tak¿e innym projektom.
Biblioteka ta ukrywa wywo³ania termios(3) i udostêpnia mniej z³o¿ony i
bezpieczniejszy (choæ o nieco mniejszych mo¿liwo¶ciach) interfejs.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install picocom pcxm pczm pcasc pcym $RPM_BUILD_ROOT%{_bindir}
install picocom.8 $RPM_BUILD_ROOT%{_mandir}/man8

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS NEWS README *.html *.ps
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man8/*.8*
