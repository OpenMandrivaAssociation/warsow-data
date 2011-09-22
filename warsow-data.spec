Name:		warsow-data
Version:	0.61
Release:	%mkrel 1
Summary:	Data files for Warsow
# See license.txt in the warsow rpm
License:	Warsow Content License
Group:		Games/Other 
URL:		http://www.warsow.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Source0:	warsow_%{version}_unified.zip
BuildArch:	noarch
BuildRequires:	fdupes
Requires:	warsow >= 0.61

%description
Data files (audio, maps, etc.) for Warsow.

%prep
%setup -q -n warsow_%{version}_unified

%build

%install
mkdir -p %{buildroot}/%{_datadir}/warsow/
cp -ap basewsw %{buildroot}/%{_datadir}/warsow/
fdupes $RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*
%{_datadir}/warsow/
