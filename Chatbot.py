# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:11:09 2018

@author: Rana Usama
"""


from chatterbot import ChatBot
import tkinter as tk
from chatterbot.trainers import ChatterBotCorpusTrainer
from PIL import Image, ImageTk
import pyttsx3
from pyswip import Prolog
pro = Prolog()
import speech_recognition as sr

pro.consult("File1.pl")

mybot=ChatBot("mybot")    # object of chatbot
mybot.set_trainer(ChatterBotCorpusTrainer)
mybot.train(
    "chatterbot.corpus.english.ai"

)
r = sr.Recognizer()            
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#second window
def open_window():
    #root.destroy()
    top = tk.Toplevel()
    top.title("top window")
    top.geometry("650x610")
    top.config(bg="lavender blush")
    scroll=tk.Scrollbar(top)
    scroll.pack(fill=tk.Y, side=tk.RIGHT)
    messages = tk.Text(top,wrap=tk.NONE,yscrollcommand=scroll.set)
    messages.pack(anchor=tk.NW)
    messages.config(bg="gray96")
    scroll.config(command=messages.yview)
    
   
   # var1= tk.StringVar()
    l=tk.Label(top, text="Input:")
    l.pack(anchor=tk.N, pady=5)
    l.config(bg="lavender blush")
    textbox = tk.Entry(top)
    textbox.pack(anchor=tk.N)
    
    b = tk.Button(top, text="get",command=lambda: callback())
    b.pack(anchor=tk.N)
    b.config(bg="lavender blush")
    iv=tk.IntVar()
    iv2=tk.IntVar()
    iv3=tk.IntVar()
    voiceCheck = tk.Checkbutton(top, text="voice input enable", variable=iv)
    voiceCheck.pack(anchor=tk.N,side=tk.TOP)
    voiceCheck.config(bg="lavender blush")
   
        
    
    infolabel=tk.Label(top, text="Information:")
    infolabel.pack(anchor=tk.W,side=tk.TOP)
    infolabel.config(bg="lavender blush")
    c = tk.Checkbutton(top, text="Student info",variable=iv2)
    c.pack(anchor=tk.W,side=tk.TOP)
    c.config(bg="lavender blush")
    c1 = tk.Checkbutton(top, text="Course info",variable=iv3)
    c1.pack(anchor=tk.W,side=tk.TOP)
    c1.config(bg="lavender blush")
    c2 = tk.Checkbutton(top, text="Free Chat")
    c2.pack(anchor=tk.W,side=tk.TOP)
    c2.config(bg="lavender blush")
    
    def callback():                                       # get button function
        ivc=iv.get()
        ivc2=iv2.get()
        if ivc == 1:                                        # Audio input check box
            messages.insert(tk.INSERT,"speak \n")
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                varS= r.recognize_google(audio)
                messages.insert(tk.INSERT,"You:")
                print(varS)
                messages.insert(tk.INSERT,'%s\n' % varS)
            except sr.UnknownValueError:
                messages.insert(tk.INSERT,"could not understand audio")
            except sr.RequestError as e:
                messages.insert(tk.INSERT,"could not understand audio")
                print(format(e))    
            reply = mybot.get_response(varS)
            print(reply)
            messages.insert(tk.INSERT,"Advia: ")
            messages.insert(tk.INSERT, '%s\n' % reply)
            engine.say(reply)
            engine.runAndWait()
        elif ivc2 == 1:                         #student info checkbox checked
            var=str(textbox.get())
            print (var)
            messages.insert(tk.INSERT,"You: ")
            messages.insert(tk.INSERT, '%s\n' % var)
            if var == "hi":
                for result in pro.query("give_reply(hi,Y)."):
                    v = list(result.values())
                    v1=v[0]
                    print(v1)
                messages.insert(tk.INSERT,"Advia: ")
                messages.insert(tk.INSERT, '%s\n' % v1)
                engine.say(v1)
                engine.runAndWait()
            elif var == "bye":
                for result in pro.query("give_reply(bye,Y)."):
                    v = list(result.values())
                    v1=v[0]
                    print(v1)
                messages.insert(tk.INSERT,"Advia: ")
                messages.insert(tk.INSERT, '%s\n' % v1)
                engine.say(v1)
                engine.runAndWait()
            elif var == "who are you":
                for result in pro.query("give_reply(who_are_you,Y)."):
                    v = list(result.values())
                    v1=v[0]
                    print(v1)
                messages.insert(tk.INSERT,"Advia: ")
                messages.insert(tk.INSERT, '%s\n' % v1)
                engine.say(v1)
                engine.runAndWait()
            elif var == "is ali student" or var == "student = ali":
                for result in pro.query("isstudent(ali)."):
                    if result == {}:
                        print("yes")
                    else:
                        print("no")
                messages.insert(tk.INSERT,"Advia: ")
                messages.insert(tk.INSERT, '%s\n' % v1)
                engine.say("yes")
                engine.runAndWait()
            
        else:                                             # for other check box
            var=str(textbox.get())
            #var=var2
            print (var)
            messages.insert(tk.INSERT,"You: ")
            messages.insert(tk.INSERT, '%s\n' % var)
            
            reply = mybot.get_response(var)             # give reply from chatterbot corpus YML files
            print(reply)
            messages.insert(tk.INSERT,"Advia: ")
            messages.insert(tk.INSERT, '%s\n' % reply)
            engine.say(reply)
            engine.runAndWait()
            #time.sleep(1)
        
       
    #close button
    button1 = tk.Button(top, text="close", command=lambda:top.destroy())
    button1.pack(anchor=tk.W,side=tk.BOTTOM)
    button1.config(bg="lavender blush")
     
    

# first window
root = tk.Tk()
root.config(bg="lavender blush")

bgphoto = ImageTk.PhotoImage(Image.open("chatbot.png"))
lbl = tk.Label(root, image=bgphoto)
lbl.pack()
lbl.config(bg="lavender blush")
l2=tk.Label(root,text="Virtual Student Advisor",fg="blue", bg="lavender blush")
l2.pack(anchor=tk.S,pady=10)


button = tk.Button(root, text="Start Chating", fg="blue",command=lambda:open_window())
button.pack(anchor=tk.S)
button.config(bg="lavender blush")

root.geometry("400x500")
root.mainloop()
#root.destroy()