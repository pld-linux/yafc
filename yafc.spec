# TODO:
#	- package bash completions
#
Summary:	Yafc is yet another FTP and SFTP client
Summary(pl.UTF-8):	Yafc to Jeszcze Jeden Klient FTP oraz SFTP
Name:		yafc
Version:	1.3.7
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://www.yafc-ftp.com/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	4b6e0d46ab7ab78956bbb106ae904820
Source1:	%{name}.desktop
URL:		http://www.yafc-ftp.com/
BuildRequires:	heimdal-devel
BuildRequires:	libbsd-devel
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

%description -l pl.UTF-8
Yafc to Jeszcze Jeden Klient FTP, podobny do ftp(1). Ma interaktywny
interfejs do protokołu FTP oraz SFTP.
#Obsługuje protokół SOCKS5.

%prep
%setup -q

%build
%configure
#	--with-socks5
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install samples/yafcrc $RPM_BUILD_ROOT%{_sysconfdir}/yafcrc
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc BUGS COPYRIGHT NEWS README.md THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yafcrc
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_infodir}/yafc.info*
