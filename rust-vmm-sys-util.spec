# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate vmm-sys-util

Name:           rust-%{crate}
Version:        0.8.0
Release:        2%{?dist}
Summary:        Helpers and utilities used by multiple rust-vmm components and VMMs 

# Upstream license specification: Apache-2.0 AND BSD-3-Clause
License:        ASL 2.0 and BSD
URL:            https://crates.io/crates/vmm-sys-util
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded files
Patch0:         vmm-sys-util-fix-metadata.diff
# Omit tests that require access to "/dev/kvm"
Patch1:         vmm-sys-util-omit-ioctl-tests.diff

ExclusiveArch:  x86_64 aarch64 ppc64le
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Helpers and utilities used by multiple rust-vmm components and VMMs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-BSD-3-Clause
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages
which use "serde_derive" feature of "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-serde-devel %{_description}

This package contains library source intended for building other packages
which use "with-serde" feature of "%{crate}" crate.

%files       -n %{name}+with-serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Mon May 03 2021 Sergio Lopez <slp@redhat.com> - 0.8.0-2
- Exclude unsupported arches

* Tue Mar 23 2021 Sergio Lopez <slp@redhat.com> - 0.8.0-1
- Initial package