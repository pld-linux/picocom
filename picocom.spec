# TODO:
# - build documentation, don't take the included ones
# - desktop and icon (maybe directly from minicom?)
Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (Дhnlich Telix)
Summary(es):	Paquete de comunicaciones modo texto a la Telix
Summary(fi):	Tietoliikenneohjelma, kuten Telix
Summary(fr):	Package de communication en mode terminal Ю la Telix
Summary(pl):	Program komunikacyjny (podobny do Telix-a)
Summary(pt_BR):	Pacote de comunicaГУes modo texto a la Telix
Summary(ru):	Коммуникационный пакет типа Telix для текстового режима
Summary(tr):	Telix benzeri, TTY kipi iletiЧim paketi
Summary(uk):	Комун╕кац╕йний пакет типу Telix для текстового режиму
Summary(zh_CN):	р╩╦Жнд╠╬╫ГцФ╣д╣Вйт╫Б╣ВфВ©ьжффВ╨мжу╤кдёдБфВ║ё
Name:		picocom
Version:	1.4
Release:	0.1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://efault.net/npat/hacks/picocom/dist/%{name}-%{version}.tar.gz
# Source0-md5:	08fcc5f6bb9e7676a2569386d5ea9f70
#Source1:	%{name}.desktop
#Source2:	%{name}.png
URL:		http://efault.net/npat/hacks/picocom/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As its name suggests, picocom is a minimal dumb-terminal emulation
program. It is, in principle, very much like minicom, only it's pico
instead of mini! It was designed to serve as a simple, manual, modem
configuration, testing, and debugging tool. It has also served (quite
well) as a low-tech "terminal-window" to allow operator intervention
in PPP connection scripts (something like the ms-windows "open
terminal window before / after dialing" feature). It could also prove
useful in many other similar tasks. It is ideal for embedded systems
since its memory footprint is minimal (less than 20K, when stripped).
Apart from being a handy little tool, picocom source distribution
includes a simple, easy to use, and thoroughly documented
terminal-management library, which could serve other projects as well.
This library hides the termios(3) calls, and provides a less complex
and safer (though certainly less feature-rich) interface.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install picocom pcxm pczm pcasc pcym $RPM_BUILD_ROOT%{_bindir}
install picocom.8 $RPM_BUILD_ROOT%{_mandir}/man8

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS NEWS README *.html *.ps
%attr(755,root,root) %{_bindir}/*
#%{_desktopdir}/*.desktop
#%{_pixmapsdir}/*
%{_mandir}/man8/*.8*
