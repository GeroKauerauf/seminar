slides.pdf : slides.tex
	xelatex $< -o$@
	xelatex $< -o$@

clean: 
	rm -f *.log *.toc *.aux slides.pdf *.snm *.nav *.out

.PHONY: clean
