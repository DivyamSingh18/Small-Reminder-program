
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log


from pygame import mixer
from time import time
from datetime import datetime

init_water = time()
init_eyes = time()
init_exercise = time()

water_time = 1800
eyes_time = 2400
exercise_time = 3600

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg}   :=:  {datetime.now()}\n")

# infinite loop
while True:
    if time() - init_eyes > eyes_time:
        print("Relax your eyes please")
        musiconloop('Relax your eyes please.mp3', 'done')
        init_eyes = time()
        log("Eyes relaxed at ")

    if time() - init_water > water_time:
        print("Time to drink water")
        musiconloop('Drink water.mp3','drank')
        init_water = time()
        log("Drank water at ")


    if time() - init_exercise > exercise_time:
        print("Time for some exercise")
        musiconloop('Time for some exercise.mp3', 'done')
        init_exercise = time()
        log("Exercise done at ")