.PHONY: dev dev-watch publish publish-test build reinstall-test

dev:
	python3 -m pip install --user -e .

dev-watch:
	while true ; do python3 setup.py develop ; sleep 1 ; done

publish-test: build
	twine upload --repository testpypi --skip-existing dist/*

publish: build
	twine upload --skip-existing dist/*

build:
	python3 setup.py sdist bdist_wheel

reinstall-test:
	pip uninstall pycompall -y && pip install -i https://test.pypi.org/simple/ pycompall

reinstall:
	pip uninstall pycompall -y && pip install pycompall