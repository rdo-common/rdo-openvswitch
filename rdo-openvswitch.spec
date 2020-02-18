%define ovs_version 2.12

# Comma-separated (no spaces) e.g. 2.10,2.9 ...
%define obsolete_ovs_versions 2.11

%{lua:
function ovs_obsoletes(package)
  local ovsv = rpm.expand("%ovs_version")
  print("Obsoletes: "..package.." < "..ovsv.."\n")
  for s in string.gmatch(rpm.expand("%obsolete_ovs_versions"), "[^,]+") do
    print("Obsoletes: "..package..s.." < "..ovsv.."\n")
  end
end}

Name:		rdo-openvswitch
Version:	%{ovs_version}
Release:	0.5%{?dist}
Summary:	Wrapper rpm to allow installing OVS with new versioning schemes

Group:		System Environment/Daemons
License:	Public domain
URL:		http://www.openvswitch.org
BuildArch:  noarch

Requires:	openvswitch >= %{ovs_version}
Requires:       network-scripts-openvswitch >= %{ovs_version}
Provides:	rhosp-openvswitch = %{ovs_version}
%{lua:ovs_obsoletes("openvswitch")}

%description
Wrapper rpm for the base openvswitch package

%package -n python3-rdo-openvswitch
Summary:    wrapper for python-openvswitch rpm
License:    Public domain
Requires:   python3-openvswitch >= %{ovs_version}
Provides: python3-rhosp-openvswitch = %{ovs_version}
%if 0%{?rhel} > 7
%{lua:ovs_obsoletes("python3-openvswitch")}
%endif
%{lua:ovs_obsoletes("python2-openvswitch")}
%{lua:ovs_obsoletes("python-openvswitch")}

%description -n python3-rdo-openvswitch
Wrapper rpm for the base python-openvswitch package

%package devel
Summary:    wrapper for openvswitch-devel rpm
License:    Public domain
Provides:   rhosp-openvswitch-devel =  %{ovs_version}
Requires:   openvswitch-devel >= %{ovs_version}
%{lua:ovs_obsoletes("openvswitch-devel")}

%description devel
Wrapper rpm for the base openvswitch-devel package

%package ovn-central
Summary:    wrapper for ovn-central rpm
License:    Public domain
Provides:   rhosp-openvswitch-ovn-central = %{ovs_version}
Requires:   ovn-central >= %{ovs_version}
%{lua:ovs_obsoletes("openvswitch-ovn-central")}

%description ovn-central
Wrapper rpm for the base ovn-central package

%package ovn-host
Summary:    wrapper for ovn-host rpm
License:    Public domain
Requires:   ovn-host >= %{ovs_version}
Provides:   rhosp-openvswitch-ovn-host = %{ovs_version}
%{lua:ovs_obsoletes("openvswitch-ovn-host")}

%description ovn-host
Wrapper rpm for the base ovn-host package

%package ovn-vtep
Summary:    wrapper for ovn-vtep rpm
License:    Public domain
Requires:   ovn-vtep >= %{ovs_version}
Provides:   rhosp-openvswitch-ovn-vtep = %{ovs_version}
%{lua:ovs_obsoletes("openvswitch-ovn-vtep")}

%description ovn-vtep
Wrapper rpm for the base ovn-vtep package

%package ovn
Summary:    wrapper for ovn rpm
License:    Public domain
Requires:   ovn >= %{ovs_version}
Provides:   rhosp-openvswitch-ovn = %{ovs_version}
%{lua:ovs_obsoletes("openvswitch-ovn-common")}

%description ovn
Wrapper rpm for the base ovn package

%package test
Summary:    wrapper for openvswitch-test rpm
License:    Public domain
Requires:   openvswitch-test >= %{ovs_version}
Provides:   rhosp-openvswitch-test = %{ovs_version}
%{lua:ovs_obsoletes("openvswitch-test")}

%description test
Wrapper rpm for the base openvswitch-test package

%setup

%build

%files
%files -n python3-rdo-openvswitch
%files devel
%files ovn-central
%files ovn-host
%files ovn-vtep
%files ovn
%files test

%changelog
* Tue Feb 18 2020 Alfredo Moralejo <amoralej@redhat.com> - 2.12.0-1
- Initial version of compatibility wrapper.
