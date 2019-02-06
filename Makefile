start-local:
	rm -rf venv/
	virtualenv venv --no-site-packages -p python3.7
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

