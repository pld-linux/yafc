Name:		yafc
Version:	0.7.10
Release:	1
Summary:	Yafc is yet another ftp and sftp client.
Summary(pl):	Yafc to Jeszcze Jeden Klient Ftp oraz sftp.
License:	GPL
Group:		Applications/Networking
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://yafc.sourceforge.net/
Patch0:		%{name}-LIBOBJS.patch
BuildRequires:	readline-devel
#BuildRequires:	socks5-devel
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yafc is yet another ftp client, similar to ftp(1). It is an
interactive interface to the FTP protocol and SFTP protocol. 
#It has SOCKS5 protocolsupport.

%description -l pl
Yafc to Jeszcze Jeden Klient Ftp, podobny do ftp(1) interaktywny
interfejs do protoko³u FTP oraz SFTP. 
#Zawiera wsparcie dla protoko³u SOCKS5.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 
#--with-socks5
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install yafcrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/yafcrc

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
%doc README doc/
