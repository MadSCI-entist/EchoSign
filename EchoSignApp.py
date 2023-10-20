import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()		
window.title('SignoGlove')
window.geometry('700x800')
window.configure(bg='blue')

def Edit_TTS_Profile():
	Edit_audio.pack_forget()
	TTS.pack_forget()
	title_label.pack_forget()
	scale.pack()
	

	
    
	
	
	Back.pack()
    

	
	



def Back():
    scale.pack_forget()
    Back.pack_forget()
    Edit_audio.configure(height= 5, width=20)
    TTS.configure(height= 5, width=20)
    Edit_audio.pack(side = 'left',pady = 350)
    TTS.pack(side = 'left',pady = 350)





     



# Header
title_label = tk.Label(master = window, text = 'SignoGlove', font = 'SegoeUI 24 bold italic', bg = 'blue')
title_label.pack()

# Buttons

input_frame = tk.Frame(master = window)
input_frame.configure(bg = 'blue')
Back = tk.Button(input_frame,text = 'Back', command = Back )
scale = tk.Scale(input_frame,from_ = 0,to = 100, orient = 'horizontal', label = 'Volume', length = 200, width = 20, font = ('Consolas', 15 ) )
Back.configure(height=5,width=20)
Edit_audio = tk.Button(input_frame,text = 'Edit audio profile', command = Edit_TTS_Profile )
Edit_audio.configure(height= 5, width=20)
Edit_audio.pack(side = 'left',pady = 350)
TTS = tk.Button(input_frame,text = 'Text to speech')
TTS.configure(height= 5, width=20)
TTS.pack(side = 'left',pady = 350)

input_frame.pack()

#if Edit_audio 


	
#run
window.mainloop()
