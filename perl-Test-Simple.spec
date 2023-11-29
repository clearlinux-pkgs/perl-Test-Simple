#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: e661f3a
#
Name     : perl-Test-Simple
Version  : 1.302197
Release  : 114
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302197.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302197.tar.gz
Summary  : 'Basic utilities for writing tests.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Simple-license = %{version}-%{release}
Requires: perl-Test-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Test2 - Framework for writing test tools that all work together.
DESCRIPTION

%package dev
Summary: dev components for the perl-Test-Simple package.
Group: Development
Provides: perl-Test-Simple-devel = %{version}-%{release}
Requires: perl-Test-Simple = %{version}-%{release}

%description dev
dev components for the perl-Test-Simple package.


%package license
Summary: license components for the perl-Test-Simple package.
Group: Default

%description license
license components for the perl-Test-Simple package.


%package perl
Summary: perl components for the perl-Test-Simple package.
Group: Default
Requires: perl-Test-Simple = %{version}-%{release}

%description perl
perl components for the perl-Test-Simple package.


%prep
%setup -q -n Test-Simple-1.302197
cd %{_builddir}/Test-Simple-1.302197
pushd ..
cp -a Test-Simple-1.302197 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Simple
cp %{_builddir}/Test-Simple-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Simple/28e7ec7493915d0625a4d80dd3b2ad71b2ec9fdc || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test2.3
/usr/share/man/man3/Test2::API.3
/usr/share/man/man3/Test2::API::Breakage.3
/usr/share/man/man3/Test2::API::Context.3
/usr/share/man/man3/Test2::API::Instance.3
/usr/share/man/man3/Test2::API::InterceptResult.3
/usr/share/man/man3/Test2::API::InterceptResult::Event.3
/usr/share/man/man3/Test2::API::InterceptResult::Hub.3
/usr/share/man/man3/Test2::API::InterceptResult::Squasher.3
/usr/share/man/man3/Test2::API::Stack.3
/usr/share/man/man3/Test2::Event.3
/usr/share/man/man3/Test2::Event::Bail.3
/usr/share/man/man3/Test2::Event::Diag.3
/usr/share/man/man3/Test2::Event::Encoding.3
/usr/share/man/man3/Test2::Event::Exception.3
/usr/share/man/man3/Test2::Event::Fail.3
/usr/share/man/man3/Test2::Event::Generic.3
/usr/share/man/man3/Test2::Event::Note.3
/usr/share/man/man3/Test2::Event::Ok.3
/usr/share/man/man3/Test2::Event::Pass.3
/usr/share/man/man3/Test2::Event::Plan.3
/usr/share/man/man3/Test2::Event::Skip.3
/usr/share/man/man3/Test2::Event::Subtest.3
/usr/share/man/man3/Test2::Event::TAP::Version.3
/usr/share/man/man3/Test2::Event::V2.3
/usr/share/man/man3/Test2::Event::Waiting.3
/usr/share/man/man3/Test2::EventFacet.3
/usr/share/man/man3/Test2::EventFacet::About.3
/usr/share/man/man3/Test2::EventFacet::Amnesty.3
/usr/share/man/man3/Test2::EventFacet::Assert.3
/usr/share/man/man3/Test2::EventFacet::Control.3
/usr/share/man/man3/Test2::EventFacet::Error.3
/usr/share/man/man3/Test2::EventFacet::Hub.3
/usr/share/man/man3/Test2::EventFacet::Info.3
/usr/share/man/man3/Test2::EventFacet::Info::Table.3
/usr/share/man/man3/Test2::EventFacet::Meta.3
/usr/share/man/man3/Test2::EventFacet::Parent.3
/usr/share/man/man3/Test2::EventFacet::Plan.3
/usr/share/man/man3/Test2::EventFacet::Render.3
/usr/share/man/man3/Test2::EventFacet::Trace.3
/usr/share/man/man3/Test2::Formatter.3
/usr/share/man/man3/Test2::Formatter::TAP.3
/usr/share/man/man3/Test2::Hub.3
/usr/share/man/man3/Test2::Hub::Interceptor.3
/usr/share/man/man3/Test2::Hub::Interceptor::Terminator.3
/usr/share/man/man3/Test2::Hub::Subtest.3
/usr/share/man/man3/Test2::IPC.3
/usr/share/man/man3/Test2::IPC::Driver.3
/usr/share/man/man3/Test2::IPC::Driver::Files.3
/usr/share/man/man3/Test2::Tools::Tiny.3
/usr/share/man/man3/Test2::Transition.3
/usr/share/man/man3/Test2::Util.3
/usr/share/man/man3/Test2::Util::ExternalMeta.3
/usr/share/man/man3/Test2::Util::Facets2Legacy.3
/usr/share/man/man3/Test2::Util::HashBase.3
/usr/share/man/man3/Test2::Util::Trace.3
/usr/share/man/man3/Test::Builder.3
/usr/share/man/man3/Test::Builder::Formatter.3
/usr/share/man/man3/Test::Builder::IO::Scalar.3
/usr/share/man/man3/Test::Builder::Module.3
/usr/share/man/man3/Test::Builder::Tester.3
/usr/share/man/man3/Test::Builder::Tester::Color.3
/usr/share/man/man3/Test::Builder::TodoDiag.3
/usr/share/man/man3/Test::More.3
/usr/share/man/man3/Test::Simple.3
/usr/share/man/man3/Test::Tester.3
/usr/share/man/man3/Test::Tester::Capture.3
/usr/share/man/man3/Test::Tester::CaptureRunner.3
/usr/share/man/man3/Test::Tutorial.3
/usr/share/man/man3/Test::use::ok.3
/usr/share/man/man3/ok.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Simple/28e7ec7493915d0625a4d80dd3b2ad71b2ec9fdc

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
