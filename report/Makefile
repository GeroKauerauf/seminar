report.pdf : report.tex
	xelatex -shell-escape report
	bibtex report
	xelatex -shell-escape report
	xelatex -shell-escape report

clean: 
	rm -f *.log *.toc *.aux report.pdf *.snm *.nav *.out *.bbl *.blg
	rm -R _minted-report

.PHONY: clean
