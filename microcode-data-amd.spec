%define		dash_snap	2019-12-20
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
# Source1-md5:	3bdedb4466186a79c469f62120f6d7bb
Source2:	http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/amd-ucode/microcode_amd_fam16h.bin
# Source2-md5:	6a47a6393c52ddfc0b5b044efc076a77
Source3:	http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/amd-ucode/microcode_amd_fam17h.bin
# Source3-md5:	60f18b6d7fa3d1231b27cc339c173c8c
URL:		http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git
Provides:	microcode-data
ExclusiveArch:	i686 athlon x86_64 amd64 x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
The microcode data file for Linux contains the latest microcode
definitions for AMD64 processor families 10h, 11h, 12h, 14h, 15h, 16h
and 17h.

%description -l pl.UTF-8
Te pliki danych mikrokodu dla Linuksa zawierają najnowsze definicje
mikrokodu dla procesorów AMD64 z rodzin 10h, 11h, 12h, 14h, 15h, 16h
i 17h.

%prep
%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/amd-ucode

cp -p %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware/amd-ucode
cp -p %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/amd-ucode
cp -p %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/amd-ucode
cp -p %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/amd-ucode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /lib/firmware/amd-ucode
/lib/firmware/amd-ucode/microcode_amd.bin
/lib/firmware/amd-ucode/microcode_amd_fam15h.bin
/lib/firmware/amd-ucode/microcode_amd_fam16h.bin
/lib/firmware/amd-ucode/microcode_amd_fam17h.bin
