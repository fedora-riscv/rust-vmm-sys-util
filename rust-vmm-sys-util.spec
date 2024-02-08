# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate vmm-sys-util

Name:           rust-vmm-sys-util
Version:        0.12.1
Release:        %autorelease -e rv64
Summary:        System utility set

License:        BSD-3-Clause
URL:            https://crates.io/crates/vmm-sys-util
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
Patch:          vmm-sys-util-fix-metadata.diff
# Omit tests that require access to "/dev/kvm"
Patch:          vmm-sys-util-omit-ioctl-tests.diff
# Omit unsupported timestamp test on aarch64
Patch:          vmm-sys-util-omit-timestamp-test.diff
# Omit unsupported pseudo_rng test on aarch64
Patch:          vmm-sys-util-omit-pseudo_rng-test.diff

ExclusiveArch:  x86_64 aarch64 ppc64l riscv64
BuildRequires:  rust-packaging >= 21
BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A system utility set.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-BSD-3-Clause
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-serde-devel %{_description}

This package contains library source intended for building other packages which
use the "with-serde" feature of the "%{crate}" crate.

%files       -n %{name}+with-serde-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
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
%autochangelog
