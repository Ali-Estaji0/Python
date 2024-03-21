import tkinter as tk
import os
import pygame as pg


root = tk.Tk()  # Make Instance Of Tkinter
root.title('Music Player')  # Title Of Root
root.geometry('600x410')
root.resizable(0, False)

Status = tk.StringVar()
pg.init()
pg.mixer.init()


# -----------------button function-------------------------#


def PlaySong():
    ShowSongName.config(state='normal')
    ShowSongName.delete('1.0', 'end')
    ShowSongName.insert('1.0', PlayList.get('active'))
    ShowSongName.config(state='disable')
    Status.set('Playing')
    pg.mixer.music.load(PlayList.get('active'))
    pg.mixer.music.play()


def StopSong():
    Status.set("Stopped")
    pg.mixer.music.stop()


def PauseSong():
    Status.set('Paused')
    pg.mixer.music.pause()


def UnpauseSong():
    Status.set("UnPausing")
    pg.mixer.music.unpause()


# --------------- Song Play List -------------------------#
SongFrame = tk.LabelFrame(root, text='Song Track',
                          bg='black', fg='white', bd=5, font=("Segoe Print", 10))
SongFrame.place(x=10, y=3, width=580, height=210)

ScrollY = tk.Scrollbar(SongFrame, orient='vertical')

PlayList = tk.Listbox(SongFrame, bg='silver', fg='black', font=(
    'Arial', 10), selectmode='single', selectbackground='black', height='100', yscrollcommand=ScrollY.set)
ScrollY.config(command=PlayList.yview)
ScrollY.pack(fill='y', side='right')

PlayList.pack(fill='both')


# --------------- Song Track -------------------------#

TrackFrame = tk.LabelFrame(root, text='Song Track',
                           bg='black', fg='white', bd=5, font=("Segoe Print", 10))
TrackFrame.place(x=10, y=219, width=580, height=90)


ShowSongName = tk.Text(TrackFrame, bg='white', fg='black',
                       width=50, height=1, state='disabled')
ShowSongName.grid(row=0, column=0, padx=17, pady=13)

ShowStates = tk.Label(TrackFrame, bg='white', fg='black',
                      width='15', textvariable=Status)
ShowStates.grid(row=0, column=1)
# --------------- Control Panel -------------------------#
CtrPanel = tk.LabelFrame(root, text='Control Panel',
                         bg='black', fg='white', bd=5, font=("Segoe Print", 10), padx=15)
CtrPanel.place(x=10, y=314, width=580, height=90)

PLayBtn = tk.Button(CtrPanel, text='PLay', width=15, command=PlaySong)
PLayBtn.grid(row=0, column=0, padx=10, pady=17)

StopBtn = tk.Button(CtrPanel, text='Stop', width=15, command=StopSong)
StopBtn.grid(row=0, column=1, padx=10, pady=17)

UnpauseBtn = tk.Button(CtrPanel, text='UnPause', width=15, command=UnpauseSong)
UnpauseBtn.grid(row=0, column=2, padx=10, pady=17)

PauseBtn = tk.Button(CtrPanel, text='Pause', width=15, command=PauseSong)
PauseBtn.grid(row=0, column=3, padx=10, pady=17)


os.chdir(r'F:\____dekstop\Music')
MySong = os.listdir()
for song in MySong:
    if ".mp3" in song:
        PlayList.insert('end', song)

root.mainloop()
