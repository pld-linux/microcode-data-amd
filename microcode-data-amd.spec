%define		_dash_snap	2012-01-17
%define		_spec_snap	%(echo %{_dash_snap} | sed -e 's/-//g')
Summary:	Microcode definitions for AMD64 processors
Name:		microcode-data-amd
Version:	%{_spec_snap}
Release:	1
License:	AMD SOFTWARE LICENSE AGREEMENT
Group:		Base
# http://www.amd64.org/index.php?id=50&file=amd-ucode-2012-01-17.tar
Source0:	amd-ucode-%{_dash_snap}.tar
# Source0-md5:	c0eabb7e25e1f9045b7dd5ceabfddd09
URL:		http://www.amd64.org/support/microcode.html
Provides:	microcode-data
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
The microcode data file for Linux contains the latest microcode
definitions for AMD64 processor families 10h, 11h, 12h, 14h, and 15h.

%prep
%setup -q -n amd-ucode-%{_dash_snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
install microcode_amd.bin $RPM_BUILD_ROOT/lib/firmware
install microcode_amd_fam15h.bin $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) /lib/firmware/microcode*.bin
