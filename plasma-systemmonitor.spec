%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-systemmonitor
Version: 5.21.0
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: System monitor for Plasma
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)

%description
System monitor for Plasma

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_bindir}/plasma-systemmonitor
%{_libdir}/qt5/qml/org/kde/ksysguard
%{_datadir}/applications/org.kde.plasma-systemmonitor.desktop
%{_datadir}/config.kcfg/systemmonitor.kcfg
%{_datadir}/knsrcfiles/plasma-systemmonitor.knsrc
%{_datadir}/ksysguard
%{_datadir}/plasma-systemmonitor
