%global tl_name scheme-tetex
%global tl_revision 74022

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	teTeX scheme (more than medium, but nowhere near full)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-tetex
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-tetex.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(acronym)
Requires:	texlive(amslatex-primer)
Requires:	texlive(bbm)
Requires:	texlive(bbm-macros)
Requires:	texlive(bbold)
Requires:	texlive(bibtex8)
Requires:	texlive(cmbright)
Requires:	texlive(collection-basic)
Requires:	texlive(collection-context)
Requires:	texlive(collection-fontsrecommended)
Requires:	texlive(collection-fontutils)
Requires:	texlive(collection-formatsextra)
Requires:	texlive(collection-langcjk)
Requires:	texlive(collection-langcyrillic)
Requires:	texlive(collection-langczechslovak)
Requires:	texlive(collection-langenglish)
Requires:	texlive(collection-langeuropean)
Requires:	texlive(collection-langfrench)
Requires:	texlive(collection-langgerman)
Requires:	texlive(collection-langgreek)
Requires:	texlive(collection-langitalian)
Requires:	texlive(collection-langother)
Requires:	texlive(collection-langpolish)
Requires:	texlive(collection-langportuguese)
Requires:	texlive(collection-langspanish)
Requires:	texlive(collection-latex)
Requires:	texlive(collection-latexrecommended)
Requires:	texlive(collection-mathscience)
Requires:	texlive(collection-metapost)
Requires:	texlive(collection-pictures)
Requires:	texlive(collection-plaingeneric)
Requires:	texlive(collection-pstricks)
Requires:	texlive(ctie)
Requires:	texlive(cweb)
Requires:	texlive(detex)
Requires:	texlive(dtl)
Requires:	texlive(dvi2tty)
Requires:	texlive(dvicopy)
Requires:	texlive(dvidvi)
Requires:	texlive(dviljk)
Requires:	texlive(eplain)
Requires:	texlive(eulervm)
Requires:	texlive(gentle)
Requires:	texlive(lshort-english)
Requires:	texlive(mltex)
Requires:	texlive(multirow)
Requires:	texlive(nomencl)
Requires:	texlive(patgen)
Requires:	texlive(pst-pdf)
Requires:	texlive(rsfs)
Requires:	texlive(seetexk)
Requires:	texlive(siunits)
Requires:	texlive(subfigure)
Requires:	texlive(supertabular)
Requires:	texlive(tamethebeast)
Requires:	texlive(tds)
Requires:	texlive(tie)
Requires:	texlive(web)
Requires:	texlive(xpdfopen)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Live scheme nearly equivalent to the teTeX distribution that was
maintained by Thomas Esser.

