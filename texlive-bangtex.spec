# revision 15878
# category Package
# catalog-ctan /language/bangtex
# catalog-date 2006-12-14 21:17:11 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-bangtex
Version:	20061214
Release:	1
Summary:	Writing Bangla and Assamese with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/bangtex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangtex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle provides class files for writing Bangla and Assamese
with LaTeX, and MetaFont sources for fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/bangtex/bang10.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangbase.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangconso.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangdefs.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangfala.mf
%{_texmfdistdir}/fonts/source/public/bangtex/banghalf.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangjuk.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangkaar.mf
%{_texmfdistdir}/fonts/source/public/bangtex/banglig.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangmac.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangnum.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangpunc.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangsl10.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangvow.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangwd10.mf
%{_texmfdistdir}/fonts/tfm/public/bangtex/bang10.tfm
%{_texmfdistdir}/fonts/tfm/public/bangtex/bangsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bangtex/bangwd10.tfm
%{_texmfdistdir}/tex/latex/bangtex/bangfont.tex
%{_texmfdistdir}/tex/latex/bangtex/barticle.cls
%{_texmfdistdir}/tex/latex/bangtex/bbk10.clo
%{_texmfdistdir}/tex/latex/bangtex/bbk11.clo
%{_texmfdistdir}/tex/latex/bangtex/bbk12.clo
%{_texmfdistdir}/tex/latex/bangtex/bbook.cls
%{_texmfdistdir}/tex/latex/bangtex/bletter.cls
%{_texmfdistdir}/tex/latex/bangtex/bsize10.clo
%{_texmfdistdir}/tex/latex/bangtex/bsize11.clo
%{_texmfdistdir}/tex/latex/bangtex/bsize12.clo
%doc %{_texmfdistdir}/doc/latex/bangtex/README.bangtex
%doc %{_texmfdistdir}/doc/latex/bangtex/manual.tex
%doc %{_texmfdistdir}/doc/latex/bangtex/samplett.tex
%doc %{_texmfdistdir}/doc/latex/bangtex/samptex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
