# Importing the libraries
from tkinter import *
import pygame

# initializing the pygame
pygame.init()
root = Tk()

# Setting the title and geometry
root.title("PyTunes")
root.geometry("1300x670")
root.configure(background="white")

# creating the Frames
abc = Frame(root, bg="powder blue", bd=20, relief=RIDGE)
abc.grid()
abc1 = Frame(abc, bg="powder blue", bd=20, relief=RIDGE)
abc1.grid()
abc2 = Frame(abc, bg="powder blue", relief=RIDGE)
abc2.grid()
abc3 = Frame(abc, bg="powder blue", relief=RIDGE)
abc3.grid()

str = StringVar()
str.set("Play Music that u like")

#Functions for sound
def value_Cs():
    str.set("C")
    sound = pygame.mixer.Sound("key19.mp3")
    sound.play()


def value_A():
    str.set("A")
    sound = pygame.mixer.Sound("key02.mp3")
    sound.play()

def value_B():
    str.set("B")
    sound = pygame.mixer.Sound("key03.mp3")
    sound.play()

def value_C():
    str.set("C")
    sound = pygame.mixer.Sound("key04.mp3")
    sound.play()

def value_Bb():
    str.set("Bb")
    sound = pygame.mixer.Sound("key05.mp3")
    sound.play()

def value_Gs():
    str.set("G#")
    sound = pygame.mixer.Sound("key06.mp3")
    sound.play()

def value_Gs1():
    str.set("G#1")
    sound = pygame.mixer.Sound("key23.mp3")
    sound.play()

def value_Fs1():
    str.set("F#1")
    sound = pygame.mixer.Sound("key16.mp3")
    sound.play()

def value_Bb1():
    str.set("Bb1")
    sound = pygame.mixer.Sound("key19.mp3")
    sound.play()

def value_Ds():
    str.set("D#")
    sound = pygame.mixer.Sound("key07.mp3")
    sound.play()

def value_Fs():
    str.set("F#")
    sound = pygame.mixer.Sound("key08.mp3")
    sound.play()

def value_G():
    str.set("G")
    sound = pygame.mixer.Sound("key09.mp3")
    sound.play()

def value_D():
    str.set("D")
    sound = pygame.mixer.Sound("key10.mp3")
    sound.play()

def value_E1():
    str.set("E1")
    sound = pygame.mixer.Sound("key11.mp3")
    sound.play()

def value_E():
    str.set("E")
    sound = pygame.mixer.Sound("key12.mp3")
    sound.play()

def value_F():
    str.set("F")
    sound = pygame.mixer.Sound("key13.mp3")
    sound.play()

def value_F1():
    str.set("F1")
    sound = pygame.mixer.Sound("key14.mp3")
    sound.play()

def value_C1():
    str.set("C1")
    sound = pygame.mixer.Sound("key15.mp3")
    sound.play()

def value_D1():
    str.set("D1")
    sound = pygame.mixer.Sound("key16.mp3")
    sound.play()

def value_Cs1():
    str.set("C#1")
    sound = pygame.mixer.Sound("key17.mp3")
    sound.play()

def value_Ds1():
    str.set("C#1")
    sound = pygame.mixer.Sound("key18.mp3")
    sound.play()
def value_G1():
    str.set("G1")
    sound = pygame.mixer.Sound("key20.mp3")
    sound.play()
def value_A1():
    str.set("A1")
    sound = pygame.mixer.Sound("key21.mp3")
    sound.play()
def value_B1():
    str.set("B1")
    sound = pygame.mixer.Sound("key22.mp3")
    sound.play()

# Label
Label(abc1, text="PyTunes", font=("arial", 25, "bold"), padx=8, pady=8, bd=4, width=59, bg="powder blue",
      fg="black", height=1,
      justify=CENTER).grid(row=0, column=0, columnspan=11)

display = Entry(abc1, textvariable=str, font=("arial", 18, "bold"), width=35, bd=34, bg="white", fg="black",
                justify=CENTER).grid(row=1, column=5, pady=1)

# Buttons for keynotes
btnCs = Button(abc2, height=6, width=4, bd=4, text="C#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Cs)
btnCs.grid(row=0, column=0, padx=5, pady=5)
btnDs = Button(abc2, height=6, width=4, bd=4, text="D#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Ds)
btnDs.grid(row=0, column=1, padx=5, pady=5)

btnSpace1 = Button(abc2, state=DISABLED, height=6, width=2, bg="powder blue", relief=FLAT)
btnSpace1.grid(row=0, column=3, padx=0, pady=0)

btnFs = Button(abc2, height=6, width=4, bd=4, text="F#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Fs)
btnFs.grid(row=0, column=4, padx=5, pady=5)
btnGs = Button(abc2, height=6, width=4, bd=4, text="G#", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Gs)
btnGs.grid(row=0, column=6, padx=5, pady=5)
btnBb = Button(abc2, height=6, width=4, bd=4, text="Bb", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Bb)
btnBb.grid(row=0, column=8, padx=5, pady=5)

btnSpace5 = Button(abc2, state=DISABLED, height=6, width=2, bg="powder blue", relief=FLAT)
btnSpace5.grid(row=0, column=9, padx=0, pady=0)

btnCs1 = Button(abc2, height=6, width=4, bd=4, text="C#1", font=("arial", 18, "bold"), bg="black", fg="white",
                command=value_Cs1)
btnCs1.grid(row=0, column=10, padx=5, pady=5)
btnDs1 = Button(abc2, height=6, width=4, bd=4, text="D#1", font=("arial", 18, "bold"), bg="black", fg="white",
                command=value_Ds1)
btnDs1.grid(row=0, column=12, padx=5, pady=5)
btnSpace7 = Button(abc2, state=DISABLED, height=6, width=2, bg="powder blue", relief=FLAT)
btnSpace7.grid(row=0, column=13, padx=0, pady=0)

btnFs1 = Button(abc2, height=6, width=4, bd=4, text="F#1", font=("arial", 18, "bold"), bg="black", fg="white",
                command=value_Fs1)
btnFs1.grid(row=0, column=15, padx=5, pady=5)
btnGs1 = Button(abc2, height=6, width=4, bd=4, text="G#1", font=("arial", 18, "bold"), bg="black", fg="white",
                command=value_Gs1)
btnGs1.grid(row=0, column=17, padx=5, pady=5)
btnBb1 = Button(abc2, height=6, width=4, bd=4, text="Bb1", font=("arial", 18, "bold"), bg="black", fg="white",
               command=value_Bb1)
btnBb1.grid(row=0, column=19, padx=5, pady=5)


btnC = Button(abc3, bd=4, width=4, height=6, text="C", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_C)
btnC.grid(row=0, column=0, padx=5, pady=5)
btnD = Button(abc3, bd=4, width=4, height=6, text="D", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_D)
btnD.grid(row=0, column=1, padx=5, pady=5)
btnE = Button(abc3, bd=4, width=4, height=6, text="E", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_E)
btnE.grid(row=0, column=2, padx=5, pady=5)
btnF = Button(abc3, bd=4, width=4, height=6, text="F", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_F)
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(abc3, bd=4, width=4, height=6, text="G", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_G)
btnG.grid(row=0, column=4, padx=5, pady=5)
btnA = Button(abc3, bd=4, width=4, height=6, text="A", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_A)
btnA.grid(row=0, column=5, padx=5, pady=5)
btnB = Button(abc3, bd=4, width=4, height=6, text="B", bg="white", fg="black", font=("arial", 18, "bold"),
              command=value_B)
btnB.grid(row=0, column=6, padx=5, pady=5)
btnC1 = Button(abc3, bd=4, width=4, height=6, text="C1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_C1)
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(abc3, bd=4, width=4, height=6, text="D1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_D1)
btnD1.grid(row=0, column=8, padx=5, pady=5)
btnE1 = Button(abc3, bd=4, width=4, height=6, text="E1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_E1)
btnE1.grid(row=0, column=9, padx=5, pady=5)
btnF1 = Button(abc3, bd=4, width=4, height=6, text="F1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_F1)
btnF1.grid(row=0, column=10, padx=5, pady=5)
btnG1 = Button(abc3, bd=4, width=4, height=6, text="G1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_G1)
btnG1.grid(row=0, column=11, padx=5, pady=5)
btnA1 = Button(abc3, bd=4, width=4, height=6, text="A1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_A1)
btnA1.grid(row=0, column=12, padx=5, pady=5)
btnB1 = Button(abc3, bd=4, width=4, height=6, text="B1", bg="white", fg="black", font=("arial", 18, "bold"),
               command=value_B1)
btnB1.grid(row=0, column=13, padx=5, pady=5)

# Mainloop
root.mainloop()
