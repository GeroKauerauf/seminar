report.pdf : report.tex
	xelatex report
	bibtex report
	xelatex report
	xelatex report

clean: 
	rm -f *.log *.toc *.aux report.pdf *.snm *.nav *.out *.bbl *.blg

.PHONY: clean
