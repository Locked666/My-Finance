from typing import Tuple
import customtkinter as ctk 
import tkinter as tk 
from tkinter import *
import os 

 

class AppLogin(ctk.CTkFrame):
    def __init__(self, master=None,width:int = 450):
        super().__init__(master)
        self.tela_login()
        self.master_frame = master
        
        
    def tela_login(self) :
        self.label = ctk.CTkLabel(self,text="Bem Vindo ao My Finance", font=('Arial',20))
        self.label.pack(side=TOP)
        
        self.label_user = ctk.CTkLabel(self,text="Usuário:", font=("Arial",12))
        self.entry_user = ctk.CTkEntry(self,width=200)
        
        self.label_password = ctk.CTkLabel(self,text="Senha:", font=("Arial",12))
        self.entry_password = ctk.CTkEntry(self,width=200,show ='*')
        
        self.button_login = ctk.CTkButton(self, text="Login", command= lambda e=None: print(f"Usuário = {self.entry_user.get()}\n Senha = {self.entry_password.get()}"))
        
        self.button_register = ctk.CTkButton(self, text="Registrar", fg_color='transparent', command= lambda e=None: AppRegister(self.master_frame))
        
        self.label_user.pack()
        self.entry_user.pack()
        
        self.label_password.pack()
        self.entry_password.pack()
        
        self.button_login.pack()
        self.button_register.pack()
        
        
        
        
        
        pass 
    
    def widget_login(self):
        
        
        pass  
 

class AppRegister(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        
    def tela_register(self):
        label = ctk.CTkLabel(self,text="teste register")
        label.pack()
        pass     
    
    pass

class AppMain(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.tela_main()
        self.widgets_tela_main()
    
    def tela_main(self):
        self.geometry("900x600")
        self.title("My Finance")
        
    def widgets_tela_main(self):
        qt_users = 1
        frame_login = None
        frame_register = None
        self.frame_left = ctk.CTkFrame(self,width=450)
        self.frame_left.pack(side=LEFT,fill=BOTH,expand=TRUE)
        
        self.frame_rigth =  ctk.CTkFrame(self,width=450)
        self.frame_rigth.pack(side=RIGHT,fill=BOTH,expand=TRUE)
        
        
        if qt_users > 0:
            frame_login = AppLogin(self.frame_rigth)
            frame_login.pack(fill=BOTH, expand=True)
            
            
            

if __name__=='__main__':
    root = AppMain()
    root.mainloop()