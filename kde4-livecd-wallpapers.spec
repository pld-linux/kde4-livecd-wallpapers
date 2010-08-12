
Summary:	PLD-LiveCD KDE4 wallpapers
Summary(pl.UTF-8):	Tapety do PLD-LiveCD z KDE4
Name:		kde4-livecd-wallpapers
Version:	0
Release:	2
License:	LGPLv3
Group:		X11/Libraries
Source0:	%{name}.tar.gz
# Source0-md5:	e59efba0963527cdbdb4f1ea38d69106
URL:		http://livecd.pld-linux.pl
BuildRequires:	rpmbuild(macros) >= 1.293
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD-LiveCD KDE4 wallpapers.

%description -l pl.UTF-8
Tapety do PLD-LiveCD z KDE4.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
cp -ar livecd $RPM_BUILD_ROOT%{_datadir}/wallpapers/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers/livecd
