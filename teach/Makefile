slides.pdf : slides.tex
	xelatex -shell-escape $< -o$@
	xelatex -shell-escape $< -o$@

clean: 
	rm -f *.log *.toc *.aux slides.pdf *.snm *.nav *.out
	rm -f __latexindent_temp.tex

.PHONY: clean
