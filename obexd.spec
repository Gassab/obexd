Summary:	D-Bus service for Obex Client access
Name:		obexd
Version:	0.46
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
# Source0-md5:	54fa544e208830fecce8ef6f3c190cb3
URL:		http://www.bluez.org/
BuildRequires:	bluez4-devel
BuildRequires:	dbus-devel
BuildRequires:	libical-devel
Requires:	bluez4
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
D-Bus service for Obex Client access

%prep
%setup -q

%build
%configure \
	--disable-server	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/obex-client
%{_datadir}/dbus-1/services/obex-client.service

