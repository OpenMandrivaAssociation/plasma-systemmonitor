%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma6-systemmonitor
Version: 6.1.1
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-systemmonitor/-/archive/%{gitbranch}/plasma-systemmonitor-%{gitbranchd}.tar.bz2#/plasma-systemmonitor-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/plasma-systemmonitor-%{version}.tar.xz
%endif
Summary: System monitor for Plasma
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Attica)
BuildRequires: cmake(KF6NewStuffCore)
BuildRequires: cmake(KF6KirigamiAddons)

%description
System monitor for Plasma.

%prep
%autosetup -p1 -n plasma-systemmonitor-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_bindir}/plasma-systemmonitor
%{_qtdir}/qml/org/kde/ksysguard
%{_datadir}/applications/org.kde.plasma-systemmonitor.desktop
%{_datadir}/config.kcfg/systemmonitor.kcfg
%{_datadir}/knsrcfiles/plasma-systemmonitor.knsrc
%{_datadir}/ksysguard
%{_datadir}/plasma-systemmonitor
%{_datadir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%{_datadir}/metainfo/org.kde.plasma-systemmonitor.metainfo.xml
%{_libdir}/libPlasmaSystemMonitor*.so*
%{_datadir}/kglobalaccel/org.kde.plasma-systemmonitor.desktop
