# this is a header-only library with architecture-dependent .pc file
%global debug_package %{nil}

%define devname %mklibname -d %{name}

Name:           tllist
Version:        1.1.0
Release:        1
Summary:        C header file only implementation of a typed linked list

License:        MIT
URL:            https://codeberg.org/dnkl/tllist
Source0:        https://codeberg.org/dnkl/tllist/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson

%description
Tllist is a C header-only implementation of a linked list that uses
pre-processor macros to implement dynamic types, where the data carrier
is typed to whatever you want; both primitive data types are supported
as well as aggregated ones such as structs, enums and unions.

%package -n %{devname}
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description -n %{devname}
Devel packages fpr Tllist.

%prep
%autosetup -p1 -n %{name}

%build
%meson
%meson_build

%install
%meson_install
# license will be installed to correct location with rpm macros
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

%files -n %{devname}
%license LICENSE
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.md
