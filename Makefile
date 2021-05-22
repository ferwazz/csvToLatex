#PHONY

.PHONY: clean


reports/template_format.pdf: reports/template_format.tex
	cd $(<D) && xelatex $(<F)	
	cd $(<D) && xelatex $(<F)

clean:
	rm -f reports/*.pdf
	rm -f reports/*.aux
	rm -f reports/*.out
	rm -f reports/*.log

