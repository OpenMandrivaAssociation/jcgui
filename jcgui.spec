Name:           jcgui
Summary:        GUI for JConvolver, an audio convolution engine for JACK
Version:        0.8
Release:        3

Source:         http://prdownloads.sourceforge.net/jcgui/%{name}-%{version}.tar.bz2
URL:            http://jcgui.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRequires:  python
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(jack)
BuildRequires:  libzita-resampler-devel
BuildRequires:  desktop-file-utils
Requires:       jconvolver

%description
JCGui is a graphical GTK user interface for JConvolver, an audio data
convolution engine for the Jack Audio Connection Kit. JConvolver is
used to create realistic acoustic environments.

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix} --cxxflags="%{optflags}"
./waf -j1

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot} -j1
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="X-Jack;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/Jc_Gui
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/Jc_Gui.desktop


%changelog
* Sat Dec 24 2011 Frank Kober <emuse@mandriva.org> 0.7-4
+ Revision: 745029
- overwrite default cxxflags with mdv optflags
- rebuild to link against newer libpng

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdv2011.0
+ Revision: 612439
- the mass rebuild of 2010.1 packages

* Tue Mar 02 2010 Frank Kober <emuse@mandriva.org> 0.7-1mdv2010.1
+ Revision: 513687
- import jcgui


