from pypresence import Presence
import time
import datetime
import math

# define time_convert()
def time_convert(sec):
    mins, secs = divmod(int(sec), 60)
    return mins, secs

#pomodoro timer intro
print('What is the Pomodoro Technique?')
print('The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for "tomato", after the tomato-shaped kitchen timer that Cirillo used as a university student.')
print('\nHere\'s how it works: During each Pomodoro, you will have 25 minutes to work hard. After each Pomodoro, you get a 5 minute break. After every 4th Pomodoro, you get a 10 minute break.')
print('\nTo quit the program, simply hit CTRL+C and the timer will stop.')
print('\nMade with love by Andrew Lin. Want to provide feedback? DM me on Discord: andrwx#1010')
print('\nv1.1.1, build date 09/03/2020')

# start session?
try:
    input('\nPress ENTER to start a session, or CTRL+C to quit.')
except KeyboardInterrupt:
    print('\nBye bye!')
    quit()

while True:
    idk = str(math.ceil(time.time()) - time.time())
    if '.0' not in idk:
        print("Waiting to start")
        time.sleep(.3)
    else:
        break

start_time = time.time()
print('Happy studying!')

# discord rpc
client_id = "751188379013480559"
RPC = Presence(client_id)
RPC.connect()

count = 1

# define countdown()
def countdown(t):
    time_difference = time.time() + t - time.time()

    while time_difference:
        mins, secs = time_convert(time_difference)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time_difference -= 1
        time.sleep(.9999)
    if t == study:
        print('Start of break time')
    else:
        print('End of break time')

# define presence 
def prGen(type, image, t):
    lol = time.time() + t + 1
    RPC.update(details='Study interval #{}'.format(count), state=type, large_image=image, large_text="made by andrwx#1010", end=lol)

# pomodoro timer
try:
    while True:
        study = 1500
        print('Interval {}'.format(count))
        prGen("Currently studying", "pencil_and_paper", study)
        countdown(int(study))

        if count % 4 != 0:
            rest = 300
        else: 
            rest = 600
        prGen("Taking a break", "boba", rest)
        countdown(int(rest))

        count += 1
except KeyboardInterrupt:
    end_time = time.time()
    time_elapsed = end_time - start_time
    mins, secs = time_convert(time_elapsed)
    
    print('Total session time: {:02d}m:{:02d}s'.format(mins, secs))
    print('Total number of completed intervals: {}'.format(count - 1))
    RPC.close()
