init:
	pip install -r snap/requirements.txt

publish:
	#python setup.py develop
	#python setup.py sdist bdist_wheel upload
	pip install -e ./bin