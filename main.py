import tkinter as tk
from tkinter import *
from tkinter import ttk
from genderqr import *
from search import choiceqr
from time import strftime
from tkcalendar import DateEntry
TypeOption = ['Selezionare un opzione','wifi','calendario','link','telefono','mail-to']

def wifiTypeQr(gui):
    encriptionOption = ['Selezionare un opzione','no','WPA','WPE']
    HiddenOpuion = ['Selezionare un opzione','true','false']
    variabilone = tk.StringVar(root)
    variabilina = tk.StringVar(root)
    #gui of wifi
    gui.append(ttk.Label(text="SSID"))
    gui.append(ttk.Entry())
    gui.append(ttk.Label(text="PASSWORD"))
    gui.append(ttk.Entry())
    gui.append(ttk.Label(text="Tipo crittologia"))
    gui.append(ttk.OptionMenu(root, variabilone, *encriptionOption))
    gui.append(ttk.Label(text="Rete nascosta?"))
    gui.append(ttk.OptionMenu(root, variabilina, *HiddenOpuion))
    gui.append(ttk.Label(text="Nome file"))
    gui.append(ttk.Entry())
    gui.append(ttk.Button(text="Genera", command= lambda: wifiG(gui[1].get(), gui[3].get(), variabilone.get(), variabilina.get(), gui[9].get()), width=15))
    #grid
    gui[0].grid(column=0, row=0, pady=10, padx=10)
    gui[1].grid(column=1, row=0, pady=10, padx=10)
    gui[2].grid(column=0, row=1, pady=10, padx=10)
    gui[3].grid(column=1, row=1, pady=10, padx=10)
    gui[4].grid(column=0, row=2, pady=10, padx=10)
    gui[5].grid(column=1, row=2, pady=10, padx=10)
    gui[6].grid(column=0, row=3, pady=10, padx=10)
    gui[7].grid(column=1, row=3, pady=10, padx=10)
    gui[8].grid(column=0, row=4, pady=10, padx=10)
    gui[9].grid(column=1, row=4, pady=10, padx=10)
    gui[10].grid(column=0, columnspan=2, row=5,  pady=10, padx=10)


def calendarTypeQr(gui,root):
    hs=f"""{strftime('%H')}"""
    hf=f"""{int(strftime('%H'))+1}"""
    m=f"""{strftime('%M')}"""
    s=f"""{strftime('%S')}"""
    #gui of calendar
    gui.append(ttk.Label(text="Nome evento: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Label(text="Luogo evento: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Label(text="Data di inzio: "))
    gui.append(DateEntry(root, selectmode='day', date_pattern='dd/MM/yyyy'))#date start
    gui.append(ttk.Label(text="Ora di inzio [h:m:s]"))
    gui.append(ttk.Spinbox(root, from_=00, to=23, format="%02.0f", width=2, justify=CENTER)) #hour
    gui.append(ttk.Spinbox(root, from_=00, to=59, format="%02.0f", width=2, justify=CENTER))#minute
    gui.append(ttk.Spinbox(root, from_=00, to=59, format="%02.0f", width=2, justify=CENTER))#second
    gui.append(ttk.Label(text="Data di fine: "))
    gui.append(DateEntry(root,selectmode='day',date_pattern='dd/MM/yyyy'))#date end
    gui.append(ttk.Label(text="Ora di fine [h:m:s]"))
    gui.append(ttk.Spinbox(root, from_=00, to=23, format="%02.0f", wrap=True, width=2, justify=CENTER)) #hour
    gui.append(ttk.Spinbox(root, from_=00, to=59, format="%02.0f", wrap=True, width=2, justify=CENTER))#minute
    gui.append(ttk.Spinbox(root, from_=00, to=59, format="%02.0f", wrap=True, width=2, justify=CENTER))#second
    gui.append(ttk.Label(text="Nome file: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Button(text="Genera", command= lambda: calendarG(gui[1].get(), gui[3].get(), gui[5].get_date().strftime("%d"), gui[5].get_date().strftime("%m"), gui[5].get_date().strftime("%Y"), gui[7].get(), gui[8].get(), gui[9].get(), gui[11].get_date().strftime("%d"), gui[11].get_date().strftime("%m"), gui[11].get_date().strftime("%Y"), gui[13].get(), gui[14].get(), gui[15].get(), gui[17].get())))
    gui[0].grid(column=0, row=0, pady=10, padx=10)#nome evento
    gui[1].grid(column=1, columnspan=3, row=0, pady=10, padx=10)#nome evento      Enrey
    gui[2].grid(column=0, row=1, pady=10, padx=10)#luogo evento
    gui[3].grid(column=1, columnspan=3, row=1, pady=10, padx=10)#luogo evento     Entry
    #data inizio
    gui[4].grid(column=0, row=2, pady=10, padx=10)#data inizio
    gui[5].grid(column=1, columnspan=3, row=2, pady=10, padx=10)#data inizio      Calendar
    #ora inizio
    gui[6].grid(column=0, row=3, pady=10, padx=10)#ora inizio
    gui[7].grid(column=1, row=3, pady=10, ipadx=5)#ora inizio       H
    gui[7].insert(tk.END,hs)
    gui[7].configure(state='readonly')
    gui[8].grid(column=2, row=3, pady=10, ipadx=5)#ora inizio       M
    gui[8].insert(tk.END,m)
    gui[8].configure(state='readonly')
    gui[9].grid(column=3, row=3, pady=10, ipadx=5)#ora inizio       S
    gui[9].insert(tk.END,s)
    gui[9].configure(state='readonly')
    #data fine
    gui[10].grid(column=0, row=4, pady=10, padx=10)#data fine
    gui[11].grid(column=1, columnspan=3, row=4, pady=10, padx=10)#data fine        Calendar
    #ora fine
    gui[12].grid(column=0, row=5, pady=10, padx=10)#ora fine
    gui[13].grid(column=1, row=5, pady=10, ipadx=5)#ora fine         H
    gui[13].insert(tk.END,hf)
    gui[13].configure(state='readonly')
    gui[14].grid(column=2, row=5, pady=10, ipadx=5)#ora fine         M
    gui[14].insert(tk.END,m)
    gui[14].configure(state='readonly')
    gui[15].grid(column=3, row=5, pady=10, ipadx=5)#ora fine         S
    gui[15].insert(tk.END,s)
    gui[15].configure(state='readonly')
    #image
    gui[16].grid(column=0, row=6, pady=10, padx=10)#name img
    gui[17].grid(column=1, columnspan=3, row=6,  pady=10, padx=10)#nameimg Entry
    gui[18].grid(column=1, columnspan=3, row=7,  pady=10, padx=10)#invio

def urlTypeQr(gui):
    gui.append(ttk.Label(text="Url: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Label(text="Nome file: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Button(text="Genera", command= lambda: urlG(gui[1].get(),gui[3].get() )))
    gui[0].grid(column=0, row=0, pady=10, padx=10)
    gui[1].grid(column=1, row=0, pady=10, padx=10)
    gui[2].grid(column=0, row=1, pady=10, padx=10)
    gui[3].grid(column=1, row=1, pady=10, padx=10)
    gui[4].grid(column=1, row=2, pady=10, padx=10)


def telTypeQr(gui):
    gui.append(ttk.Label(text="Prefisso: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Label(text="Numero: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Label(text="Nome file: "))
    gui.append(ttk.Entry())
    gui.append(ttk.Button(text="Genera", command= lambda: telG(gui[1].get(),gui[3].get(),gui[5].get() )))
    gui[0].grid(column=0, row=0, pady=10, padx=10)
    gui[1].grid(column=1, row=0, pady=10, padx=10)
    gui[2].grid(column=0, row=1, pady=10, padx=10)
    gui[3].grid(column=1, row=1, pady=10, padx=10)
    gui[4].grid(column=0, row=2, pady=10, padx=10)
    gui[5].grid(column=1, row=2, pady=10, padx=10)
    gui[6].grid(column=1, row=3, pady=10, padx=10)

def MailtoTypeQr(gui,master):
    fact = """..."""
    gui.append(ttk.Label(text="A: "))#0
    gui.append(ttk.Entry(width=30))
    gui.append(ttk.Label(text="Soggetto: "))#1
    gui.append(ttk.Entry(width=30))
    gui.append(ttk.Label(text="Testo: "))#2
    gui.append(tk.Text(master=master, width=45, height=10))
    gui.append(ttk.Label(text="Nome file: "))#3
    gui.append(ttk.Entry())
    gui.append(ttk.Button(text="Genera", command= lambda: mailG(gui[1].get(), gui[3].get(), gui[5].get())))#4
    gui[0].grid(column=0, row=0, pady=10, padx=10)
    gui[1].grid(column=1, row=0, pady=10, padx=10)
    gui[2].grid(column=0, row=1, pady=10, padx=10)
    gui[3].grid(column=1, row=1, pady=10, padx=10)
    gui[4].grid(column=0, row=2, pady=10, padx=10)
    gui[5].grid(column=1, row=2, pady=10, padx=10)
    gui[5].insert(tk.END, fact)
    gui[6].grid(column=0, row=3, pady=10, padx=10)
    gui[7].grid(column=1, row=3, pady=10, padx=10)
    gui[8].grid(column=1, row=4, pady=10, padx=10)

def typeSelected(variabil, gui, root):
    #scomposizione iniziale
    choice = variabil.get()
    if "calendario" or "wifi" or "link" or "telefono" or "mail-to" in choice:
        for element in gui:#distrugge gli elementi e licancella dalla lista
            element.destroy()
        gui.clear()

        if choice == "calendario":
            calendarTypeQr(gui,root)
        elif choice == "wifi":
            wifiTypeQr(gui)
        elif choice == "link":
            urlTypeQr(gui)
        elif choice == "telefono":
            telTypeQr(gui)
        elif choice == "mail-to":
            MailtoTypeQr(gui,root)


def second(gui,root):
    # scanziona
    for element in gui:
        element.destroy()
    gui.clear()
    data = choiceqr() #return a list
    prdata = f"""{data[1]}"""
    ttk.Label(root, text=f"{data[0]}:").grid(column=0, row=0, pady=10, padx=10)
    output = tk.Text(master=root, width=55, height=10)
    output.insert(tk.END, prdata)
    output.configure(state='disabled')
    output.grid(column=0, row=1, pady=10, padx=10)



root = tk.Tk()
#variabile per prendere il dato da menu
variabil = tk.StringVar(root)
#variabil.set("Selezionare un opzione")#da dove incomincia a partire il menu
#gui
one_tab = []
root.title("scan & generate")
one_tab.append(ttk.Label(root,text="Scegli"))
one_tab.append(ttk.Button(text="scan", command=lambda: second(one_tab,root), width=15))
one_tab.append(ttk.OptionMenu(root, variabil, *TypeOption))
one_tab.append(ttk.Button(text="Invio Scelta", command= lambda: typeSelected(variabil, one_tab,root), width=15))
one_tab[0].grid(column=0,columnspan= 2, row=0, pady=10)
one_tab[1].grid(column=0, row=1, ipadx=3, padx=20, pady=10)
one_tab[2].grid(column=1, row=1, ipadx=3, padx=20, pady=10)
one_tab[3].grid(column=1, row=2, ipadx=8, padx=20, pady=15)
root.mainloop()
