init:
	python -m venv env
	source env/bin/activate
	pip install fastapi uvicorn

save:
	pip freeze > requirements.txt

protoc:
	python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/protorest.proto

run:
	uvicorn main:app --reload

gen-gitignore:
	curl https://www.toptal.com/developers/gitignore/api/python > .gitignore

.PHONY: init ninja-init
