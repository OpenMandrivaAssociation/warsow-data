%define		debug_package	%nil

Name:		warsow-data
Version:	2.1.2
Release:	1
Summary:	Data files for Warsow
# See license.txt in the warsow rpm
License:	Warsow Content License
Group:		Games/Other
URL:		http://www.warsow.net/
#http://www.warsow.net:1337/~warsow/%{version}/
Source0:	warsow_21_unified.tar.gz
BuildRequires:	fdupes
Requires:	warsow = %{version}

%description
Data files (audio, maps, etc.) for Warsow.


%setup -qn warsow_21
find . -type f -perm 0600 -exec chmod 644 {} \;
find . -type d -perm 0700 -exec chmod 755 {} \;

%build

%install
mkdir -p %{buildroot}%{_libdir}/games/warsow/
cp -ap basewsw %{buildroot}%{_libdir}/games/warsow/
fdupes %{buildroot}

%files
%doc docs/*
%{_libdir}/games/warsow/basewsw
