from typing import Tuple
import customtkinter as ctk 
import tkinter as tk 
from tkinter import *
import os 
from PIL import Image, ImageDraw, ImageTk


# Variaveis Globais. 

global DIRECTORY_ASSESTS
global CURRENT_PATH
global ICON_DIR
global ICON_PATH

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
DIRECTORY_ASSESTS = os.path.join(CURRENT_PATH,'assets')
ICON_DIR = os.path.join(DIRECTORY_ASSESTS,'imagens', "icons")

ICON_PATH = {
    "close": (os.path.join(ICON_DIR, "close_black.png"), os.path.join(ICON_DIR, "close_white.png")),
    "images": list(os.path.join(ICON_DIR, f"image{i}.jpg") for i in range(1, 4)),
    "eye1": (os.path.join(ICON_DIR, "eye1_black.png"), os.path.join(ICON_DIR, "eye1_white.png")),
    "eye2": (os.path.join(ICON_DIR, "eye2_black.png"), os.path.join(ICON_DIR, "eye2_white.png")),
    "info": os.path.join(ICON_DIR, "info.png"),
    "warning": os.path.join(ICON_DIR, "warning.png"),
    "error": os.path.join(ICON_DIR, "error.png"),
    "left": os.path.join(ICON_DIR, "left.png"),
    "right": os.path.join(ICON_DIR, "right.png"),
    "warning2": os.path.join(ICON_DIR, "warning2.png"),
    "loader": os.path.join(ICON_DIR, "loader.gif"),
    "icon": os.path.join(ICON_DIR, "icon.png"),
    "arrow": os.path.join(ICON_DIR, "arrow.png"),
    "image": os.path.join(ICON_DIR, "image.png"),
}


class EntryPassword(ctk.CTkEntry):
    def __init__(self, master: any, icon_width=20, icon_height=15, **kwargs):
        super().__init__(master, **kwargs)

        self.icon_width = icon_width
        self.icon_height = icon_height

        self.is_hidden = False
        self.eye_btn = None

        self.warning = ctk.CTkImage(Image.open(ICON_PATH["warning2"]), Image.open(ICON_PATH["warning2"]),
                                    (self.icon_width, self.icon_height))
        self.eye1 = ctk.CTkImage(Image.open(ICON_PATH["eye1"][0]), Image.open(ICON_PATH["eye1"][1]),
                                 (self.icon_width, self.icon_height))
        self.eye2 = ctk.CTkImage(Image.open(ICON_PATH["eye2"][0]), Image.open(ICON_PATH["eye2"][1]),
                                 (self.icon_width, self.icon_height))

        self.button_bg = ctk.ThemeManager.theme["CTkEntry"]["fg_color"]
        self.border_color = ctk.ThemeManager.theme["CTkEntry"]["border_color"]

    def custom_input(self, icon_path, text=None, compound="right"):
        icon = ctk.CTkImage(Image.open(icon_path), Image.open(icon_path), (self.icon_width, self.icon_height))

        icon_label = ctk.CTkLabel(self, text=text if text else None, image=icon, width=self.icon_width,
                                  height=self.icon_height, compound=compound)
        icon_label.grid(row=0, column=0, padx=4, pady=0, sticky="e")

    def password_input(self):
        self.is_hidden = True
        self.configure(show="*")
        self.eye_btn = ctk.CTkButton(self, text="", width=self.icon_width, height=self.icon_height,
                                     fg_color=self.button_bg, hover=False, image=self.eye1,
                                     command=self.toggle_input)
        self.eye_btn.grid(row=0, column=0, padx=2, pady=0, sticky="e")

    def show_waring(self, border_color="red"):
        self.configure(border_color=border_color)
        icon_label = ctk.CTkLabel(self, text="", image=self.warning, width=self.icon_width, height=self.icon_height)
        icon_label.grid(row=0, column=0, padx=4, pady=0, sticky="e")

    def toggle_input(self):
        if self.is_hidden:
            self.is_hidden = False
            self.configure(show="")
            self.eye_btn.configure(image=self.eye2)
        else:
            self.is_hidden = True
            self.configure(show="*")
            self.eye_btn.configure(image=self.eye1)

    def reset_default(self):
        self.configure(border_color=self.border_color)
        self.configure(show="")
        self.is_hidden = False
        for widget in self.winfo_children():
            widget_name = widget.winfo_name()
            if widget_name.startswith("!ctklabel") or widget_name.startswith("!ctkbutton"):
                widget.destroy()




class AppLogin(ctk.CTkFrame):
    def __init__(self, master=None,width:int = 450):
        super().__init__(master)
        self.tela_login()
        self.master_frame = master
        
        
    def tela_login(self) :
        
        def click_login(event=None):
            
            if self.entry_user.get().strip() and self.entry_password.get().strip():
                
                print(f"Usuário = {self.entry_user.get()}\n Senha = {self.entry_password.get()}")
                self.entry_user.reset_default()
                self.entry_password.reset_default()
                self.entry_password.password_input()
                
            elif  not self.entry_user.get().strip() and not self.entry_password.get().strip() :
                print("Campo Usuário  e senha Vazio")
                self.entry_user.reset_default()
                self.entry_user.show_waring()
                self.entry_password.reset_default()
                self.entry_password.show_waring()
                
            elif  not self.entry_user.get().strip():
                print("Campo usuario  Vazio")
                self.entry_user.reset_default()
                self.entry_user.show_waring()
                
                self.entry_password.reset_default()
                self.entry_password.password_input()
                
            elif  not self.entry_password.get().strip():
                print("Campo senha  Vazio")
                
                self.entry_user.reset_default()
                self.entry_password.reset_default()
                self.entry_password.show_waring()
                self.entry_password.configure(show='*')
                
            else: 
                print("Campos Vazios")
            pass
        
        def verifica_user(user,password):
            
        
            
            
            pass
        
        self.label = ctk.CTkLabel(self,text="Bem Vindo ao My Finance", font=('Arial',20))
        self.label.place(x=10,y=2)
        
        self.label_user = ctk.CTkLabel(self,text="Usuário:", font=("Arial",12))
        self.entry_user = EntryPassword(self,width=320)
        
        self.label_password = ctk.CTkLabel(self,text="Senha:", font=("Arial",12))
        self.entry_password = EntryPassword(self,width=320,show ='*')
        self.entry_password.password_input()
        
        self.button_login = ctk.CTkButton(self, text="Login", command=click_login )
        
        self.button_register = ctk.CTkButton(self,width=10,hover=False, text="Registrar", fg_color='transparent', command= lambda e=None: AppRegister(self.master_frame).pack())
        
        self.label_user.place(x=5,y=60)
        self.entry_user.place(x=5,y=80)
        
        self.label_password.place(x=5,y=120)
        self.entry_password.place(x=5,y=140)
        
        self.button_login.place(x=5,y=170)
        self.button_register.place(x=200,y=170)
        
        
        
        
        
        
        
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
        self.resizable(False,False)
        
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