Name:           clicfs
BuildRequires:  cmake e2fsprogs-devel fuse-devel gcc-c++ openssl-devel xz
Requires:       fuse
Summary:        Compressed Loop Image Container
Version:        1.4.0
Release:        0
License:        GPLv2
Group:          System/Base
Source:         clicfs.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Clic FS is a FUSE file system to mount a Compressed Loop Image
Container. It has several features that make it a good choice for live
systems. It will compress a Loop Image and export it as read write,
creating a copy on write behaviour.


%prep
%setup -c %name 

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 .

%install
#make DESTDIR=%{buildroot} install
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE
%{_bindir}/*clicfs
%_mandir/man1/*

