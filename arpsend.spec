%define name arpsend
%define version 1.2.2
%define release 3

Summary: Sends an Ethernet frame containing an IP ARP request or reply packet
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.net.princeton.edu/software/arpsend/%{name}-%{version}.tar.gz
License: BSD
Group:   System/Kernel and hardware
Url: https://www.net.princeton.edu/software/arpsend/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	net-devel >= 1.1.3

%description
arpsend sends an Ethernet frame containing an IP ARP request or
reply packet containing fields you specify.
This is a diagnostic tool intended for use by network administrators.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/arpsend
%{_mandir}/man8/arpsend*



%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 1.2.2-2mdv2011.0
+ Revision: 571831
- use configure2_5x

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdv2010.0
+ Revision: 382696
- rebuilt against libnet 1.1.3

* Thu Mar 05 2009 Erwan Velu <erwan@mandriva.org> 1.2.2-1mdv2009.1
+ Revision: 348878
- 1.2.2
- import arpsend


* Fri Mar 05 2008 Erwan Velu <erwan@seanodes.com> 1.2.1-1
- initial release
