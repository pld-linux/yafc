Name:		yafc
Version:	0.6.6
Release:	1
Summary:	Yafc is yet another ftp client
Summary(pl):	Yafc to Jeszcze Jeden Klient Ftp
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://mayer.physto.se/pub/yafc/%{name}-%{version}.tar.gz
URL:		http://www.stacken.kth.se/~mhe/yafc
BuildRequires:	readline-devel
BuildRequires:	socks5-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yafc is yet another ftp client, similar to ftp(1). It is an
interactive interface to the FTP protocol. It has SOCKS5 protocol
support.

%description -l pl
Yafc to Jeszcze Jeden Klient Ftp, podobny do ftp(1) interaktywny
interfejs do protoko³u FTP. Zawiera wsparcie dla protoko³u SOCKS5.

%prep
%setup -q

%build
autoconf
%configure --with-socks5
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install yafcrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/yafcrc

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/yafcrc
%doc *.gz
