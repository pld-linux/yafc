Summary:	Yafc is yet another ftp and sftp client
Summary(pl):	Yafc to Jeszcze Jeden Klient Ftp oraz sftp
Name:		yafc
Version:	0.7.10
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://yafc.sourceforge.net/
Patch0:		%{name}-LIBOBJS.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-tinfo.patch
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
#BuildRequires:	socks5-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yafc is yet another ftp client, similar to ftp(1). It is an
interactive interface to the FTP protocol and SFTP protocol.
#It has SOCKS5 protocol support.

%description -l pl
Yafc to Jeszcze Jeden Klient Ftp, podobny do ftp(1). Ma interaktywny
interfejs do protoko³u FTP oraz SFTP.
#Obs³uguje protokó³ SOCKS5.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 
#	--with-socks5
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install yafcrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/yafcrc

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README doc/
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/yafcrc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
