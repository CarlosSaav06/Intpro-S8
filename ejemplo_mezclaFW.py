import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for i in range(5):
    for j in range(5):
        text = f"{i}, {j}"
        speaker.Speak(text)
        time.sleep(3)
