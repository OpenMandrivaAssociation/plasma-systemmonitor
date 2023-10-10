%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-systemmonitor
Version: 5.27.8
Release: 2
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: System monitor for Plasma
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KSysGuard) < 5.27.50
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Package)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5NewStuffCore)
BuildRequires: cmake(KF5NewStuffQuick)
BuildRequires: ksystemstats
BuildRequires: qt5-qtquickcontrols2
Requires: ksystemstats
Requires: qt5-qtquickcontrols2

%description
System monitor for Plasma.

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
%{_datadir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%{_datadir}/metainfo/org.kde.plasma-systemmonitor.metainfo.xml
