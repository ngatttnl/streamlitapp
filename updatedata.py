from datetime import date
import pandas as pd
import websocket, json, pprint
from sqlalchemy import create_engine

engine = create_engine('sqlite:///crypto.db')
SOCKET = "wss://stream.binance.com:9443/ws/!miniTicker@arr"
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    json_message = json.loads(message)
    #pprint.pprint(json_message)
    symbol = [x for x in json_message if x['s'].endswith('USDT')]
    frame = pd.DataFrame(symbol)[['E', 's', 'c']]
    frame.E = pd.to_datetime(frame.E, unit='ms')
    frame.c = frame.c.astype(float)
    #print(frame)
    for row in range(len(frame)):
        data = frame[row:row+1]
        data[['E', 'c']].to_sql(data['s'].values[0], con = engine, index = False, if_exists = 'append')
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()

