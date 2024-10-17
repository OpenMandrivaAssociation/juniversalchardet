%{?_javapackages_macros:%_javapackages_macros}
Name:          juniversalchardet
Version:       1.0.3
Release:       3.3
Summary:       A Java port of Mozilla's universalchardet
Group:         Development/Java
# ALL files are under MPL (v1.1) GPL license
# build.xml and c/* under MPL 1.1/GPL 2.0/LGPL 2.1 license
License:       MPLv1.1 or GPLv2+ or LGPLv2+
URL:           https://code.google.com/p/juniversalchardet/
Source0:       http://juniversalchardet.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:       http://repo1.maven.org/maven2/com/googlecode/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# added javadoc task
# fix example build
Patch0:        %{name}-1.0.3-build.patch

BuildRequires: java-devel
BuildRequires: javapackages-tools
BuildRequires: ant

Requires:      javapackages-tools
BuildArch:     noarch

%description
juniversalchardet is a Java port of 'universalchardet',
that is the encoding detector library of Mozilla.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p0

sed -i 's/\r//' readme.txt

%build

%ant dist javadoc example

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 dist/%{name}-example-%{version}.jar %{buildroot}%{_javadir}/%{name}-example.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/%{name}-example.jar
%doc MPL-1.1.txt readme.txt

%files javadoc
%{_javadocdir}/%{name}
%doc MPL-1.1.txt

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.3-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 21 2013 gil cattaneo <puntogil@libero.it> 1.0.3-1
- initial rpm
