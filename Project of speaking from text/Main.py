from gtts import gTTS
import os as o
import tkinter as tk
root = tk.Tk()  


def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speak.mp3")
    #mac
    o.system("afplay speak.mp3")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Speak", command=lambda: speak(entry.get()))
button.pack()




root.mainloop()