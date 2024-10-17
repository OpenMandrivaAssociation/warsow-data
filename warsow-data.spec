%define		debug_package	%nil

Name:		warsow-data
Version:	2.1.2
Release:	1
Summary:	Data files for Warsow
# See license.txt in the warsow rpm
License:	Warsow Content License
Group:		Games/Other
URL:		https://www.warsow.net/
#http://www.warsow.net:1337/~warsow/%{version}/
Source0:	warsow_21_unified.tar.gz
BuildRequires:	fdupes
BuildRequires:	dos2unix

Requires:	warsow = %{version}

%description
Data files (audio, maps, etc.) for Warsow.


%prep
%setup -q -n warsow_21

rm -rf libs/ warsow* wsw*

dos2unix docs/*.txt

%build

%install
mkdir -p %{buildroot}%{_gamesdatadir}/warsow/
cp -rf basewsw %{buildroot}%{_gamesdatadir}/warsow/

%files
%doc docs/*
%{_gamesdatadir}/warsow/
