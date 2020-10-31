report.pdf : report.tex
	lualatex report
	bibtex report
	lualatex report
	lualatex report

clean: 
	rm -f *.log *.toc *.aux report.pdf *.snm *.nav *.out *.bbl *.blg

.PHONY: clean
