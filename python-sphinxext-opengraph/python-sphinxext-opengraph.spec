%global project_name sphinxext-opengraph

Name:           python-%{project_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Sphinx extension to generate unique OpenGraph metadata

License:        MIT
URL:            https://%{project_name}.readthedocs.io/en/latest/
Source0:        https://github.com/wpilibsuite/%{project_name}/archive/v%{version}/%{project_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
%{summary}.}

%description %_description

%package -n python3-%{project_name}
Summary:        %{summary}

%description -n python3-%{project_name} %_description

%prep
%autosetup -p1 -n %{project_name}-%{version}

sed -i 's|version = "main"|version = "%{version}"|' setup.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*'


%files -n python3-%{project_name} -f %{pyproject_files}
%doc README.md


%changelog
* Tue Feb 01 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.5.1-1
- initial spec for version 0.5.1

