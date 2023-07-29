from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import os


def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="/home/aadhil/Documents/tkinter calculator/music/",
                                           title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_song:
        s = os.path.basename(s)
        songs_list.insert(END, s)


def Play():
    song = songs_list.get(ACTIVE)
    song = f'/home/aadhil/Documents/tkinter calculator/music/{song}'
    mixer.music.load(song)
    mixer.music.play()


def Pause():
    mixer.music.pause()


root = Tk()
root.title('Music Player App')
mixer.init()

songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="green", font=('arial', 15), height=12, width=47,
                     selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

defined_font = font.Font(family='Helvetica')

play_button = Button(root, text="Play", width=20, height=3, command=Play)
play_button['font'] = defined_font
play_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

pause_button = Button(root, text="Pause", width=20, height=3, command=Pause)
pause_button['font'] = defined_font
pause_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)

root.mainloop()
