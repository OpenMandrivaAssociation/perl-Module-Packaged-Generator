%define upstream_name    Module-Packaged-Generator
%define upstream_version 1.111930

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Role to provide easy url fetching
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildRequires:	perl(Devel::Platform::Info::Linux)
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::HomeDir) >= 0.970.0
BuildRequires:	perl(File::HomeDir::PathClass)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long::Descriptive)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Log::Dispatchouli)
BuildRequires:	perl(Module::Build) >= 0.360.100
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::ClassAttribute)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::SemiAffordanceAccessor)
BuildRequires:	perl(MooseX::Singleton)
BuildRequires:	perl(Parse::CPAN::Packages::Fast)
BuildRequires:	perl(Term::ProgressBar::Quiet)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More) >= 0.880.0
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This module alows to fetch modules available as native Linux (or BSD)
distribution packages, and wraps them in a sqlite database. This allows
people to do analysis, draw CPANTS metrics from it or whatever.

Of course, running the utility shipped in this dist will only create the
database for the current distribution. But that's not our job to do crazy
manipulation with this data, we just provide the data :-)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/pkgcpan
%{_datadir}/man/man1/pkgcpan.1.*


%changelog
* Fri Jul 15 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.111.930-2mdv2011
+ Revision: 690048
- Fix version requires on perl-File-HomeDir

* Tue Jul 12 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.111.930-1
+ Revision: 689775
- Fix buildrequires
- New version
- import perl-Module-Packaged-Generator

