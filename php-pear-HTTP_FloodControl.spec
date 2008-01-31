%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	FloodControl
%define		_status		alpha
%define		_pearname	HTTP_FloodControl
Summary:	%{_pearname} - detect and protect from attempts to flood a site
Summary(pl.UTF-8):	%{_pearname} - detekcja i ochrona przed atakami typu flood
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	848fc5590d607b12f480faaf84fbf7c5
URL:		http://pear.php.net/package/HTTP_FloodControl/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(DB.*)'  'pear(MDB.*)'  'pear(MDB2.*)'

%description
The HTTP_FloodControl package can be used to detect and protect a Web
site from attempts to flood it with too many requests. It also allows
to protect the site from automatic downloading many pages or files
from the same IP address, session ID or other unique identifier.

The detection of flood is determine according to a set of parameters
indicating the maximal allowed number of requests for the certain time
interval. It is possible to set several parameters at once in order to
perform more effective protection.

The package uses various storage containers (regular files, DB, MDB,
MDB2) to handle counter logs.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa HTTP_FloodControl może być użytka do wykrycia i ochrony strony
Web przed próbami przepełnienia ich zbyt dużą ilością zapytań. Pozwala
także na ochronę serwisu przed automatycznym sciąganiem wielu stron
przez klienta identyfikowanego na podstawie adresu IP, identyfikatora
sesji bądź innego unikalnego identyfikatora.

Flood wykrywany jest na podstawie zestawu parametrów określających
maksymalną dozwoloną liczbę zapytań w zadanym przedziale czasowym.
Możliwe jest określenie wielu parametrów jednocześnie w celu
zapewnienia skutecznej ochrony.

Pakiet ten może skorzystać z różnych kontenerów danych (pliki, DB,
MDB, MDB2) w celu przechowywania informacji o licznach logów.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/HTTP
%pear_package_install
mv -f $RPM_BUILD_ROOT%{php_pear_dir}/{Flood*,HTTP}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTTP/FloodControl/
%{php_pear_dir}/HTTP/FloodControl.php
