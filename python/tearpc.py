from pypresence import Presence
import time
import datetime

images = "tgy (tieguanyin)"
toppings = "goji"

tea = input("what tea?")
print(images)
limage = input("large image?")
print(toppings)
topping = input("what additions?")
simage = input("small image?")
ltt = input("large tooltip?")
stt = input("small tooltip?")


client_id = "761078336637632522"
RPC = Presence(client_id)
RPC.connect()
aaaa = time.time()

count = 1
def tea_update():
    RPC.update(details = tea + " with " + topping, state = "cup #" + str(count), large_image = limage, small_image = simage, large_text = ltt, small_text = stt, start=aaaa)

try:
    while True:
        tea_update()
        counter = input("press enter to add 1 cup, \'update\' to update your rich presence stuff, or \'reset\' to reset the number of cups")
        if counter == "":
            count += 1
            tea_update()
        elif counter == "update":
            tea = input("what tea?")
            print(images)
            limage = input("large image?")
            print(toppings)
            topping = input("what additions?")
            simage = input("small image?")
            ltt = input("large tooltip?")
            stt = input("small tooltip?")
        elif counter == "reset":
            count = 1
        else:
            print("invalid response")
except KeyboardInterrupt:
    RPC.close()