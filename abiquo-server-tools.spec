%define abiquo_basedir /opt/abiquo

Name:     abiquo-server-tools
Version: 1.7
Release:  6.v0.0.15%{?dist}%{?buildstamp}
Summary:  Abiquo Server Tools
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source:  %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package installs Abiquo Server Tools.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -r $RPM_BUILD_DIR/%{name}-%{version}/ $RPM_BUILD_ROOT/%{abiquo_basedir}/tools
cp $RPM_BUILD_ROOT/%{abiquo_basedir}/tools/abiquoServerCheckState.sh $RPM_BUILD_ROOT/%{_bindir}/
cp $RPM_BUILD_ROOT/%{abiquo_basedir}/tools/abiquoNodeInfoCollector.sh $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tools/
%{_bindir}/abiquoServerCheckState.sh
%{_bindir}/abiquoNodeInfoCollector.sh

%changelog
* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6.v0.0.15
- add redis migration tools

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5.v0.0.14
- upstream update

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- upstream update

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- upstream update

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- include abiquo17-update-config script

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Tue Sep 21 2010 Sergio Rubio srubio@abiquo.com 1.6.5-2
- Fixed bin scripts

* Tue Sep 14 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- Initial Release
