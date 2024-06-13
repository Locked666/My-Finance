from typing import Tuple
import customtkinter as ctk 
import tkinter as tk 
from tkinter import *
import os 
from pathlib import Path
from src.config_app import APP_CONFIG_NAME, AUTH_USER_SAVE, AUTH_USER_PASS_SAVE
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageDraw, ImageTk
from src import models

# Variaveis Globais.
global DIRECTORY_ASSESTS
global CURRENT_PATH
global ICON_DIR
global ICON_PATH


global USER_TEST
global USER_PASSWORD_TEST 



USER_TEST =  "juliosales"
USER_PASSWORD_TEST = "juliolindo"


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
        
        def show_warning(menssagem:str):
            # Show some retry/cancel warnings
            msg = CTkMessagebox(title="Warning Message!", message=menssagem,
                        icon="warning", option_1="Cancelar", option_2="Refazer")
            
            response = msg.get()
            return response
        
        
        def click_login(event=None):
            
            if self.entry_user.get().strip() and self.entry_password.get().strip():
                
                verifica_user()
                self.entry_user.reset_default()
                self.entry_password.reset_default()
                self.entry_password.password_input()
             
            ## Quando o usuário e senha estiverem vazio    
            elif  not self.entry_user.get().strip() and not self.entry_password.get().strip() :
                
                self.entry_user.reset_default()
                self.entry_user.show_waring()
                self.entry_password.reset_default()
                self.entry_password.show_waring()
                self.entry_password.configure(show='*')
                men = show_warning("Campo Usuário  e senha Vazio")
                if men == "Refazer":
                    self.entry_user.reset_default()
                    self.entry_password.reset_default()
                    self.entry_user.delete(0,END)
                    self.entry_password.delete(0,END)
                    self.entry_password.password_input()
                    
                
            ## Quando o usuário estiver vazio     
            elif  not self.entry_user.get().strip():
                
                self.entry_user.reset_default()
                self.entry_user.show_waring()
                self.entry_password.reset_default()
                self.entry_password.password_input()
                
                men = show_warning("Campo usuario  Vazio")
                if men == "Refazer":
                    self.entry_user.reset_default()
                    self.entry_user.delete(0,END)

                    
            #Quando a senha estiver vazia     
            elif  not self.entry_password.get().strip():

                self.entry_user.reset_default()
                self.entry_password.reset_default()
                self.entry_password.show_waring()
                self.entry_password.configure(show='*')
                men = show_warning("Campo senha  Vazio")
                
                if men == "Refazer":
                    self.entry_password.reset_default()
                    self.entry_password.delete(0,END)
                    self.entry_password.password_input()
                
            else: 
                men = show_warning("Campos Vazios")
                if men == "Refazer":
                    self.entry_user.reset_default()
                    self.entry_password.reset_default()
                    self.entry_user.delete(0,END)
                    self.entry_password.delete(0,END)
                    self.entry_password.password_input()
            pass
        
        def verifica_user(event=None):
            print(f"Usuário = {self.entry_user.get()}\n Senha = {self.entry_password.get()}")
            
            usuario_login = self.entry_user.get().strip() 
            password_login = self.entry_password.get().strip()
            
            if usuario_login == USER_TEST and password_login == USER_PASSWORD_TEST:
                print("Login realizado com sucesso")
            else:
                msg = CTkMessagebox(title="Warning", message="Usuário ou senha incorretos",
                        icon="cancel", option_1="Okay")

        
        def register_user(event=None):
            #AppRegister(self.master_frame).pack()
            self.pack_forget()
            form_register = AppRegister(self.master_frame)
            form_register.pack(expand=True, fill=BOTH)
            pass
        
        self.label = ctk.CTkLabel(self,text=f"Bem Vindo ao {APP_CONFIG_NAME}", font=('Arial',20))
        self.label.place(x=10,y=2)
        
        self.label_user = ctk.CTkLabel(self,text="Usuário:", font=("Arial",12))
        self.entry_user = EntryPassword(self,width=320)
        
        self.label_password = ctk.CTkLabel(self,text="Senha:", font=("Arial",12))
        self.entry_password = EntryPassword(self,width=320,show ='*')
        self.entry_password.password_input()
        
        self.check_save_login = ctk.CTkCheckBox(self, text="Salvar Login")
        
        self.button_login = ctk.CTkButton(self, text="Login", command=click_login )
        
        self.button_register = ctk.CTkButton(self,hover=False, text="Registrar",  command= register_user )
        
        self.label_user.place(x=5,y=90)
        self.entry_user.place(x=5,y=115)
        
        self.label_password.place(x=5,y=150)
        self.entry_password.place(x=5,y=175)
        self.check_save_login.place(x=5, y=215)
        
        self.button_login.place(x=5,y=270)
        self.button_register.place(x=200,y=270)
        
        self.entry_user.bind('<Return>',lambda e=None : self.entry_password.focus())
        self.entry_password.bind('<Return>',lambda e=None : self.button_login.focus())
        self.button_login.bind('<Return>',click_login)
        
        pass 
    

class AppRegister(ctk.CTkFrame):
    def __init__(self, master=None,width:int = 450,prime_user: bool = False ):
        super().__init__(master,width)
        self.master_frame = master
        self.prime_user = prime_user
        self.tela_register()
        
        
    def tela_register(self):
        def back_login():
            self.pack_forget()
            frame_login = AppLogin(self.master_frame)
            frame_login.pack(fill=BOTH, expand=True)
            pass
        
        def callback_register_user():
            def restart_entrys():
                self.entry_name.reset_default()
                self.entry_user.reset_default()
                self.entry_password.reset_default()
                self.entry_confirm_password.reset_default()
                
                #self.entry_confirm_password.password_input()
                #self.entry_password.password_input()
                
                pass
            
            def save_register_user():
                try:
                    if models.get_user(type='user_filter', user=user)== 0 :
                        models.new_user(
                            bussines= 1, 
                            name=name_user,
                            user=user,
                            password=password,
                            email=email_user,
                            phone=phone_user
                            )
                        msg = CTkMessagebox(title="Sucesso", message=f"Usuário foi cadastrado com sucesso !",
                        icon="check", option_1="Okay") 
                        back_login()
                    else:
                         msg = CTkMessagebox(title="Warning", message=f"Usuário Já cadastrado",
                        icon="cancel", option_1="Okay")
                                
                except ValueError as error: msg = CTkMessagebox(title="Warning", message=f"Ocorreu um erro ao salvar usuário\n {error}",
                        icon="cancel", option_1="Okay")   
                
                
            name_user = self.entry_name.get().strip()
            email_user = self.entry_email.get().strip()
            phone_user = self.entry_phone.get().strip()
            user = self.entry_user.get().strip().strip()
            password = self.entry_password.get().strip()
            confirm_password = self.entry_confirm_password.get().strip()
            
            variaveis =  [
                {name_user:self.entry_name},
                {user: self.entry_user},
                {password: self.entry_password},
                {confirm_password: self.entry_confirm_password}
                ]
            label_info = ctk.CTkLabel(self, text="",font=("Arial",17), text_color="red")
            
            last_row = self.button_confirm.grid_info()["row"]
            
            label_info.grid(row=int(last_row) + 1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
            

            for variavel in variaveis:
                for chave,valor in variavel.items():
                    if not chave:
                        valor.reset_default()
                        valor.show_waring()
                        if valor == self.entry_password or self.entry_confirm_password:
                            valor.configure(show='*')                       
            
            if password != confirm_password:
                restart_entrys()
                self.entry_password.show_waring()
                self.entry_password.password_input()
                self.entry_confirm_password.show_waring()
                self.entry_confirm_password.password_input()
                label_info.configure(text='As senhas não são iguais.',font=("Arial",18))
                
            else:
                if password != '' and confirm_password != '': 
                    save_register_user() 
                

        
        self.label = ctk.CTkLabel(self,text=f"Registro {APP_CONFIG_NAME}")
        
        self.label_name = ctk.CTkLabel(self, text="Nome Completo:")
        self.entry_name = EntryPassword(self,width=320)
        
        self.label_email = ctk.CTkLabel(self,text="E-mail:")
        self.entry_email = EntryPassword(self,width=320)
        
        self.label_phone = ctk.CTkLabel(self,text='Telefone:')
        self.entry_phone = EntryPassword(self,width=320)
        
        self.label_user = ctk.CTkLabel(self,text="Usuário:")
        self.entry_user = EntryPassword(self,width=320)
        
        self.label_password = ctk.CTkLabel(self,text="Senha:")
        self.entry_password = EntryPassword(self,width=320,show='*')
        
        self.label_confirm_password = ctk.CTkLabel(self,text="Confirmar a Senha:")
        self.entry_confirm_password  = EntryPassword(self,width=320)
        
        self.button_confirm = ctk.CTkButton(self,text="Confirme Registro",width=140, command=callback_register_user)
        
        self.button_back = ctk.CTkButton(self,  text="Voltar",width=140,command=back_login)
                
        self.entry_password.password_input()
        self.entry_confirm_password.password_input()
        
        self.entry_confirm_password.grid()

        widgets = [
            (self.label, 0, 0, 2),  # O título ocupa duas colunas
            (self.label_name, 1, 0, 1),
            (self.entry_name, 1, 1, 1),
            (self.label_email, 2, 0, 1),
            (self.entry_email, 2, 1, 1),
            (self.label_phone, 3, 0, 1),
            (self.entry_phone, 3, 1, 1),
            (self.label_user, 4, 0, 1),
            (self.entry_user, 4, 1, 1),
            (self.label_password, 5, 0, 1),
            (self.entry_password, 5, 1, 1),
            (self.label_confirm_password, 6, 0, 1),
            (self.entry_confirm_password, 6, 1, 1),
            (self.button_confirm, 7, 0, 1),
            (self.button_back, 7, 1, 1),
        ]

        # Adiciona widgets à grid
        for widget, row, column, colspan in widgets:
            widget.grid(row=row, column=column, columnspan=colspan, padx=5, pady=5, sticky="ew")

        # Configura o peso das colunas para expandirem corretamente
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        
        if self.prime_user == True:
            self.button_back.grid_forget()
            self.button_confirm.grid_configure(columnspan=3)
            
        pass     
    
    pass

class AppMain(ctk.CTk):
    
    
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.tela_main()
        self.widgets_tela_main()
    
    def tela_main(self):
        self.geometry("900x600")
        self.title(f"{APP_CONFIG_NAME}")
        self.resizable(False,False)
        
    def widgets_tela_main(self):
        qt_users = models.get_user(type="count")
        frame_login = None
        frame_register = None
        self.frame_left = ctk.CTkFrame(self,width=450)
        self.frame_left.pack(side=LEFT,fill=BOTH,expand=TRUE)
        
        self.frame_rigth =  ctk.CTkFrame(self,width=450)
        self.frame_rigth.pack(side=RIGHT,fill=BOTH,expand=TRUE)
        

        
        if qt_users > 0:
            frame_login = AppLogin(self.frame_rigth)
            frame_login.pack(fill=BOTH, expand=True)
        else:
            frame_register = AppRegister(self.frame_rigth,prime_user=True)
            frame_register.pack(fill=BOTH, expand=True)
            

if __name__=='__main__':
    root = AppMain()
    root.mainloop()
    
    
    
    