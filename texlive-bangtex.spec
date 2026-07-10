%global tl_name bangtex
%global tl_revision 55475

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Writing Bangla and Assamese with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/bengali/bangtex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangtex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides class files for writing Bangla and Assamese with
LaTeX, and Metafont sources for fonts.

