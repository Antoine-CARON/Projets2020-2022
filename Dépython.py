from random import *
from tkinter import*


def NouveauLance():
    nb=randint(1,6)
    img = PhotoImage(file="fondecranblanc.png")
    MafenetreLabel = Label(Mafenetre, image = img).grid(row=1,column=1)
    del(img)
    if nb==1:
         img = PhotoImage(file="de_1.png")
         MafenetreLabel = Label(Mafenetre, image = img).grid(row=1,column=1)
         Mafenetre.mainloop()
    elif nb==2:
         img = PhotoImage(file="de_2.png")
         MafenetreLabel = Label(Mafenetre, image = img).grid(row=1,column=1)
         Mafenetre.mainloop()
    elif nb==3:
         img = PhotoImage(file="de_3.png")
         MafenetreLabel = Label(Mafenetre, image = img).grid(row=1,column=1)
         Mafenetre.mainloop()
    elif nb==4:
         img = PhotoImage(file="de_4.png")
         MafenetreLabel = Label(Mafenetre, image = img).grid(row=1,column=1)
         Mafenetre.mainloop()
    elif nb==5:
         img = PhotoImage(file="de_5.png")
         MafenetreLabel = Label(Mafenetre, image = img).grid(row=1,column=1)
         Mafenetre.mainloop()
    elif nb==6:
         img = PhotoImage(file="de_6.png")
         MafenetreLabel = Label(Mafenetre, image = img).grid(row=1,column=1)
         Mafenetre.mainloop()

Mafenetre = Tk()
Mafenetre.title('Dé à 6 faces')


BoutonLancer = Button(Mafenetre, text ='Lancer', command=NouveauLance)
BoutonLancer.grid(row=2, column = 0, padx = 5, pady = 5)

BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.grid(row=2, column = 1, padx = 5, pady = 5)

NouveauLance()