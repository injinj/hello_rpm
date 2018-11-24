Name:		hello_rpm
Version:	999.999
Release:	99999%{?dist}
Summary:	Hello world copr example

License:	BSD
URL:		https://github.com/injinj/hello_rpm
Source0:	%{name}-%{version}-99999.tar.gz
BuildRoot:	${_tmppath}
BuildRequires:  gcc-c++
Prefix:	        /usr

%description
A hello world rpm example

%prep
%setup -q

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0
%define _missing_build_ids_terminate_build 0
%define _include_gdb_index 1

%build
make build_dir=./usr %{?_smp_mflags} dist_bins

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/*

%changelog
* __DATE__ <hello_world@hello.world>
- Hello world
