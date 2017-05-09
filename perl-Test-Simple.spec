#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Simple
Version  : 1.302085
Release  : 28
URL      : http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Test-Simple-1.302085.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Test-Simple-1.302085.tar.gz
Summary  : 'Basic utilities for writing tests.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Simple-doc

%description
NAME
Test2 - Framework for writing test tools that all work together.
DESCRIPTION

%package doc
Summary: doc components for the perl-Test-Simple package.
Group: Documentation

%description doc
doc components for the perl-Test-Simple package.


%prep
%setup -q -n Test-Simple-1.302085

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/Test/Builder.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Builder/Formatter.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Builder/IO/Scalar.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Builder/Module.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Builder/Tester.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Builder/Tester/Color.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Builder/TodoDiag.pm
/usr/lib/perl5/site_perl/5.24.0/Test/More.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Simple.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Tester.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Tester/Capture.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Tester/CaptureRunner.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Tester/Delegate.pm
/usr/lib/perl5/site_perl/5.24.0/Test/Tutorial.pod
/usr/lib/perl5/site_perl/5.24.0/Test/use/ok.pm
/usr/lib/perl5/site_perl/5.24.0/Test2.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/API.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/API/Breakage.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/API/Context.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/API/Instance.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/API/Stack.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Bail.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Diag.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Encoding.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Exception.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Generic.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Note.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Ok.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Plan.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Skip.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Subtest.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/TAP/Version.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Event/Waiting.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Formatter.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Formatter/TAP.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Hub.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Hub/Interceptor.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Hub/Interceptor/Terminator.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Hub/Subtest.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/IPC.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/IPC/Driver.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/IPC/Driver/Files.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Tools/Tiny.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Transition.pod
/usr/lib/perl5/site_perl/5.24.0/Test2/Util.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Util/ExternalMeta.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Util/HashBase.pm
/usr/lib/perl5/site_perl/5.24.0/Test2/Util/Trace.pm
/usr/lib/perl5/site_perl/5.24.0/ok.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
