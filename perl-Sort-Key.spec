#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sort-Key
Version  : 1.33
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Sort-Key-1.33.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Sort-Key-1.33.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsort-key-perl/libsort-key-perl_1.33-2.debian.tar.xz
Summary  : 'the fastest way to sort anything in Perl'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Sort-Key-lib = %{version}-%{release}
Requires: perl-Sort-Key-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Sort-Key
========
sort arrays by one or multiple calculated keys.
INSTALLATION
To install this module type the following:

%package dev
Summary: dev components for the perl-Sort-Key package.
Group: Development
Requires: perl-Sort-Key-lib = %{version}-%{release}
Provides: perl-Sort-Key-devel = %{version}-%{release}

%description dev
dev components for the perl-Sort-Key package.


%package lib
Summary: lib components for the perl-Sort-Key package.
Group: Libraries
Requires: perl-Sort-Key-license = %{version}-%{release}

%description lib
lib components for the perl-Sort-Key package.


%package license
Summary: license components for the perl-Sort-Key package.
Group: Default

%description license
license components for the perl-Sort-Key package.


%prep
%setup -q -n Sort-Key-1.33
cd ..
%setup -q -T -D -n Sort-Key-1.33 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Sort-Key-1.33/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sort-Key
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Sort-Key/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sort/Key.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sort/Key/Maker.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sort/Key/Multi.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sort/Key/Natural.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sort/Key/Register.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sort/Key/Types.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sort::Key.3
/usr/share/man/man3/Sort::Key::Maker.3
/usr/share/man/man3/Sort::Key::Multi.3
/usr/share/man/man3/Sort::Key::Natural.3
/usr/share/man/man3/Sort::Key::Register.3
/usr/share/man/man3/Sort::Key::Types.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Sort/Key/Key.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sort-Key/deblicense_copyright
