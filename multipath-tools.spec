#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v12
# autospec commit: fbcebd0
#
Name     : multipath-tools
Version  : 0.9.9
Release  : 21
URL      : https://github.com/opensvc/multipath-tools/archive/0.9.9/multipath-tools-0.9.9.tar.gz
Source0  : https://github.com/opensvc/multipath-tools/archive/0.9.9/multipath-tools-0.9.9.tar.gz
Summary  : Device mapper multipath management library
Group    : Development/Tools
License  : LGPL-2.0
Requires: multipath-tools-bin = %{version}-%{release}
Requires: multipath-tools-config = %{version}-%{release}
Requires: multipath-tools-lib = %{version}-%{release}
Requires: multipath-tools-license = %{version}-%{release}
Requires: multipath-tools-man = %{version}-%{release}
Requires: multipath-tools-services = %{version}-%{release}
BuildRequires : libaio-dev
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(liburcu)
BuildRequires : pkgconfig(ncurses)
BuildRequires : readline-dev
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A package that provides binaries to drive the Device Mapper multipathing
driver: multipath (device mapper target autoconfig), multipathd (multipath
daemon), mpathpersist (management of SCSI persistent reservations on dm
multipath devices), and kpartx (creates device maps from partition tables).

%package bin
Summary: bin components for the multipath-tools package.
Group: Binaries
Requires: multipath-tools-config = %{version}-%{release}
Requires: multipath-tools-license = %{version}-%{release}
Requires: multipath-tools-services = %{version}-%{release}

%description bin
bin components for the multipath-tools package.


%package config
Summary: config components for the multipath-tools package.
Group: Default

%description config
config components for the multipath-tools package.


%package dev
Summary: dev components for the multipath-tools package.
Group: Development
Requires: multipath-tools-lib = %{version}-%{release}
Requires: multipath-tools-bin = %{version}-%{release}
Provides: multipath-tools-devel = %{version}-%{release}
Requires: multipath-tools = %{version}-%{release}

%description dev
dev components for the multipath-tools package.


%package lib
Summary: lib components for the multipath-tools package.
Group: Libraries
Requires: multipath-tools-license = %{version}-%{release}

%description lib
lib components for the multipath-tools package.


%package license
Summary: license components for the multipath-tools package.
Group: Default

%description license
license components for the multipath-tools package.


%package man
Summary: man components for the multipath-tools package.
Group: Default

%description man
man components for the multipath-tools package.


%package services
Summary: services components for the multipath-tools package.
Group: Systemd services
Requires: systemd

%description services
services components for the multipath-tools package.


%prep
%setup -q -n multipath-tools-0.9.9
cd %{_builddir}/multipath-tools-0.9.9
pushd ..
cp -a multipath-tools-0.9.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718380906
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}  prefix=/usr SYSTEMDPATH=lib

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}  prefix=/usr SYSTEMDPATH=lib
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718380906
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/multipath-tools
cp %{_builddir}/multipath-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/multipath-tools/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3 prefix=/usr SYSTEMDPATH=lib
popd
GOAMD64=v2
%make_install prefix=/usr SYSTEMDPATH=lib
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/udev/kpartx_id

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kpartx
/V3/usr/bin/mpathpersist
/V3/usr/bin/multipath
/V3/usr/bin/multipathc
/V3/usr/bin/multipathd
/usr/bin/kpartx
/usr/bin/mpathpersist
/usr/bin/multipath
/usr/bin/multipathc
/usr/bin/multipathd

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/multipath.conf
/usr/lib/udev/rules.d/11-dm-mpath.rules
/usr/lib/udev/rules.d/11-dm-parts.rules
/usr/lib/udev/rules.d/56-multipath.rules
/usr/lib/udev/rules.d/66-kpartx.rules
/usr/lib/udev/rules.d/68-del-part-nodes.rules
/usr/lib/udev/rules.d/99-z-dm-mpath-late.rules

%files dev
%defattr(-,root,root,-)
/usr/include/libdmmp/libdmmp.h
/usr/include/mpath_cmd.h
/usr/include/mpath_persist.h
/usr/include/mpath_valid.h
/usr/lib64/libdmmp.so
/usr/lib64/libmpathcmd.so
/usr/lib64/libmpathpersist.so
/usr/lib64/libmpathutil.so
/usr/lib64/libmpathvalid.so
/usr/lib64/libmultipath.so
/usr/lib64/pkgconfig/libdmmp.pc
/usr/share/man/man3/dmmp_context_free.3
/usr/share/man/man3/dmmp_context_log_func_set.3
/usr/share/man/man3/dmmp_context_log_priority_get.3
/usr/share/man/man3/dmmp_context_log_priority_set.3
/usr/share/man/man3/dmmp_context_new.3
/usr/share/man/man3/dmmp_context_timeout_get.3
/usr/share/man/man3/dmmp_context_timeout_set.3
/usr/share/man/man3/dmmp_context_userdata_get.3
/usr/share/man/man3/dmmp_context_userdata_set.3
/usr/share/man/man3/dmmp_flush_mpath.3
/usr/share/man/man3/dmmp_last_error_msg.3
/usr/share/man/man3/dmmp_log_priority_str.3
/usr/share/man/man3/dmmp_mpath_array_free.3
/usr/share/man/man3/dmmp_mpath_array_get.3
/usr/share/man/man3/dmmp_mpath_kdev_name_get.3
/usr/share/man/man3/dmmp_mpath_name_get.3
/usr/share/man/man3/dmmp_mpath_wwid_get.3
/usr/share/man/man3/dmmp_path_array_get.3
/usr/share/man/man3/dmmp_path_blk_name_get.3
/usr/share/man/man3/dmmp_path_group_array_get.3
/usr/share/man/man3/dmmp_path_group_id_get.3
/usr/share/man/man3/dmmp_path_group_priority_get.3
/usr/share/man/man3/dmmp_path_group_selector_get.3
/usr/share/man/man3/dmmp_path_group_status_get.3
/usr/share/man/man3/dmmp_path_group_status_str.3
/usr/share/man/man3/dmmp_path_status_get.3
/usr/share/man/man3/dmmp_path_status_str.3
/usr/share/man/man3/dmmp_reconfig.3
/usr/share/man/man3/dmmp_strerror.3
/usr/share/man/man3/libdmmp.h.3
/usr/share/man/man3/mpath_persistent_reserve_in.3
/usr/share/man/man3/mpath_persistent_reserve_out.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libdmmp.so.0.2.0
/V3/usr/lib64/libmpathcmd.so.0
/V3/usr/lib64/libmpathpersist.so.0
/V3/usr/lib64/libmpathutil.so.0
/V3/usr/lib64/libmpathvalid.so.0
/V3/usr/lib64/libmultipath.so.0
/V3/usr/lib64/multipath/libcheckcciss_tur.so
/V3/usr/lib64/multipath/libcheckdirectio.so
/V3/usr/lib64/multipath/libcheckemc_clariion.so
/V3/usr/lib64/multipath/libcheckhp_sw.so
/V3/usr/lib64/multipath/libcheckrdac.so
/V3/usr/lib64/multipath/libcheckreadsector0.so
/V3/usr/lib64/multipath/libchecktur.so
/V3/usr/lib64/multipath/libforeign-nvme.so
/V3/usr/lib64/multipath/libprioalua.so
/V3/usr/lib64/multipath/libprioana.so
/V3/usr/lib64/multipath/libprioconst.so
/V3/usr/lib64/multipath/libpriodatacore.so
/V3/usr/lib64/multipath/libprioemc.so
/V3/usr/lib64/multipath/libpriohds.so
/V3/usr/lib64/multipath/libpriohp_sw.so
/V3/usr/lib64/multipath/libprioiet.so
/V3/usr/lib64/multipath/libprioontap.so
/V3/usr/lib64/multipath/libpriopath_latency.so
/V3/usr/lib64/multipath/libpriorandom.so
/V3/usr/lib64/multipath/libpriordac.so
/V3/usr/lib64/multipath/libpriosysfs.so
/V3/usr/lib64/multipath/libprioweightedpath.so
/usr/lib64/libdmmp.so.0.2.0
/usr/lib64/libmpathcmd.so.0
/usr/lib64/libmpathpersist.so.0
/usr/lib64/libmpathutil.so.0
/usr/lib64/libmpathvalid.so.0
/usr/lib64/libmultipath.so.0
/usr/lib64/multipath/libcheckcciss_tur.so
/usr/lib64/multipath/libcheckdirectio.so
/usr/lib64/multipath/libcheckemc_clariion.so
/usr/lib64/multipath/libcheckhp_sw.so
/usr/lib64/multipath/libcheckrdac.so
/usr/lib64/multipath/libcheckreadsector0.so
/usr/lib64/multipath/libchecktur.so
/usr/lib64/multipath/libforeign-nvme.so
/usr/lib64/multipath/libprioalua.so
/usr/lib64/multipath/libprioana.so
/usr/lib64/multipath/libprioconst.so
/usr/lib64/multipath/libpriodatacore.so
/usr/lib64/multipath/libprioemc.so
/usr/lib64/multipath/libpriohds.so
/usr/lib64/multipath/libpriohp_sw.so
/usr/lib64/multipath/libprioiet.so
/usr/lib64/multipath/libprioontap.so
/usr/lib64/multipath/libpriopath_latency.so
/usr/lib64/multipath/libpriorandom.so
/usr/lib64/multipath/libpriordac.so
/usr/lib64/multipath/libpriosysfs.so
/usr/lib64/multipath/libprioweightedpath.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/multipath-tools/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/multipath.conf.5
/usr/share/man/man8/kpartx.8
/usr/share/man/man8/mpathpersist.8
/usr/share/man/man8/multipath.8
/usr/share/man/man8/multipathc.8
/usr/share/man/man8/multipathd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/multipathd.service
/usr/lib/systemd/system/multipathd.socket
