from tkinter import *

from tkinter import ttk

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

global name


def dash(i):
    for x in range(i):
        try:
            
                GPIO.output(18,GPIO.HIGH) ##switch LED button on
                time.sleep(0.9); ## dot is 1 unit 300 milliseconds & dash is 3 x = 900
                GPIO.output(18,GPIO.LOW) ##switch LED button off
                time.sleep(0.3);
        except KeyboardInterrupt:
            GPIO.cleanup()

def dot(i):
    for x in range(i):
        try:
                GPIO.output(18,GPIO.HIGH) ##switch LED button on
                time.sleep(0.3); ## dot is 1 unit 300 milliseconds & dash is 3 x = 900
                GPIO.output(18,GPIO.LOW) ##switch LED button off
                time.sleep(0.3);
        except KeyboardInterrupt:
            GPIO.cleanup()
            
def a():
    dot(1);
    dash(1);

def b():
    dash(1);
    dot(3);

def c():
    dash(1);
    dot(1);
    dash(1);
    dot(1);

def d():
    dash(1);
    dot(2);
    
def e():
    dot(1);
    
def f():
    dot(2);
    dash(1);
    dot(1);
    
def g():
    dash(2);
    dot(1);

def h():
    dot(4);
  
def i():
    dot(2);
    
def j():
    dot(1);
    dash(3);

def k():
    dash(1);
    dot(1);
    dash(1);

def l():
    dot(1);
    dash(1);
    dot(2);

def m():
    dash(2);
    
def n():
    dash(1);
    dot(1);

def o():
    dash(3);

def p():
    dot(1);
    dash(2);
    dot(1);
        
def q():
    dash(2);
    dot(1);
    dash(1);

def r():
    dot(1);
    dash(1);
    dot(1);

def s():
    dot(3);

def t():
    dash(1);

def u():
    dot(2);
    dash(1);

def v():
    dot(3);
    dash(1);

def w():
    dot(1);
    dash(2);

def x():
    dash(1);
    dot(2);
    dash(1);

def y():
    dash(1);
    dot(1);
    dash(2);

def z():
    dash(2);
    dot(2);


   
def exit_app():
    GPIO.output(18,GPIO.LOW) #red off
    win.hide()



def run_morse():
    word="a"
    word=getInput()
    l=len(word);
    print(word);
    word=word.lower();
    for x in word:
        if ord(x) == 97:
            a();
        elif ord(x) == 98:
            b();
        elif ord(x) == 99:
            c();
        elif ord(x) == 100:
            d();
        elif ord(x) == 101:
            e();
        elif ord(x) == 102:
            f();
        elif ord(x) == 103:
            g();
        elif ord(x) == 104:
            h();
        elif ord(x) == 105:
            i();
        elif ord(x) == 106:
            j();
        elif ord(x) == 107:
            k();
        elif ord(x) == 108:
            l();
        elif ord(x) == 109:
            m();
        elif ord(x) == 110:
            n();
        elif ord(x) == 111:
            o();
        elif ord(x) == 112:
            p();
        elif ord(x) == 113:
            q();
        elif ord(x) == 114:
            r();
        elif ord(x) == 115:
            s();
        elif ord(x) == 116:
            t();
        elif ord(x) == 117:
            u();
        elif ord(x) == 118:
            v();
        elif ord(x) == 119:
            w();
        elif ord(x) == 120:
            x();
        elif ord(x) == 121:
            y();
        elif ord(x) == 122:
            z();
        
            
def getInput():
    word="a"
    word=wordentry.get()
    return word
     
##def init(win):
    ##win.title("Morse Code Generator")
   ## win.minsize(500,100)
    ##word='a'
    
    ##wordentry=Text(win, height=1,width=25)
    
    
    ##btn=Button(win, text="Run morse", command=lambda: run_morse())
    ##btn2=Button(win, text="Exit", command=win.destroy)
    ##wordentry.pack()
    ##btn.pack()
    ##btn2.pack()
    
    

win=Tk()
win.title("Morse Code Generator")
win.minsize(500,100)
word = "a"
inputvar=StringVar()
wordentry=Entry(win, textvariable=inputvar)


btn=Button(win, text="Run morse", command=lambda: run_morse())
btn2=Button(win, text="Exit", command=win.destroy)
wordentry.pack()
btn.pack()
btn2.pack()


##init(win)
mainloop()