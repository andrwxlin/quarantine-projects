from pypresence import Presence
import time
import datetime

asdf = input("What class?")

client_id = "753283872443203636"
RPC = Presence(client_id)
RPC.connect()

try:
    start_time = time.time()
    while True:
        RPC.update(details='In a meeting', state=asdf, large_image="zoom", start=start_time)
        time.sleep(60)
except KeyboardInterrupt:
    print("class ended")
    RPC.close()
