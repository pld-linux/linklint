%include	/usr/lib/rpm/macros.perl
Summary:	Fast html link checker
Summary(pl):	Szybkie narzêdzie do sprawdzania odno¶ników HTML
Name:		linklint
Version:	2.3.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.linklint.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c1ae0860199da59ded28771d1fa7b800
URL:		http://www.linklint.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linklint is a Perl program that checks links on web sites.

%description -l pl
linklint jest perlowym programem który sprawdza odno¶niki na stronach
WWW.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install linklint-%{version} $RPM_BUILD_ROOT%{_bindir}/linklint

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
