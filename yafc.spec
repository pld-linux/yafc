Summary:	Yafc is yet another FTP and SFTP client
Summary(pl):	Yafc to Jeszcze Jeden Klient FTP oraz SFTP
Name:		yafc
Version:	1.1.1
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/yafc/%{name}-%{version}.tar.bz2
# Source0-md5:	832d074183a36ee15b47553ed5962fce
Source1:	%{name}.desktop
URL:		http://yafc.sourceforge.net/
Patch0:		%{name}-errno.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-tinfo.patch
Patch3:		%{name}-home_etc.patch
Patch4:		%{name}-gssapi.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	heimdal-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
#BuildRequires:	socks5-devel
BuildRequires:	texinfo
Requires:	openssh-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 

%description
Yafc is yet another FTP client, similar to ftp(1). It is an
interactive interface to the FTP protocol and SFTP protocol.
#It has SOCKS5 protocol support.

%description -l pl
Yafc to Jeszcze Jeden Klient FTP, podobny do ftp(1). Ma interaktywny
interfejs do protoko³u FTP oraz SFTP.
#Obs³uguje protokó³ SOCKS5.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I cf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
#	--with-socks5
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install yafcrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/yafcrc
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc BUGS COPYRIGHT NEWS README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yafcrc
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_mandir}/man1/*
%{_infodir}/yafc.info*
