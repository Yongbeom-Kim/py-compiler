.PHONY: dev dev-watch publish build

dev:
	python setup.py develop

dev-watch:
	while true ; do ; python setup.py develop ; sleep 1 ; done

publish-test: build
	twine upload --repository testpypi --skip-existing dist/*

build:
	python setup.py sdist bdist_wheel

reinstall-test:
	pip uninstall py-compiler -y && pip install -i https://test.pypi.org/simple/ py-compiler