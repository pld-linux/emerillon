Summary:	Emerillon is a map viewer featuring Open Street Maps
Name:		emerillon
Version:	0.1.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.gnome.org/sources/emerillon/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	39c344961105019b45dc8b49e8d70cbe
URL:		http://projects.gnome.org/emerillon/
BuildRequires:	clutter-devel
BuildRequires:	geoclue-devel >= 0.11.1
BuildRequires:	glib-devel >= 2.12.0
BuildRequires:	gtk+2-devel >= 2.12.0
BuildRequires:	libchamplain-devel >= 0.4
BuildRequires:	libethos-devel >= 0.2
BuildRequires:	librest-devel >= 0.6.1
Requires:	clutter
Requires:	geoclue >= 0.11.1
Requires:	glib >= 2.12.0
Requires:	gtk+2 >= 2.12.0
Requires:	libchamplain >= 0.4
Requires:	libethos >= 0.2
Requires:	librest >= 0.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emerillon is a map viewer. Aiming at simple user interface, Emerillon
is a powerful, extensible application. It is pronounced
Ey-may-ree-yon.

It features OpenStreetMap based maps: the street map, the cycling map
and the transportation map. Use it to:

- Browse maps,
- Search the map for places,
- Placemark places for later quick access.

Emerillon is named after the Émérillon, one of the three boats that
visited New France under Jacques Cartier's command in 1535. Émérillon
is also French for Merlin Falcons.

%package devel
Summary:	Header files for emerillon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for emerillon

%prep
%setup -q

# If gtk+2 >= 2.20 patch for new names of depricated methods.
%define GTKVER %(rpm -q --qf %{version} gtk+2)
%if "GTKVER" >= "2.20.0"
%{__sed} -i -e 's/GTK_WIDGET_VISIBLE/gtk_widget_get_visible/g' %{name}/*.c
%{__sed} -i -e 's/GTK_WIDGET_NO_WINDOW/gtk_widget_get_has_window/g' %{name}/*.c
%endif

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugins
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-ui.xml
%{_desktopdir}/%{name}.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-0.1/%{name}
%{_pkgconfigdir}/*.pc
