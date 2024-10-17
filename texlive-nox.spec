Name:		texlive-nox
Version:	30991
Release:	2
Summary:	Adaptable tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nox.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
