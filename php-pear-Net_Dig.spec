%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Dig
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - interface to the dig command
Summary(pl):	%{_class}_%{_subclass} - interfejs do polecenia dig
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Dig class should be a nice, friendly OO interface to the
dig command.

%description -l pl
Klasa PEAR::Net_Dig to przyjemny i przyjazny, obiektowo zorientowany
interfejs do polecenia dig.

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
