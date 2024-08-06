from typing import Tuple
import customtkinter as ctk
from main import AppRegister, AppLogin

class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("500x500")
        self.button_login = ctk.CTkButton(self,text="Login", command= self.open_login)        
        self.button_register = ctk.CTkButton(self,text="register", command= self.open_register)
        
        self.button_login.pack()
        self.button_register.pack()
    
    def open_login(self):
        open_frame = OpenLogin(self)            
    
    def open_register(self):
        open_frame = OpenRegister(self)
        
        
        
class OpenLogin(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        framelogin = AppLogin(self)
        framelogin.pack(fill='both', expand=True)  

class OpenRegister(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        frameregister = AppRegister(self)
        frameregister.pack(fill='both', expand=True)                
        
        
if __name__=='__main__':
    app = App()
    app.mainloop()
            