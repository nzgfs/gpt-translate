import openai

from tkinter import *
from tkinter.filedialog import askdirectory
import os
import threading
import time
import tkinter
import tkinter.font as tkFont

window=Tk()
window.title("gpt translate")
window.geometry("550x375")


origin=Text(window,width=49)
origin.grid(column=1,row=0)
origin.place(x=30,y=20,height=100)
fontExample = tkFont.Font(family="Microsoft YaHei", size=13, weight="normal")
origin.configure(font=fontExample)

target=Text(window,width=49)
target.grid(column=1,row=1)
target.place(x=30,y=200,height=100)
target.configure(font=fontExample)


def clicked():
    message=origin.get("0.0","end")

    openai.api_key = 'YOUR_API_KEY'
    messages = []
    messages.append({"role": "system", "content": "translator"})
    
    messages.append({"role": "user", "content": 'Translate the following English text to Chinese: '+ message})
    response = openai. ChatCompletion. create(
        model="gpt-3.5-turbo", 
        messages=messages)
    reply = response ["choices"] [0] ["message"] ["content"]
    messages. append ({"role": "assistant", "content": reply})
    target.delete("1.0","end")
    target.insert("end",reply)


btn=Button(window,text="translate",command=clicked)
btn.grid(column=0,row=3)
btn.place(x=230,y=150,height=30)

window.mainloop()

