%define name            jcgui
%define version         0.7
%define release         %mkrel 1

Name:           %{name}
Summary:        GUI for JConvolver, an audio convolution engine for JACK
Version:        %{version} 
Release:        %{release}

Source:         http://prdownloads.sourceforge.net/jcgui/%{name}-%{version}.tar.bz2
URL:            http://jcgui.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRequires:  python
BuildRequires:  gtk2-devel
BuildRequires:  libsndfile-devel, libjack-devel
Requires:       jconvolver

%description
JCGui is a graphical GTK user interface for JConvolver, an audio data
convolution engine for the Jack Audio Connection Kit. JConvolver is
used to create realistic acoustic environments.

%prep 
%setup -q

%build
./waf configure --prefix=%{_prefix} 
./waf

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot}
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
