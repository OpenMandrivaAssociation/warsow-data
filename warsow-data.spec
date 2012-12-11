Name:		warsow-data
Version:	1.02
Release:	%mkrel 2
Summary:	Data files for Warsow
# See license.txt in the warsow rpm
License:	Warsow Content License
Group:		Games/Other
URL:		http://www.warsow.net/
#http://www.warsow.net:1337/~warsow/%{version}/
Source0:	warsow_%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	fdupes
Requires:	warsow = %{version}

%description
Data files (audio, maps, etc.) for Warsow.

%prep
%setup -q -n warsow_%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/warsow/
cp -ap basewsw %{buildroot}/%{_datadir}/warsow/
fdupes %{buildroot}

%files
%doc docs/*
%{_datadir}/warsow/
