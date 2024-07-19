# Demo application for web socket
This app expose a websocket and return a 10 MB response in json format

## Run locally

- `pip install -r requirements.txt`
- `python main.py`

## Run with docker

- `docker build . -t <your tag>`
- `docker run --rm -p 8000:8000 <your tag>`

## Use websocket

Once the server is up connect to the websocket at: `ws://localhost:8000/ws` and send any message in json format:
for example: `{"message": "message"}`

## Deploy on kuberenetes

Push your image on a docker registry and change the image name in `k8s.yml` deployment