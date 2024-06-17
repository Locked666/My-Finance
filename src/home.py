from typing import Tuple
import customtkinter as ctk
import os
from PIL import Image
try :   
    from .config_app import *
except: 
    from config_app import *   

class AppHome(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self._config_display()
        self._config_layout()
        
    def _config_display(self):
        self.title(f"Bem vindo ao {APP_CONFIG_NAME}")
        self.geometry("1000x700")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
    def _config_layout(self):
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'assets','imagens','icons')
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(25, 25))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        
        self.dashboard_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "dashboard_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "dashboard_light.png")), size=(30, 30))
        
        self.investimento_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "investimento_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "investimento_light.png")), size=(30, 30))
        
        self.inventario_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "inventario_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "inventario_light.png")), size=(30, 30))
        
        self.wallet_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "carteira_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "carteira_light.png")), size=(30, 30))
        
        self.revenue_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "receita_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "receita_light.png")), size=(30, 30))
        
        self.expense_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "despesa_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "despesa_light.png")), size=(30, 30))
        
        self.config_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "config_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "config_light.png")), size=(30, 30))

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text=f"  {APP_CONFIG_NAME}", image=self.logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=lambda e=None: self.select_frame_by_name("home"))#self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        
        

        self.dashboard_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Dashboard",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.dashboard_image, anchor="w", command=self.dashboard_button_event)
        self.dashboard_button.grid(row=2, column=0, sticky="ew")
        
        self.revenue_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Receita",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.revenue_image, anchor="w", command=self.revenue_button_event)
        self.revenue_button.grid(row=3, column=0, sticky="ew")
        
        self.expense_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Despesa",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.expense_image, anchor="w", command=self.expense_button_event)
        self.expense_button.grid(row=4, column=0, sticky="ew")


        self.invest_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Investimento",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.investimento_image, anchor="w", command=self.invest_button_event)
        self.invest_button.grid(row=5, column=0, sticky="ew")
        
        
        self.inventory_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inventário",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.inventario_image, anchor="w", command=self.inventory_button_event)
        self.inventory_button.grid(row=6, column=0, sticky="ew")
        
        
        self.wallet_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Carteira",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.wallet_image, anchor="w", command=self.wallet_button_event)
        self.wallet_button.grid(row=7, column=0, sticky="ew")
        
        
        self.settings_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Configuração",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.config_image, anchor="w", command=self.settings_button_event)
        self.settings_button.grid(row=8, column=0,  sticky="ws")


        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=9, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        
        self.label_teste = ctk.CTkLabel(self.home_frame,text='teste')
        self.label_teste.pack(anchor='center',pady=100)

        # self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        # self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # self.home_frame_button_1 = ctk.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.home_frame_button_2 = ctk.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        # self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.home_frame_button_3 = ctk.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        # self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_4 = ctk.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.dashboard_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.invest_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.inventory_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.wallet_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.expense_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.revenue_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.settings_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "dashboard" else "transparent")
        
        self.invest_button.configure(fg_color=("gray75", "gray25") if name == "invest" else "transparent")
        
        self.inventory_button.configure(fg_color=("gray75", "gray25") if name == "inventory" else "transparent")
        
        self.wallet_button.configure(fg_color=("gray75", "gray25") if name == "wallet" else "transparent")
        
        self.revenue_button.configure(fg_color=("gray75", "gray25") if name == "revenue" else "transparent")
        
        self.expense_button.configure(fg_color=("gray75", "gray25") if name == "expense" else "transparent")
        
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "dashboard":
            self.dashboard_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.dashboard_frame.grid_forget()
            
        if name == "invest":
            self.invest_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.invest_frame.grid_forget()
            
        if name == "inventory":
            self.inventory_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.inventory_frame.grid_forget()
            
        if name == "wallet":
            self.wallet_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.wallet_frame.grid_forget()
            
        if name == "revenue":
            self.revenue_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.revenue_frame.grid_forget()
            
        if name == "expense":
            self.expense_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.expense_frame.grid_forget()
            
        if name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()

   # def home_button_event(self):
    #    self.select_frame_by_name("home")

    def dashboard_button_event(self):
        self.select_frame_by_name("dashboard")

    def invest_button_event(self):
        self.select_frame_by_name("invest")
        
    def inventory_button_event(self):
        self.select_frame_by_name("inventory")
        
    def wallet_button_event(self):
        self.select_frame_by_name("wallet")
        
    def expense_button_event(self):
        self.select_frame_by_name("expense")
        
    def revenue_button_event(self):
        self.select_frame_by_name("revenue")
        
    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
   app = ctk.CTk()
   home = AppHome()
   app.mainloop()
 