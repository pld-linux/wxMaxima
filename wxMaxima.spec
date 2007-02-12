Summary:	wxWidgets interface for maxima
Summary(pl.UTF-8):	Interfejs do maximy używający wxWidgets
Name:		wxMaxima
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/wxmaxima/%{name}-%{version}.tar.gz
# Source0-md5:	005f5bffe74caa987f66af2084d9df45
URL:		http://wxmaxima.sourceforge.net/
BuildRequires:	libxml2-devel
BuildRequires:	wxGTK2-devel
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

%build
%{configure}\
	--with-wx-config=/usr/bin/wx-gtk2-ansi-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -D wxmaxima.desktop $RPM_BUILD_ROOT%{_desktopdir}/wxmaxima.desktop
sed -e "s@Application;Utility;X-Red-Hat-Base;X-Red-Hat-Base-Only;@Science;Math;@g" -i $RPM_BUILD_ROOT%{_desktopdir}/wxmaxima.desktop

install -D maxima-new.png $RPM_BUILD_ROOT%{_pixmapsdir}/maxima-new.png
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/wxmaxima
%{_datadir}/wxMaxima
%{_pixmapsdir}/maxima-new.png
%{_desktopdir}/wxmaxima.desktop
