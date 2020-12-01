slides.pdf : slides.tex
	xelatex -shell-escape $< -o$@

clean: 
	rm -f *.log *.toc *.aux slides.pdf *.snm *.nav *.out

.PHONY: clean
