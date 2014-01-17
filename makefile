.PHONY: test clean

test: .tox
	tox

# Clean if we edit any of the tox dependencies.
.tox: requirements.txt tox.ini
	make clean

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf .tox
	rm -rf canopener.egg-info
	rm -rf dist
