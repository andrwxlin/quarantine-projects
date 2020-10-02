from pypresence import Presence
import time
import datetime

english = input("what drama? (english name)")
foreign = input("what drama? (foreign name)")

client_id = "759925694624694302"
RPC = Presence(client_id)
RPC.connect()

try:
    while True:
        RPC.update(details=english, state=foreign, start=time.time())
        time.sleep(300)
except KeyboardInterrupt:
    RPC.close()