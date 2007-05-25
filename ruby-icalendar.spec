Summary:	iCalendar parser and generator for Ruby
Name:		ruby-icalendar
Version:	0.98
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/16745/icalendar-0.98.gem
# Source0-md5:	7381ac5225cb3fc337a87605e9d7aa37
Patch0:	%{name}-noeval.patch
URL:		http://icalendar.rubyforge.org
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides iCalendar support for ruby. (RFC-2445) (Note: this is the format supported by Apple ical, Mozilla Sunbird, Evolution etc...)

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
%patch0 -p1
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/icalendar*
%{ruby_ridir}/Icalendar
