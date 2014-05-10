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
./waf install --destdir=%{buildroot} -j1
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="X-Jack;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%files
%{_bindir}/Jc_Gui
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/Jc_Gui.desktop


