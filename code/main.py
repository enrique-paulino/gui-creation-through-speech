from listen import listener
from commands import take
import tkinter as tk
import threading

window = tk.Tk()
window.title("VoiceGUI")
window.geometry("640x360")


def rec():
    while True:
        take(listener(), window)


window.wait_visibility()
threading.Thread(target=rec).start()
window.mainloop()
