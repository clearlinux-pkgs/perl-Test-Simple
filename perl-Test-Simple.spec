#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v18
# autospec commit: f35655a
#
Name     : perl-Test-Simple
Version  : 1.302200
Release  : 121
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302200.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302200.tar.gz
Summary  : 'Basic utilities for writing tests.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Simple-license = %{version}-%{release}
Requires: perl-Test-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(JSON::MaybeXS)
BuildRequires : perl(Term::Table)
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
%setup -q -n Test-Simple-1.302200
cd %{_builddir}/Test-Simple-1.302200
pushd ..
cp -a Test-Simple-1.302200 buildavx2
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
cp %{_builddir}/Test-Simple-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Simple/b70b3b91dcf1142f43384b4363ee8507e397f11d || :
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
/usr/share/man/man3/Test2::AsyncSubtest.3
/usr/share/man/man3/Test2::AsyncSubtest::Event::Attach.3
/usr/share/man/man3/Test2::AsyncSubtest::Event::Detach.3
/usr/share/man/man3/Test2::AsyncSubtest::Hub.3
/usr/share/man/man3/Test2::Bundle.3
/usr/share/man/man3/Test2::Bundle::Extended.3
/usr/share/man/man3/Test2::Bundle::More.3
/usr/share/man/man3/Test2::Bundle::Simple.3
/usr/share/man/man3/Test2::Compare.3
/usr/share/man/man3/Test2::Compare::Array.3
/usr/share/man/man3/Test2::Compare::Bag.3
/usr/share/man/man3/Test2::Compare::Base.3
/usr/share/man/man3/Test2::Compare::Bool.3
/usr/share/man/man3/Test2::Compare::Custom.3
/usr/share/man/man3/Test2::Compare::DeepRef.3
/usr/share/man/man3/Test2::Compare::Delta.3
/usr/share/man/man3/Test2::Compare::Event.3
/usr/share/man/man3/Test2::Compare::EventMeta.3
/usr/share/man/man3/Test2::Compare::Float.3
/usr/share/man/man3/Test2::Compare::Hash.3
/usr/share/man/man3/Test2::Compare::Isa.3
/usr/share/man/man3/Test2::Compare::Meta.3
/usr/share/man/man3/Test2::Compare::Negatable.3
/usr/share/man/man3/Test2::Compare::Number.3
/usr/share/man/man3/Test2::Compare::Object.3
/usr/share/man/man3/Test2::Compare::OrderedSubset.3
/usr/share/man/man3/Test2::Compare::Pattern.3
/usr/share/man/man3/Test2::Compare::Ref.3
/usr/share/man/man3/Test2::Compare::Regex.3
/usr/share/man/man3/Test2::Compare::Scalar.3
/usr/share/man/man3/Test2::Compare::Set.3
/usr/share/man/man3/Test2::Compare::String.3
/usr/share/man/man3/Test2::Compare::Undef.3
/usr/share/man/man3/Test2::Compare::Wildcard.3
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
/usr/share/man/man3/Test2::Manual.3
/usr/share/man/man3/Test2::Manual::Anatomy.3
/usr/share/man/man3/Test2::Manual::Anatomy::API.3
/usr/share/man/man3/Test2::Manual::Anatomy::Context.3
/usr/share/man/man3/Test2::Manual::Anatomy::EndToEnd.3
/usr/share/man/man3/Test2::Manual::Anatomy::Event.3
/usr/share/man/man3/Test2::Manual::Anatomy::Hubs.3
/usr/share/man/man3/Test2::Manual::Anatomy::IPC.3
/usr/share/man/man3/Test2::Manual::Anatomy::Utilities.3
/usr/share/man/man3/Test2::Manual::Concurrency.3
/usr/share/man/man3/Test2::Manual::Contributing.3
/usr/share/man/man3/Test2::Manual::Testing.3
/usr/share/man/man3/Test2::Manual::Testing::Introduction.3
/usr/share/man/man3/Test2::Manual::Testing::Migrating.3
/usr/share/man/man3/Test2::Manual::Testing::Planning.3
/usr/share/man/man3/Test2::Manual::Testing::Todo.3
/usr/share/man/man3/Test2::Manual::Tooling.3
/usr/share/man/man3/Test2::Manual::Tooling::FirstTool.3
/usr/share/man/man3/Test2::Manual::Tooling::Formatter.3
/usr/share/man/man3/Test2::Manual::Tooling::Nesting.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::TestExit.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::TestingDone.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::ToolCompletes.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::ToolStarts.3
/usr/share/man/man3/Test2::Manual::Tooling::Subtest.3
/usr/share/man/man3/Test2::Manual::Tooling::TestBuilder.3
/usr/share/man/man3/Test2::Manual::Tooling::Testing.3
/usr/share/man/man3/Test2::Mock.3
/usr/share/man/man3/Test2::Plugin.3
/usr/share/man/man3/Test2::Plugin::BailOnFail.3
/usr/share/man/man3/Test2::Plugin::DieOnFail.3
/usr/share/man/man3/Test2::Plugin::ExitSummary.3
/usr/share/man/man3/Test2::Plugin::SRand.3
/usr/share/man/man3/Test2::Plugin::Times.3
/usr/share/man/man3/Test2::Plugin::UTF8.3
/usr/share/man/man3/Test2::Require.3
/usr/share/man/man3/Test2::Require::AuthorTesting.3
/usr/share/man/man3/Test2::Require::AutomatedTesting.3
/usr/share/man/man3/Test2::Require::EnvVar.3
/usr/share/man/man3/Test2::Require::ExtendedTesting.3
/usr/share/man/man3/Test2::Require::Fork.3
/usr/share/man/man3/Test2::Require::Module.3
/usr/share/man/man3/Test2::Require::NonInteractiveTesting.3
/usr/share/man/man3/Test2::Require::Perl.3
/usr/share/man/man3/Test2::Require::RealFork.3
/usr/share/man/man3/Test2::Require::ReleaseTesting.3
/usr/share/man/man3/Test2::Require::Threads.3
/usr/share/man/man3/Test2::Suite.3
/usr/share/man/man3/Test2::Todo.3
/usr/share/man/man3/Test2::Tools.3
/usr/share/man/man3/Test2::Tools::AsyncSubtest.3
/usr/share/man/man3/Test2::Tools::Basic.3
/usr/share/man/man3/Test2::Tools::Class.3
/usr/share/man/man3/Test2::Tools::ClassicCompare.3
/usr/share/man/man3/Test2::Tools::Compare.3
/usr/share/man/man3/Test2::Tools::Defer.3
/usr/share/man/man3/Test2::Tools::Encoding.3
/usr/share/man/man3/Test2::Tools::Event.3
/usr/share/man/man3/Test2::Tools::Exception.3
/usr/share/man/man3/Test2::Tools::Exports.3
/usr/share/man/man3/Test2::Tools::GenTemp.3
/usr/share/man/man3/Test2::Tools::Grab.3
/usr/share/man/man3/Test2::Tools::Mock.3
/usr/share/man/man3/Test2::Tools::Ref.3
/usr/share/man/man3/Test2::Tools::Refcount.3
/usr/share/man/man3/Test2::Tools::Spec.3
/usr/share/man/man3/Test2::Tools::Subtest.3
/usr/share/man/man3/Test2::Tools::Target.3
/usr/share/man/man3/Test2::Tools::Tester.3
/usr/share/man/man3/Test2::Tools::Tiny.3
/usr/share/man/man3/Test2::Tools::Warnings.3
/usr/share/man/man3/Test2::Transition.3
/usr/share/man/man3/Test2::Util.3
/usr/share/man/man3/Test2::Util::ExternalMeta.3
/usr/share/man/man3/Test2::Util::Facets2Legacy.3
/usr/share/man/man3/Test2::Util::Grabber.3
/usr/share/man/man3/Test2::Util::Guard.3
/usr/share/man/man3/Test2::Util::HashBase.3
/usr/share/man/man3/Test2::Util::Importer.3
/usr/share/man/man3/Test2::Util::Ref.3
/usr/share/man/man3/Test2::Util::Stash.3
/usr/share/man/man3/Test2::Util::Sub.3
/usr/share/man/man3/Test2::Util::Table.3
/usr/share/man/man3/Test2::Util::Table::LineBreak.3
/usr/share/man/man3/Test2::Util::Times.3
/usr/share/man/man3/Test2::Util::Trace.3
/usr/share/man/man3/Test2::V0.3
/usr/share/man/man3/Test2::Workflow.3
/usr/share/man/man3/Test2::Workflow::BlockBase.3
/usr/share/man/man3/Test2::Workflow::Build.3
/usr/share/man/man3/Test2::Workflow::Runner.3
/usr/share/man/man3/Test2::Workflow::Task.3
/usr/share/man/man3/Test2::Workflow::Task::Action.3
/usr/share/man/man3/Test2::Workflow::Task::Group.3
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
/usr/share/package-licenses/perl-Test-Simple/b70b3b91dcf1142f43384b4363ee8507e397f11d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
