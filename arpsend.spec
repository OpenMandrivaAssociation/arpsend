%define name arpsend
%define version 1.2.1
%define release %mkrel 1

Summary: Blktool is a multi-purpose tool to manage common block concepts
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.net.princeton.edu/software/arpsend/%{name}-%{version}.tar.gz
License: BSD
Group:   System/Kernel and hardware
Url: http://www.net.princeton.edu/software/arpsend/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libnet1.1.2-devel

%description
arpsend sends an Ethernet frame containing an IP ARP request or
reply packet containing fields you specify.
This is a diagnostic tool intended for use by network administrators.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/arpsend
%{_mandir}/man8/arpsend*

