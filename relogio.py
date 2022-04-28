from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file('digital-7.ttf')

#---------------------------------------------------------------------
cor1 = '#FFFFFF' #branco
cor2 = '#4F4F4F' #cinza
cor3 = '#000000' #preto
#---------------------------------------------------------------------

#fundo de tela
behind = cor3

#janela
wind = Tk()
wind.title('')
wind.geometry('420x200')
wind.resizable(width=FALSE, height=FALSE)
wind.configure(bg=cor3)
#---------------------------------------------------------------------
def relog():
    temp = datetime.now()
    hour = temp.strftime(' %H:%M:%S')
    day_week = temp.strftime('%A')
    day = temp.day
    month = temp.strftime('%b')
    year = temp.strftime('%Y')
    # ---------------------------------
    lab1.config(text=hour)
    lab1.after(200, relog)
    lab2.config(text=day_week + ' ' + str(day) + '/' + str(month) + '/' + str(year))

#--------------------------Label-------------------------------------------
lab1 = Label(wind, text='', font=('digital-7 100'), bg=behind, fg=cor2 )
lab1.grid(row=0, column=0, sticky=NW, padx=5)
lab2 = Label(wind, text='', font=('digital-7 18'), bg=behind, fg=cor2)
lab2.grid(row=1, column=0, sticky=NW, padx=5)
#---------------------------------------------------------------------

relog()
wind.mainloop()