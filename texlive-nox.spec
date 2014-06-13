# revision 30991
# category Package
# catalog-ctan /macros/latex/contrib/nox
# catalog-date 2013-06-19 16:57:50 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-nox
Version:	1.0
Release:	6
Summary:	Adaptable tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows data, text (including (La)TeX commands or
environments) to be formatted into a array which may be split.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nox/nox.sty
%doc %{_texmfdistdir}/doc/latex/nox/README
%doc %{_texmfdistdir}/doc/latex/nox/nox.pdf
%doc %{_texmfdistdir}/doc/latex/nox/nox.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
