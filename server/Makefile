init:
	python -m venv env
	source env/bin/activate
	pip install fastapi uvicorn

save:
	pip freeze > requirements.txt

protoc:
	protoc -I=. --python_out=. models.proto

run:
	uvicorn main:app --reload --port 8002

gen-gitignore:
	curl https://www.toptal.com/developers/gitignore/api/python > .gitignore

.PHONY: init save protoc run gen-gitignore