from tkinter import Tk, Label, Entry, Button, Listbox, BROWSE, Button, StringVar, ANCHOR, messagebox
from YTload import show_options

class App(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Youtube mp4 videos downloader")
        self.window.geometry("800x600+40+40")
        self.createWidgets()

        self.window.mainloop()

    def createWidgets(self):
        self.label = Label(text="Wklej link:", anchor = "w", bg = "red")
        self.label.place(relx = 0.01, rely = 0.01, relwidth = 0.18)

        self.textbox = Entry()
        self.textbox.place(relx = 0.2, rely = 0.01, relwidth = 0.4)
        
        self.button = Button(text="Pokaż", command = self.button_click)
        self.button.place(relx = 0.61, rely = 0.01)

        self.listbox = Listbox(selectmode = BROWSE)
        self.listbox.place(relx = 0.01, rely = 0.06, relwidth = 0.98, relheight = 0.4)

        self.button2 = Button(text="Pobierz", command = self.download)
        self.button2.place(relx = 0.01, rely = 0.5)

        self.text = StringVar()
        self.text.set("Status")

        self.label2 = Label(textvariable = self.text, anchor = "w")
        self.label2.place(relx = 0.01, rely = 0.6, relwidth = 0.18)

    def button_click(self):
        try:
            self.lista = show_options(self.textbox.get())
            self.listbox.insert(0, *self.lista)
            self.text.set("Podano dostępne opcje")
        except:
            messagebox.showinfo("Błąd", "Prawdopodobnie brak dostępu do internetu")

    def download(self):
        try:
            self.text.set("Trwa pobieranie")  # nie działa
            stream = self.listbox.get(ANCHOR)

            for item in self.lista:
                if(stream == str(item)):
                    item.download()
            
            self.text.set("Pobrano film")
        except:
            messagebox.showinfo("Błąd", "Nie można pobrać pliku")

app = App()