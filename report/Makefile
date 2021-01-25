DEPEND = $(shell find ./introduction -name "*.tex") $(shell find ./problem-description -name "*.tex") $(shell find ./feedforward-networks -name "*.tex") $(shell find ./deep-learning -name "*.tex") $(shell find ./state-of-the-art -name "*.tex") $(shell find ./conclusion -name "*.tex")

report.pdf : report.tex $(DEPEND)
	xelatex -shell-escape report
	bibtex report
	xelatex -shell-escape report
	xelatex -shell-escape report

clean: 
	rm -f *.log *.toc *.aux report.pdf *.snm *.nav *.out *.bbl *.blg
	rm -R _minted-report

.PHONY: clean
