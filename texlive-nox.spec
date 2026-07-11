%global tl_name nox
%global tl_revision 30991

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Adaptable tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nox
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows data, text (including (La)TeX commands or
environments) to be formatted into a array which may be split.

