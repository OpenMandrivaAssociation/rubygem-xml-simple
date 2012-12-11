%define oname xml-simple

Name:       rubygem-%{oname}
Version:    1.0.12
Release:    %mkrel 1
Summary:    A simple API for XML processing
Group:      Development/Ruby
License:    GPLv2+ or Ruby License
URL:        http://xml-simple.rubyforge.org
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A simple API for XML processing.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Fri Dec 10 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.12-1mdv2011.0
+ Revision: 620455
- import rubygem-xml-simple

