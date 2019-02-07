Name:       telepathy-rakia
Summary:    SIP connection manager for Telepathy
Version:    0.7.4
Release:    1
Group:      Applications/Communications
License:    LGPLv2+
URL:        http://telepathy.freedesktop.org/wiki/Components
Source0:    http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:    runTest.sh
Source2:    mktests.sh
Patch0:     0001-Check-for-gio-to-avoid-linking-issue.patch
Patch1:     0002-nemo-test-install.patch
Patch2:     0003-switch-to-using-gireactor-to-work-with-new-gi-based-.patch
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(telepathy-glib) >= 0.17.7
BuildRequires:  pkgconfig(sofia-sip-ua-glib) >= 1.12.11
BuildRequires:  libxslt
BuildRequires:  python >= 2.3
BuildRequires:  python-twisted
Provides:   telepathy-sofiasip = %{version}-%{release}
Obsoletes:  telepathy-sofiasip < 0.7.2

%description
%{name} is a SIP connection manager for the Telepathy
framework based on the SofiaSIP-stack.


%package tests
Summary:    Tests package for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   python-twisted
Requires:   dbus-python
Requires:   pygobject2

%description tests
The %{name}-tests package contains tests and
tests.xml for automated testing.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Library, headers, and other files for developing applications
that use %{name}.


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.


%prep
%setup -q -n %{name}-%{version}/%{name}

# 0001-Check-for-gio-to-avoid-linking-issue.patch
%patch0 -p1
# 0002-nemo-test-install.patch
%patch1 -p1
# 0003-switch-to-using-gireactor-to-work-with-new-gi-based-.patch
%patch2 -p1
%__cp $RPM_SOURCE_DIR/mktests.sh tests/
%__chmod 0755 tests/mktests.sh

%build
%autogen --no-configure

%configure --disable-static
make %{?_smp_mflags}

tests/mktests.sh > tests/tests.xml

%install
rm -rf %{buildroot}
%make_install

install -m 0755 $RPM_SOURCE_DIR/runTest.sh $RPM_BUILD_ROOT/opt/tests/%{name}/bin/runTest.sh
install -m 0644 tests/tests.xml $RPM_BUILD_ROOT/opt/tests/%{name}/tests.xml

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        README NEWS TODO

%files
%defattr(-,root,root,-)
%license COPYING
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager

%files tests
%defattr(-,root,root,-)
/opt/tests/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}-0.7

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
%{_mandir}/man8/%{name}.8.gz
