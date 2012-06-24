%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Dig
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - interface to the dig command
Summary(pl):	%{_pearname} - interfejs do polecenia dig
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	df50c33ae84e71074219740f5d3ca260
URL:		http://pear.php.net/package/Net_Dig/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Dig class should be a nice, friendly OO interface to the
dig command.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::Net_Dig to przyjemny i przyjazny, obiektowo zorientowany
interfejs do polecenia dig.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
