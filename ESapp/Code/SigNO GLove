from PIL import Image
from PIL import ImageTk

import tkinter as tk
from tkinter import ttk

import json

import pyttsx3



#window
window = tk.Tk()		
window.title('SignoGlove')
window.geometry('700x800')
window.configure(bg='blue')

Engine = pyttsx3.init()

background_image=tk.PhotoImage(file = "C:\\Users/Emmanuel\\Dropbox/My PC (DESKTOP-3AI9NQB)\\Downloads\\Signo Glove\\Textures\\OIG.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

TTT_Button = tk.PhotoImage(file='C:\\Users\Emmanuel\\Dropbox\\My PC (DESKTOP-3AI9NQB)\\Downloads\\Signo Glove\\Textures\\TTS-removebg-preview_mini.png')
Edit_audio_Btton = tk.PhotoImage(file="C:\\Users\\Emmanuel\\Dropbox\\My PC (DESKTOP-3AI9NQB)\\Downloads\\Signo Glove\\Textures\\AUDIO_Profile-removebg-preview_mini.png")
scale = tk.Scale(window,from_ = 0,to = 10, orient = 'horizontal', label = 'Volume', length = 200, width = 20, font = ('Consolas', 15 ) )


def Edit_TTS_Profile():
	Edit_audio.pack_forget()
	TTS.pack_forget()
	title_label.pack_forget()
	scale.pack(pady=350)
	title_label.place_forget()


	
	Bck.place(x=260, y=5)
	

def TTS():
	Edit_audio.pack_forget()
	TTS.pack_forget()
	title_label.pack_forget()
	title_label.place_forget()
	TTS_entry.pack(pady=350)
	Back_2.place(x=260, y=5)
	Say.pack()

 

def Back():
    scale.pack_forget()
    Bck.place_forget()
    title_label.place(x=280, y=5)
    title_label.lift()
    
    
    Edit_audio.pack(pady = 50)
    TTS.pack(pady = 20)

def Bck_2():
	TTS_entry.pack_forget()
	
	Say.pack_forget()
	Back_2.place_forget()
	title_label.place(x=280, y=5)
	title_label.lift()


	Edit_audio.pack(pady = 50)	   
	TTS.pack(pady = 20)
	

def volume_position_save():
	position = scale.get()
	data = {'vol_pos' : position}
	with open('settings.txt','w') as settings_file:
		json.dump(data, settings_file)

def volume_position_load():
	with open('settings.txt') as settings_file:
		data = json.load(settings_file)
		position = data.get('vol_pos')
		scale.set(position)

def TTS_convert():
	TTS_TEXT = TTS_entry.get()
	Engine.say(TTS_TEXT)
	Engine.runAndWait()

def volume_set():
	with open('settings.txt') as settings_file:
		data2 = json.load(settings_file)
		decibals = data2.get('vol_pos')
		
		Engine.setProperty('volume',decibals/10)

def lambda_func():
	volume_position_save()
	volume_set()
		









# Header
title_label = tk.Label(master = window, text = 'SignoGlove', font = ('SegoeUI 24 bold italic',20,'italic','bold'))
title_label.pack(side = 'top', anchor = 'n')

# Buttons
#vaolume = scale.get()
#input_frame = tk.Frame(master = window)
#input_frame.configure(bg = 'blue')
Bck = tk.Button(window,text = 'Back', command = Back )
Back_2 = tk.Button(window,text = 'Back', command = Bck_2 )
Say = tk.Button(window,text = 'Say', command = TTS_convert )

TTS_entry = tk.Entry(window, font =('Arial',20))
Bck.configure(height=5,width=20)
Edit_audio = tk.Button(window,text = 'Edit audio profile', command = Edit_TTS_Profile, image= Edit_audio_Btton, compound = 'top', font= ('Comic Sans' , 20))
Edit_audio.pack(pady = 50)

TTS = tk.Button(window,text = 'Text to speech', image= TTT_Button, compound = 'top', font= ('Comic Sans' , 20), command = TTS)

TTS.pack(pady = 20)

scale.bind('<Motion>', lambda event: lambda_func())

volume_position_load()

Engine = pyttsx3.init()

#input_frame.pack()

#if Edit_audio 

#run
window.mainloop()
