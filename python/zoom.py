from pypresence import Presence
import time

client_id = "753283872443203636"
RPC = Presence(client_id)
RPC.connect()

def meeting_RPC():
    asdf = input("What class?")
    RPC.update(details='In a meeting', state=asdf, large_image="zoom", start=time.time())
    decision = input("CTRL+C or close this window to exit, press ENTER to start a new meeting")
    if decision == "":
        meeting_RPC()
    else:
        print("Invalid response")

try:
    meeting_RPC()
except KeyboardInterrupt:
    print("class ended")
    RPC.close()
