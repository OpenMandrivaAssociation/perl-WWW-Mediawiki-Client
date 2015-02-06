%define upstream_name    WWW-Mediawiki-Client
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Simple cvs-like interface for Mediawiki driven WikiWiki websites
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(VCS::Lite)
BuildRequires:	perl(XML::LibXML)
BuildArch:	noarch

%description
WWW::Mediawiki::Client provides a very simple cvs-like interface for
Mediawiki driven WikiWiki websites, such as http://www.wikitravel.org or
http://www.wikipedia.org.  The interface mimics the two most basic cvs
commands: update and commit with similarly named methods.  Each of these has a
shorter alias, as in cvs.  Verbosity is controled through an output_level
accessor method.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
make test

%install
%makeinstall_std

%files 
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/WWW


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.0
+ Revision: 401914
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.31-4mdv2009.0
+ Revision: 242157
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-2mdv2008.0
+ Revision: 87076
- rebuild


* Fri Aug 04 2006 guillomovitch
+ 2006-08-04 13:52:07 (51750)
- ooops

* Fri Aug 04 2006 guillomovitch
+ 2006-08-04 13:44:32 (51748)
- New version
- spec cleanup
- drop patch, seems uneeded now
- clean buildroot before install

* Thu Aug 03 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 15:05:32 (43249)
- import perl-WWW-Mediawiki-Client-0.28-1mdk

* Tue May 16 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.28-1mdk
- 0.28 
- Fix Source URL
- Add  patch1 see http://wikitravel.org/en/User_talk:Mark/WWW-Mediawiki-Client#Extra_Linefeeds
	Thank Brouard Nicolas for his big help

* Thu Dec 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.27-3mdk
- Fix BuildRequires

* Sat Nov 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.27-2mdk
- Fix BuildRequires

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.27-1mdk
- 0.27

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.25-3mdk
- fix url

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.25-2mdk
- Fix BuildRequires

* Thu Apr 28 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.25-1mdk
- initial build

