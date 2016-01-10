# Tornado WebSocket and REST API example

This is a websocket and rest api example written in python.

## Reference:

  `https://github.com/hiroakis/tornado-websocket-rest-example.git`

## Installation

1. `git clone https://github.com/thermalogic/tornado-websocket-rest-example.git`

2. `cd tornado-websocket-example`

3. Edit index.html

  `ws = new WebSocket("ws://" + window.location.host + "/ws")`  <- change to your url/localhost

4. `pip install -r requirements.txt`

5. `python app.py`

6. http://127.0.0.1:8000/

7. Send a REST call:

 `http://127.0.0.1:8000/api?id=1&value=100`

## REST API examples

Set the "id 1" value to 100 :
- `curl "http://127.0.0.1:8000/api?id=1&value=100"`

Set the "id 1" value to 300( The row No 1 will change to yellow ) :
- `curl "http://127.0.0.1:8000/api?id=1&value=300"`

Set The "id 1" value to 600( The row No 1 will change to red ):
- `curl "http://127.0.0.1:8000/api?id=1&value=600"`

- value 201 - 500 : change to yellow
- value 501 - : change to red

## License

MIT 
