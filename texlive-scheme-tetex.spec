# revision 21479
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-tetex
Version:	20120307
Release:	1
Summary:	teTeX scheme (more than medium, but nowhere near full)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-tetex.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-FAQ-en
Requires:	texlive-SIunits
Requires:	texlive-acronym
Requires:	texlive-amslatex-primer
Requires:	texlive-bbm
Requires:	texlive-bbm-macros
Requires:	texlive-bbold
Requires:	texlive-bibtex8
Requires:	texlive-ctie
Requires:	texlive-detex
Requires:	texlive-dtl
Requires:	texlive-dvi2tty
Requires:	texlive-dvicopy
Requires:	texlive-dvidvi
Requires:	texlive-dviljk
Requires:	texlive-patgen
Requires:	texlive-pdftools
Requires:	texlive-seetexk
Requires:	texlive-tie
Requires:	texlive-web
Requires:	texlive-cmbright
Requires:	texlive-cweb
Requires:	texlive-eplain
Requires:	texlive-eulervm
Requires:	texlive-gentle
Requires:	texlive-lshort-english
Requires:	texlive-mathmode
Requires:	texlive-mltex
Requires:	texlive-multirow
Requires:	texlive-nomencl
Requires:	texlive-pst-pdf
Requires:	texlive-pstricks-tutorial
Requires:	texlive-rsfs
Requires:	texlive-subfigure
Requires:	texlive-supertabular
Requires:	texlive-tamethebeast
Requires:	texlive-tds
Requires:	texlive-tex-refs
Requires:	texlive-collection-basic
Requires:	texlive-collection-context
Requires:	texlive-collection-documentation-base
Requires:	texlive-collection-fontutils
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-genericrecommended
Requires:	texlive-collection-langcjk
Requires:	texlive-collection-langcroatian
Requires:	texlive-collection-langcyrillic
Requires:	texlive-collection-langczechslovak
Requires:	texlive-collection-langdanish
Requires:	texlive-collection-langdutch
Requires:	texlive-collection-langfinnish
Requires:	texlive-collection-langfrench
Requires:	texlive-collection-langgerman
Requires:	texlive-collection-langgreek
Requires:	texlive-collection-langhungarian
Requires:	texlive-collection-langitalian
Requires:	texlive-collection-langlatin
Requires:	texlive-collection-langmongolian
Requires:	texlive-collection-langnorwegian
Requires:	texlive-collection-langother
Requires:	texlive-collection-langpolish
Requires:	texlive-collection-langportuguese
Requires:	texlive-collection-langspanish
Requires:	texlive-collection-langswedish
Requires:	texlive-collection-langenglish
Requires:	texlive-collection-langvietnamese
Requires:	texlive-collection-latex
Requires:	texlive-collection-latexrecommended
Requires:	texlive-collection-mathextra
Requires:	texlive-collection-metapost
Requires:	texlive-collection-omega
Requires:	texlive-collection-pictures
Requires:	texlive-collection-pstricks
Requires:	texlive-collection-texinfo
%rename tetex
%rename texlive-dviutils

%description
TeX Live scheme nearly equivalent to the teTeX distribution
that was maintained by Thomas Esser.

%posttrans
    %{_sbindir}/texlive.post -

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120307-1
+ Revision: 783157
- Import texlive-scheme-tetex
- Import texlive-scheme-tetex

