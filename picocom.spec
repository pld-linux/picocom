# TODO:
# - use included apps for transfer and recving files
Summary:	TTY mode communications package ala Telix
Summary(de.UTF-8):   TTY-Modus-Kommunikationspaket (ähnlich Telix)
Summary(es.UTF-8):   Paquete de comunicaciones modo texto a la Telix
Summary(fi.UTF-8):   Tietoliikenneohjelma, kuten Telix
Summary(fr.UTF-8):   Package de communication en mode terminal à la Telix
Summary(pl.UTF-8):   Program komunikacyjny (podobny do Teliksa)
Summary(pt_BR.UTF-8):   Pacote de comunicações modo texto a la Telix
Summary(ru.UTF-8):   Коммуникационный пакет типа Telix для текстового режима
Summary(tr.UTF-8):   Telix benzeri, TTY kipi iletişim paketi
Summary(uk.UTF-8):   Комунікаційний пакет типу Telix для текстового режиму
Summary(zh_CN.UTF-8):   一个文本界面的调试解调器控制器和终端模拟器。
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
BuildRequires:	groff
BuildRequires:	xmlmp
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

%description -l pl.UTF-8
Jak sama nazwa sugeruje picocom to minimalny program do emulacji
prymitywnego terminala "dumb". Jest bardzo podobny do minicoma, ale
jest "pico" zamiast "mini". Został zaprojektowany aby służyć za prosty
program do ręcznej konfiguracji i testów modemów oraz narzędzie do
rozwiązywania problemów. Służył też (dosyć dobrze) jako "okno
terminala" umożliwiajace administratorowi interweniowanie w skryptach
połączeń PPP (coś w rodzaju "otwórz okno terminala przed / po
dzwonieniu" z MS Windows). Może się okazać przydatny także przy innych
podobnych zadaniach. Jest idealny dla systemów wbudowanych, jako że ma
bardzo mały narzut pamięciowy (poniżej 20kB po zestripowaniu). Oprócz
bycia małym przydatnym narzędziem, picocom w swoich źródłach zawiera
prostą, łatwą w użyciu i obszernie udokumentowaną bibliotekę
zarządzania terminalem, mogącą służyć także innym projektom.
Biblioteka ta ukrywa wywołania termios(3) i udostępnia mniej złożony i
bezpieczniejszy (choć o nieco mniejszych możliwościach) interfejs.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

rm -rf picocom.8 picocom.8.html picocom.8.ps
%{__make} picocom.8 picocom.8.html picocom.8.ps

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
