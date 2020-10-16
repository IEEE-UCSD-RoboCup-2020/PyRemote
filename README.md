# PyRemote 
Remote control TritonBot program running locally or remotely via sockets.

## Dependency
* python3
* pip3
* protoc 3.11 or above
* pynput 
```
pip3 install --upgrade protobuf
pip3 install pynput
```

## Regenerate Proto Source Code (_pb2.py)
Note:  the _pb2 suffix here has **nothing** to do with proto version
```
make proto
```

### Run
```
make run
```