Name:           compute
Version:        X.Y.Z
Release:        1%{?dist}
Summary:        Simple Command-line Calculations

Group:          Applications/File 
License:        GPLv3+
URL:            http://agordon.github.io/compute/
Source0:        https://s3.amazonaws.com/agordon/compute/src/compute-X.Y.Z.tar.gz

#BuildRequires:  
#Requires:       

%description
The 'Compute' program provices simple command-line calculation
(sum,min,max,mean,stdev,etc.) on tabular textual input files.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_mandir}/man1/compute.1.gz
%{_bindir}/compute
%{_datadir}/compute/examples/readme.md
%{_datadir}/compute/examples/genes.txt
%{_datadir}/compute/examples/genes_h.txt
%{_datadir}/compute/examples/scores.txt
%{_datadir}/compute/examples/scores_h.txt


%changelog
* Wed Mar 12 2014 A. Gordon <assafgordon@gmail.com> 1.0.1
- Initial Release
