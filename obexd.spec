Summary:	D-Bus service for Obex Client access
Name:		obexd
Version:	0.48
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
# Source0-md5:	d03cf9bad2983243837f4f6d76ef14a6
URL:		http://www.bluez.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	libical-devel
Requires:	bluez
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
D-Bus service for Obex Client access

%prep
%setup -q

%build
%configure \
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
%attr(755,root,root) %{_libexecdir}/obexd
%{_datadir}/dbus-1/services/obex-client.service
%{_datadir}/dbus-1/services/obexd.service

