# pip3 install --upgrade protobuf

default: run

run:
	python3 PyRemote.py

proto: RemoteAPI.proto
	protoc --python_out=. RemoteAPI.proto

clean:
	rm -f RemoteAPI_pb2.py


.PHONY: clean