%include	/usr/lib/rpm/macros.perl
Summary:	fast html link checker
Summary(pl):	szybkie narzêdzie do sprawdzania odno¶ników HTML
Name:		linklint
Version:	2.3.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.linklint.org/download/%{name}-%{version}.tar.gz
URL:		http://www.linklint.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linklint is a Perl program that checks links on web sites.

%description -l pl
Linklint jest perlowym programem który sprawdza odno¶niki na stronach WWW.

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
