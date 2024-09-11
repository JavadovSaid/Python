from playsound3 import playsound
import time
CLEAR = "/033[2J"
CLEAR_AND_RETURN = "/033[H"
def alarm(seconds):
    current_time = 0

    while current_time < seconds:
        time.sleep(1)
        current_time+=1
        left_time = seconds - current_time
        minute_time = left_time//60
        second_time = left_time%60

        print(f"{minute_time:02d}:{second_time:02d}")
    playsound("C:\\Users\\Huawei\\Downloads\\twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3")
minute = int(input("How meny minutes do you wanna wait ? "))
second = int(input("How meny seconds do you wanna wait ? "))
total_time = minute * 60 +second
alarm(total_time)


