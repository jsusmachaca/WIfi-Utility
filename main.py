from tkinter import * 
import subprocess as sp
from time import sleep

class main:
        
    def __init__(self):
        self.root = Tk()
        self.myframe = Frame(self.root, bg="#4A4B5B" ,width="330", height="450")
        #self.myframe.pack()

    def final (self):
        self.root.mainloop()

    def properties(self):    
        self.root.title("Windows try")
        self.root.resizable(False, False)
        self.myframe.pack(fill="y", expand="True")
      
    
    def components(self, m, c):
        def labels():
            label = Label(
                self.myframe,
                text="Configuración de internet",
                fg="#ffffff", bg="#0f101a", font=("Ubuntu Nerd Font", 10), padx=130
                ).place(x=-120, y=0) 
        
            label2 = Label(
                self.myframe,
                text=c,
                fg="#ffffff",
                bg="#0f101a", 
                justify=CENTER, 
                font=("Ubuntu Nerd Font", 14), 
                padx=70, 
                pady=4).place(x=42, y=416)

            label3 = Label(
                self.myframe,
                text="NetWork ",
                fg="#0f101a",
                bg="#4A4B5B",
                font=("Ubuntu Nerd Font", 12)
            ).place(x=4, y=320)

            label4 = Label(
                self.myframe,
                text="Password ",
                fg="#0f101a",
                bg="#4A4B5B",
                font=("Ubuntu Nerd Font", 12)
            ).place(x=3, y=360)

        def lists():
            nombre=StringVar()
            listbox = Listbox(
                self.myframe,
                fg="#ffffff",
                bg="#0f101a", 
                font=("Ubuntu Nerd Font", 11), 
                width="30", 
                height="10"
                )
            listbox.insert(END, * (i for i in m.split("\n")))
            listbox.place(x=28, y=40)

            def textfields():
                
                def network(event):
                    list1 = []
                    try:
                        paswd = textfield1.get()
                        net = textfield.get()
                        a = sp.check_output(f"nmcli device wifi connect {net} password {paswd}", shell=True)
                        p = str(a)
                        list1.append(p.split(" "))
        
                        if ("correctamente" in list1[0]) == True:
                            sp.call("""notify-send "Conectado correctamente" """, shell=True)
                        else:
                            sp.call("""notify-send "Error al conectar" """, shell=True)
                    except Exception:
                        sp.call("""notify-send "No se pudo conectar" """, shell=True)

                
                textfield = Entry(self.myframe, font=("Ubuntu Nerd Font", 11))
                textfield.config(width=20)
                textfield.place(x=90, y=320)

                textfield1 = Entry(self.myframe, font=("Ubuntu Nerd Font", 11))
                textfield1.config(width=20, show="*")
                textfield1.place(x=90, y=360)
                
                textfield, textfield1.bind("<Return>", network)
            
            textfields()
            
        labels()
        lists()
        
    
    def wifi(self):
        sp.call("nmcli device wifi rescan", shell=True)
        runing = """nmcli device wifi list | sed 's/* //'  | awk '{print $2}' > /home/jisas/.config/wifilist.txt """
        a = sp.call(runing, shell=True)
        file = open("/home/jisas/.config//wifilist.txt", "r")
        r = file.read()
        return r

    def connect(self):
        runing = """nmcli | grep " conectado" | awk '{print " "$4}' > /home/jisas/.config/conection.txt """
        a = sp.call(runing, shell=True)
        file = open("/home/jisas/.config//conection.txt", "r")
        r = file.read()
        return r

if __name__ == "__main__":
    main = main()
    m = main.wifi()
    c = main.connect()
    main.properties()
    main.components(m, c)
    main.final()
