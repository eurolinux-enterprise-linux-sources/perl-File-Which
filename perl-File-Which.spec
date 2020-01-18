Name:           perl-File-Which
Version:        1.09
Release:        12%{?dist}
Summary:        Portable implementation of the 'which' utility
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-Which/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/File-Which-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
File::Which is a portable implementation (in Perl) of 'which', and can
be used to get the absolute filename of an executable program
installed somewhere in your PATH, or just check for its existence. It
includes the command-line utility 'pwhich' which has the same function
as 'which'.

%prep
%setup -q -n File-Which-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
%if !%{defined perl_bootstrap}
make test
%endif

%files
%doc Changes README
%{_bindir}/pwhich
%{perl_vendorlib}/File/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.09-12
- Mass rebuild 2013-12-27

* Wed Oct 24 2012 Petr Šabata <contyk@redhat.com> - 1.09-11
- Specify all dependencies
- Modernize spec
- Drop command macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.09-9
- Perl 5.16 re-rebuild of bootstrapped packages

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.09-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.09-6
- Perl mass rebuild
- add perl_bootstrap macro

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.09-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.09-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.09-2
- rebuild against perl 5.10.1

* Mon Oct  5 2009 Stepan Kasal <skasal@redhat.com> - 1.09-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-4
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-3
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Dec 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-2
- find: fixed arguments order.

* Sun Dec 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-1
- First build.
