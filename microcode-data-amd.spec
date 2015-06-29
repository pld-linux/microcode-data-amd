%define		dash_snap	2013-07-10
%define		spec_snap	%(echo %{dash_snap} | sed -e 's/-//g')
Summary:	Microcode definitions for AMD64 processors
Summary(pl.UTF-8):	Definicje mikrokodu dla procesorów AMD64
Name:		microcode-data-amd
Version:	%{spec_snap}
Release:	1
License:	AMD SOFTWARE LICENSE AGREEMENT
Group:		Base
Source0:	http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/amd-ucode/microcode_amd.bin
# Source0-md5:	55ae79b82cbfddcf7142058be3c9ec2d
Source1:	http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/amd-ucode/microcode_amd_fam15h.bin
# Source1-md5:	122ac7e56442c2b7c28eb26978b2d57c
URL:		http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git
Provides:	microcode-data
ExclusiveArch:	i686 %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
The microcode data file for Linux contains the latest microcode
definitions for AMD64 processor families 10h, 11h, 12h, 14h, and 15h.

%description -l pl.UTF-8
Te pliki danych mikrokodu dla Linuksa zawierają najnowsze definicje
mikrokodu dla procesorów AMD64 z rodzin 10h, 11h, 12h, 14h i 15h.

%prep
%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/amd-ucode
install %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware/amd-ucode
install %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/amd-ucode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /lib/firmware/amd-ucode
%attr(644,root,root) /lib/firmware/amd-ucode/microcode_amd.bin
%attr(644,root,root) /lib/firmware/amd-ucode/microcode_amd_fam15h.bin
