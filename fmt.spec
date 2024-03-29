#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fmt
Version  : 8.1.1
Release  : 10
URL      : https://github.com/fmtlib/fmt/archive/8.1.1/fmt-8.1.1.tar.gz
Source0  : https://github.com/fmtlib/fmt/archive/8.1.1/fmt-8.1.1.tar.gz
Summary  : A modern formatting library
Group    : Development/Tools
License  : MIT Python-2.0
Requires: fmt-lib = %{version}-%{release}
Requires: fmt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : python3

%description
This directory contains build support files such as
* CMake modules
* Build scripts

%package dev
Summary: dev components for the fmt package.
Group: Development
Requires: fmt-lib = %{version}-%{release}
Provides: fmt-devel = %{version}-%{release}
Requires: fmt = %{version}-%{release}

%description dev
dev components for the fmt package.


%package lib
Summary: lib components for the fmt package.
Group: Libraries
Requires: fmt-license = %{version}-%{release}

%description lib
lib components for the fmt package.


%package license
Summary: license components for the fmt package.
Group: Default

%description license
license components for the fmt package.


%prep
%setup -q -n fmt-8.1.1
cd %{_builddir}/fmt-8.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641585346
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1641585346
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fmt
cp %{_builddir}/fmt-8.1.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/fmt/a6571b819c2fb290e2bb182e92a7a20d7d42318d
cp %{_builddir}/fmt-8.1.1/doc/python-license.txt %{buildroot}/usr/share/package-licenses/fmt/f19fa3302647d3061306ffb9ef072a777c166e0b
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/fmt/args.h
/usr/include/fmt/chrono.h
/usr/include/fmt/color.h
/usr/include/fmt/compile.h
/usr/include/fmt/core.h
/usr/include/fmt/format-inl.h
/usr/include/fmt/format.h
/usr/include/fmt/locale.h
/usr/include/fmt/os.h
/usr/include/fmt/ostream.h
/usr/include/fmt/printf.h
/usr/include/fmt/ranges.h
/usr/include/fmt/xchar.h
/usr/lib64/cmake/fmt/fmt-config-version.cmake
/usr/lib64/cmake/fmt/fmt-config.cmake
/usr/lib64/cmake/fmt/fmt-targets-relwithdebinfo.cmake
/usr/lib64/cmake/fmt/fmt-targets.cmake
/usr/lib64/libfmt.so
/usr/lib64/pkgconfig/fmt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfmt.so.8
/usr/lib64/libfmt.so.8.1.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fmt/a6571b819c2fb290e2bb182e92a7a20d7d42318d
/usr/share/package-licenses/fmt/f19fa3302647d3061306ffb9ef072a777c166e0b
