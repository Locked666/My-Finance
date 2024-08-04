from typing import Tuple
import customtkinter as ctk
import os
from CTkTable import *
from PIL import Image

try :   
    from .config_app import *
    from .form_revenue import FormRevenue
    from .form_expense import FormExpense
except: 
    from config_app import *
    from form_revenue import FormRevenue
    from form_expense import FormExpense   

class AppHome(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self._config_display()
        self._config_layout()
        self.app_revenue = None
        
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
        
        self.eyes_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "eye1_black.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "eye1_white.png")), size=(10, 10))

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text=f"  {APP_CONFIG_NAME}", image=self.logo_image,
                                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=lambda e=None: self.select_frame_by_name("home"))
        self.home_button.grid(row=1, column=0, sticky="ew")
        
        

        self.dashboard_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Dashboard",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.dashboard_image, anchor="w", command= lambda e=None: self.select_frame_by_name("dashboard")) #self.dashboard_button_event)
        self.dashboard_button.grid(row=2, column=0, sticky="ew")
        
        self.revenue_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Receita",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.revenue_image, anchor="w", command=lambda e=None: self.select_frame_by_name("revenue"))#self.revenue_button_event)
        self.revenue_button.grid(row=3, column=0, sticky="ew")
        
        self.expense_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Despesa",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.expense_image, anchor="w", command=lambda e=None: self.select_frame_by_name("expense"))# self.expense_button_event)
        self.expense_button.grid(row=4, column=0, sticky="ew")


        self.invest_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Investimento",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.investimento_image, anchor="w", command=lambda e=None: self.select_frame_by_name("invest"))#self.invest_button_event)
        self.invest_button.grid(row=5, column=0, sticky="ew")
        
        
        self.inventory_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inventário",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.inventario_image, anchor="w", command=lambda e=None: self.select_frame_by_name("inventory"))#self.inventory_button_event)
        self.inventory_button.grid(row=6, column=0, sticky="ew")
        
        
        self.wallet_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Carteira",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.wallet_image, anchor="w", command=lambda e=None: self.select_frame_by_name("wallet"))#self.wallet_button_event)
        self.wallet_button.grid(row=7, column=0, sticky="ew")
        
        
        self.settings_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Configuração",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.config_image, anchor="w", command=lambda e=None: self.select_frame_by_name("settings"))#self.settings_button_event)
        self.settings_button.grid(row=8, column=0,  sticky="ws")


        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=9, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        #self.home_frame.grid_columnconfigure(1, weight=1)
        #self.home_frame.grid_rowconfigure(3,weight=1, uniform=True)
        
        self.home_frame.grid_rowconfigure(0, minsize=20)  # Espaçamento superior de 20 pixels
        
        # Configura as colunas para espaçamento entre os frames
        self.home_frame.grid_columnconfigure(0, weight=1)  # Espaçamento antes do primeiro frame
        self.home_frame.grid_columnconfigure(1, weight=0,minsize=20)  # Primeiro frame
        self.home_frame.grid_columnconfigure(2, weight=1)  # Espaçamento entre primeiro e segundo frame
        self.home_frame.grid_columnconfigure(3, weight=0,minsize=20)  # Segundo frame
        self.home_frame.grid_columnconfigure(4, weight=1)  # Espaçamento entre segundo e terceiro frame
        self.home_frame.grid_columnconfigure(5, weight=0,minsize=20)  # Terceiro frame
        self.home_frame.grid_columnconfigure(6, weight=1)  # Espaçamento depois do terceiro frame
        

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

    def _layout_display_home(self):
        self.urgent_warning = ctk.CTkFrame(self.home_frame, width=218,height=90,border_width=2,corner_radius=8)
        
        self.green_warning = ctk.CTkFrame(self.home_frame, width=218,height=90,border_width=2,corner_radius=8)
        
        self.yellow_warning = ctk.CTkFrame(self.home_frame, width=218,height=90,border_width=2,corner_radius=8)
        
        self.urgent_warning.grid(row=1, column=1, padx=10, pady=10)      
        self.green_warning.grid(row=1, column=3, padx=10, pady=10)
        
        self.yellow_warning.grid(row=1, column=5, padx=10, pady=10)
        # -----------------------------------------------------------
        self.label_urgent_value = ctk.CTkLabel(self.urgent_warning,text=f"0",font=('Arial',18))
        
        self.button_urgent = ctk.CTkButton(self.urgent_warning,text='',width=10,height=10,image=self.eyes_image,compound='left')
        
        self.label_urgent_value.grid(row=1,column=1)
        self.button_urgent.grid(row=1,column=3)
        #-------------------------#
        
        self.label_yellow_value = ctk.CTkLabel(self.yellow_warning,text=f"0",font=('Arial',18))
        
        self.button_yellow= ctk.CTkButton(self.yellow_warning,text='',width=10,height=10,image=self.eyes_image,compound='left')
        
        self.label_yellow_value.grid(row=1,column=1)
        self.button_yellow.grid(row=1,column=3)
        
        ####################### -##########
        self.label_green_value = ctk.CTkLabel(self.green_warning,text=f"0",font=('Arial',18))
        
        self.button_green = ctk.CTkButton(self.green_warning,text='',width=10,height=10,image=self.eyes_image,compound='left')
        
        self.label_green_value.grid(row=1,column=1)
        self.button_green.grid(row=1,column=3)
        
    def _layout_display_revenue(self):
       
       def returno(e=None):
           a = self.table_revenue.get()
           b= self.table_revenue.get_selected_row()
           c = self.table_revenue.get_selected_column()
           
           print(f"get: {a}")
           print('----------------------------------------------')
           print(f"get_selected_row: {b}")
           print('----------------------------------------------')
           print(f"get_selected_column: {c}")
           print('----------------------------------------------')
           print(f"varavel retornada : {e}")
           print('----------------------------------------------')
           print(f"varavel value : {e['value']}")
           print('----------------------------------------------')
           print(f"varavel value row : {e['row']}")
           print('----------------------------------------------')
           print(f"varavel value row, colum selected : {self.table_revenue.get(row=e['row'])}")
           print('----------------------------------------------')
           print(f"varavel value row: {self.table_revenue.get_row(row=e['row'])}")
           self.table_revenue.draw_table()
           self.table_revenue.select_row(row=e['row'])
           print('--------------------------------------------')
           
           
           #print(f"varavel value row, colum selected : {self.table_revenue.select(row=e['row'],column=e['column'])}")
           
       self.ctkbox = ctk.CTkCheckBox(self.revenue_frame,text=())     
       value = [[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20],
                [21,22,23,24,25]]

        
            
       def callback_button_add_revenue():
           if self.app_revenue is None or not self.app_revenue.winfo_exists():
            self.app_revenue = FormRevenue()
            self.app_revenue.focus_set
           else:
               self.app_revenue.focus() 
           
           
               
           

       self.button_add_revenue = ctk.CTkButton(self.revenue_frame,text='', command=callback_button_add_revenue )
       
       self.table_revenue = CTkTable(self.revenue_frame,values=value,hover=True,hover_color='#000000',command=returno)
       
       
       self.button_add_revenue.grid(column=0,row=0)
       
       self.table_revenue.grid(column=0,row=1)
        
    
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
            self._layout_display_home()
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
            self._layout_display_revenue()
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


    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
   app = ctk.CTk()
   home = AppHome()
   app.mainloop()
 