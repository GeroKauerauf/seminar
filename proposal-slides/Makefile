slides.pdf : slides.tex
	lualatex $< -o$@
	lualatex $< -o$@

clean: 
	rm -f *.log *.toc *.aux slides.pdf *.snm *.nav *.out

.PHONY: clean
