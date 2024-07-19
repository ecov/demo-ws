from fastapi import FastAPI, Response, status
from fastapi import APIRouter, HTTPException,Depends
from fastapi import WebSocket, WebSocketDisconnect, WebSocketException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from logger import setLogger
import os
import uvicorn
logger = setLogger(__name__)


app = FastAPI()

@app.get("/_alive", status_code=204)
async def _alive():
  return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.websocket("/ws")
async def ws_sirene(websocket: WebSocket):
  logger.info("sirene worker "+ str(os.getpid()))
  await websocket.accept()

  try:
      response = await websocket.receive_json()
      try:
         with open("response.json", "r") as response:
          await websocket.send_text(response.read()) 
      except:
          logger.info("SIRENE WebSocketException WS_1003_UNSUPPORTED_DATA")
          raise WebSocketException(code=status.WS_1003_UNSUPPORTED_DATA)

      raise WebSocketException(code=status.WS_1000_NORMAL_CLOSURE)
  except WebSocketDisconnect:
      logger.info("websocket disconnect by the client")
      return
  await websocket.close()


if __name__ == '__main__':
    try:
        config = uvicorn.Config(
          "main:app",
          host="0.0.0.0",
          port=8000,
          ws_per_message_deflate=True,
          ws_ping_interval=10,
          ws_ping_timeout=10,
          workers=4,
          ws_max_size=70000000
        )
        server = uvicorn.Server(config)
        server.run()
    except Exception as e:
        raise