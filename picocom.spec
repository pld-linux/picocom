# TODO:
# - build documentation, don't take the included ones
# - use included apps for transfer and recving files
Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (‰hnlich Telix)
Summary(es):	Paquete de comunicaciones modo texto a la Telix
Summary(fi):	Tietoliikenneohjelma, kuten Telix
Summary(fr):	Package de communication en mode terminal ‡ la Telix
Summary(pl):	Program komunikacyjny (podobny do Teliksa)
Summary(pt_BR):	Pacote de comunicaÁıes modo texto a la Telix
Summary(ru):	ÎœÕÕ’Œ…À¡√…œŒŒŸ  –¡À≈‘ ‘…–¡ Telix ƒÃ— ‘≈À”‘œ◊œ«œ “≈÷…Õ¡
Summary(tr):	Telix benzeri, TTY kipi ileti˛im paketi
Summary(uk):	ÎœÕ’Œ¶À¡√¶ Œ…  –¡À≈‘ ‘…–’ Telix ƒÃ— ‘≈À”‘œ◊œ«œ “≈÷…Õ’
Summary(zh_CN):	“ª∏ˆŒƒ±æΩÁ√Êµƒµ˜ ‘Ω‚µ˜∆˜øÿ÷∆∆˜∫Õ÷’∂Àƒ£ƒ‚∆˜°£
Name:		picocom
Version:	1.4
Release:	2
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://efault.net/npat/hacks/picocom/dist/%{name}-%{version}.tar.gz
# Source0-md5:	08fcc5f6bb9e7676a2569386d5ea9f70
Source1:	%{name}-ttyS0.desktop
Source2:	%{name}-ttyS1.desktop
Source3:	%{name}.png
Patch0:		%{name}-ascii_xfr.patch
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
jest "pico" zamiast "mini". Zosta≥ zaprojektowany aby s≥uøyÊ za prosty
program do rÍcznej konfiguracji i testÛw modemÛw oraz narzÍdzie do
rozwi±zywania problemÛw. S≥uøy≥ teø (dosyÊ dobrze) jako "okno
terminala" umoøliwiajace administratorowi interweniowanie w skryptach
po≥±czeÒ PPP (co∂ w rodzaju "otwÛrz okno terminala przed / po
dzwonieniu" z MS Windows). Moøe siÍ okazaÊ przydatny takøe przy innych
podobnych zadaniach. Jest idealny dla systemÛw wbudowanych, jako øe ma
bardzo ma≥y narzut pamiÍciowy (poniøej 20kB po zestripowaniu). OprÛcz
bycia ma≥ym przydatnym narzÍdziem, picocom w swoich ºrÛd≥ach zawiera
prost±, ≥atw± w uøyciu i obszernie udokumentowan± bibliotekÍ
zarz±dzania terminalem, mog±c± s≥uøyÊ takøe innym projektom.
Biblioteka ta ukrywa wywo≥ania termios(3) i udostÍpnia mniej z≥oøony i
bezpieczniejszy (choÊ o nieco mniejszych moøliwo∂ciach) interfejs.

%prep
%setup -q
%patch0 -p1

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
