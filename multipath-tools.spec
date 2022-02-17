#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : multipath-tools
Version  : 0.8.8
Release  : 14
URL      : https://github.com/opensvc/multipath-tools/archive/0.8.8/multipath-tools-0.8.8.tar.gz
Source0  : https://github.com/opensvc/multipath-tools/archive/0.8.8/multipath-tools-0.8.8.tar.gz
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
Patch1: 0001-Update-Makefile.inc-move-all-content-under-usr.patch

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

%description services
services components for the multipath-tools package.


%prep
%setup -q -n multipath-tools-0.8.8
cd %{_builddir}/multipath-tools-0.8.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645057904
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1645057904
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/multipath-tools
cp %{_builddir}/multipath-tools-0.8.8/COPYING %{buildroot}/usr/share/package-licenses/multipath-tools/ba8966e2473a9969bdcab3dc82274c817cfd98a1
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/udev/kpartx_id

%files bin
%defattr(-,root,root,-)
/usr/bin/kpartx
/usr/bin/mpathpersist
/usr/bin/multipath
/usr/bin/multipathd

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/11-dm-mpath.rules
/usr/lib/udev/rules.d/11-dm-parts.rules
/usr/lib/udev/rules.d/56-multipath.rules
/usr/lib/udev/rules.d/66-kpartx.rules
/usr/lib/udev/rules.d/68-del-part-nodes.rules

%files dev
%defattr(-,root,root,-)
/usr/include/libdmmp/libdmmp.h
/usr/include/mpath_cmd.h
/usr/include/mpath_persist.h
/usr/include/mpath_valid.h
/usr/lib64/libdmmp.so
/usr/lib64/libmpathcmd.so
/usr/lib64/libmpathpersist.so
/usr/lib64/libmpathvalid.so
/usr/lib64/libmultipath.so
/usr/lib64/pkgconfig/libdmmp.pc
/usr/share/man/man3/dmmp_context_free.3.gz
/usr/share/man/man3/dmmp_context_log_func_set.3.gz
/usr/share/man/man3/dmmp_context_log_priority_get.3.gz
/usr/share/man/man3/dmmp_context_log_priority_set.3.gz
/usr/share/man/man3/dmmp_context_new.3.gz
/usr/share/man/man3/dmmp_context_timeout_get.3.gz
/usr/share/man/man3/dmmp_context_timeout_set.3.gz
/usr/share/man/man3/dmmp_context_userdata_get.3.gz
/usr/share/man/man3/dmmp_context_userdata_set.3.gz
/usr/share/man/man3/dmmp_flush_mpath.3.gz
/usr/share/man/man3/dmmp_last_error_msg.3.gz
/usr/share/man/man3/dmmp_log_priority_str.3.gz
/usr/share/man/man3/dmmp_mpath_array_free.3.gz
/usr/share/man/man3/dmmp_mpath_array_get.3.gz
/usr/share/man/man3/dmmp_mpath_kdev_name_get.3.gz
/usr/share/man/man3/dmmp_mpath_name_get.3.gz
/usr/share/man/man3/dmmp_mpath_wwid_get.3.gz
/usr/share/man/man3/dmmp_path_array_get.3.gz
/usr/share/man/man3/dmmp_path_blk_name_get.3.gz
/usr/share/man/man3/dmmp_path_group_array_get.3.gz
/usr/share/man/man3/dmmp_path_group_id_get.3.gz
/usr/share/man/man3/dmmp_path_group_priority_get.3.gz
/usr/share/man/man3/dmmp_path_group_selector_get.3.gz
/usr/share/man/man3/dmmp_path_group_status_get.3.gz
/usr/share/man/man3/dmmp_path_group_status_str.3.gz
/usr/share/man/man3/dmmp_path_status_get.3.gz
/usr/share/man/man3/dmmp_path_status_str.3.gz
/usr/share/man/man3/dmmp_reconfig.3.gz
/usr/share/man/man3/dmmp_strerror.3.gz
/usr/share/man/man3/libdmmp.h.3.gz
/usr/share/man/man3/mpath_persistent_reserve_in.3.gz
/usr/share/man/man3/mpath_persistent_reserve_out.3.gz

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdmmp.so.0.2.0
/usr/lib64/libmpathcmd.so.0
/usr/lib64/libmpathpersist.so.0
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
/usr/share/man/man5/multipath.conf.5.gz
/usr/share/man/man8/kpartx.8.gz
/usr/share/man/man8/mpathpersist.8.gz
/usr/share/man/man8/multipath.8.gz
/usr/share/man/man8/multipathd.8.gz

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/multipathd.service
/usr/lib/systemd/system/multipathd.socket
