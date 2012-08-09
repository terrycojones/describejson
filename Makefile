check:
	python test.py

trial:
	trial --rterrors test.py

clean:
	rm -fr *~ .*~ *.pyc _trial_temp
