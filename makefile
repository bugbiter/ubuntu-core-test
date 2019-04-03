#init:
#	pip install -r snap/requirements.txt

publish:
	python setup.py sdist bdist_wheel upload
