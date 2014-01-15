Summary:	wxWidgets interface for maxima
Summary(pl.UTF-8):	Interfejs do maximy używający wxWidgets
Name:		wxMaxima
Version:	12.01.0
Release:	3
License:	GPL
Group:		Applications/Math
Source0:	http://downloads.sourceforge.net/wxmaxima/%{name}-%{version}.tar.gz
# Source0-md5:	ef71ba8339fcdd7b715619af51bfa65e
Patch0:		%{name}-pixmap.patch
Patch1:		%{name}-docdir.patch
URL:		http://wxmaxima.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	wxWidgets-devel
Requires:	maxima >= 1:5.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxMaxima is a wxWidgets interface for the computer algebra system
Maxima.

%description -l pl.UTF-8
wxMaxima jest bazującym na wxWidgets interfejsem dla systemu algebry
komputerowej Maxima.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{configure}\
	--with-wx-config=%{_bindir}/wx-gtk2-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -e "s@Application;Utility;X-Red-Hat-Base;X-Red-Hat-Base-Only;@Science;Math;@g" wxmaxima.desktop \
	> $RPM_BUILD_ROOT%{_desktopdir}/wxmaxima.desktop

ln -s %{_pixmapsdir}/wxmaxima.png $RPM_BUILD_ROOT%{_datadir}/wxMaxima

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/wxmaxima
%{_datadir}/wxMaxima
%{_pixmapsdir}/wxmaxima.png
%{_desktopdir}/wxmaxima.desktop
