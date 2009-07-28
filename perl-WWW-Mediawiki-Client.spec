%define upstream_name    WWW-Mediawiki-Client
%define upstream_version 0.31

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Simple cvs-like interface for Mediawiki driven WikiWiki websites
License:        Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif
BuildRequires:  perl-Test-Differences
BuildRequires:  perl-libwww-perl
BuildRequires:  perl-VCS-Lite
BuildRequires:  perl-Exception-Class
BuildRequires:  perl-XML-LibXML 
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make 

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/WWW
