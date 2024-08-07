from typing import Tuple
import customtkinter as ctk 
import os 
from pathlib import Path
from tkcalendar import *
from PIL import Image
try :   
    from .config_app import *
except: 
    from config_app import * 

class FormExpense(ctk.CTkToplevel):
    def __init__(self,id:int = None, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(id, *args, fg_color=fg_color, **kwargs)
        self.id_expense = id 
        if self.id_expense:
            self._add_expense_info()
        
        self._conf_display()
        self.geometry("400x500")
        self.resizable(False,False)
            
    def _pop_calendario(self):
        self.pop = ctk.CTkToplevel(
            self,
        )
        self.pop.geometry('300x200+780+350')
        self.pop.title('Calendário')
        self.pop.resizable(False, False)
        self.pop.grab_set()
        self.pop.focus_force()

        self.calendario = Calendar(
            self.pop,
            selectmode='day',
        )
        self.calendario.place(x=0, y=0, width=300, height=160)

        self.bt_confirmar = ctk.CTkButton(
            self.pop,
            text='Confirmar',
            font=('Segoe UI', 12, 'bold'),
            width=100,
            height=30,
            command=self._get_date
        )
        self.bt_confirmar.place(x=18, y=163)
        self.bt_cancelar = ctk.CTkButton(
            self.pop,
            text='Cancelar',
            font=('Segoe UI', 12, 'bold'),
            width=100,
            height=30,
            command=self._fecha_calendario
        )
        self.bt_cancelar.place(x=189, y=163)

    def _get_date(self):
        self.entry_date_expense.delete(0, 'end')
        data_nascimento = self.calendario.get_date()
        self.entry_date_expense.insert('end', data_nascimento)
        self.pop.destroy()

    def _fecha_calendario(self):
        self.pop.destroy()    
        
    def _conf_display(self):
 
        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'assets','imagens','icons')
        self.calendar_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "calendar_light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "calendar_light.png")), size=(20, 20))
        self.tabview_expense = ctk.CTkTabview(self)
        self.tabview_expense.add('Despesa')
        self.tabview_expense.add('Mais Deta.')
        self.tabview_expense.pack(fill='both',expand=True)
        
        self.label_valor_expense = ctk.CTkLabel(self.tabview_expense.tab('Despesa'),text='Valor da Despesa:',anchor='w')
        self.label_cifrao_expense = ctk.CTkLabel(self.tabview_expense.tab('Despesa'),text='R$:',anchor='w')
        self.entry_value_expense =  ctk.CTkEntry(self.tabview_expense.tab('Despesa'),)
        
        def __switch_event():
            e = self.switch_state_expense.get()
            
            if e == 1:
                self.switch_state_expense.configure(text='Foi Recebido')
            else: 
                self.switch_state_expense.configure(text='Não recebido')               
        
        self.switch_state_expense = ctk.CTkSwitch(self.tabview_expense.tab('Despesa'),text='Não recebido',command=__switch_event)
        
        self.label_date_expense = ctk.CTkLabel(self.tabview_expense.tab('Despesa'),text='Data da Despesa:',anchor='w')
        self.entry_date_expense = ctk.CTkEntry(self.tabview_expense.tab('Despesa'))
        self.button_date_expense = ctk.CTkButton(self.tabview_expense.tab('Despesa'),image=self.calendar_image,text='',width=20,height=20,command=self._pop_calendario)
        
        self.label_descri_expense = ctk.CTkLabel(self.tabview_expense.tab('Despesa'),text=' Descrição:',anchor='w')
        self.entry_descri_expense = ctk.CTkEntry(self.tabview_expense.tab('Despesa'),width=380)
        
        self.label_origin_expense = ctk.CTkLabel(self.tabview_expense.tab('Despesa'),text=' Origem da Despesa:',anchor='w')
        self.optionmenu_origin_expense = ctk.CTkOptionMenu(self.tabview_expense.tab('Despesa'))
        
        self.label_account_expense = ctk.CTkLabel(self.tabview_expense.tab('Despesa'),text=' Conta Débito:',anchor='w')
        self.optionmenu_account_expense =  ctk.CTkOptionMenu(self.tabview_expense.tab('Despesa'))
        
        self.button_confirm_expense = ctk.CTkButton(self.tabview_expense.tab('Despesa'),text="Confirmar", command=self._get_data_display)
        self.button_back_expense = ctk.CTkButton(self.tabview_expense.tab('Despesa'),text="Cancelar",command=lambda e=None: self.destroy())
        

                # Linha 0
        self.label_valor_expense.grid(row=0, column=0, padx=5, pady=5,sticky="w")

        # Linha 1
        self.label_cifrao_expense.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_value_expense.grid(row=1, column=1,sticky="w", padx=0, pady=5)
        


        # Linha 2
        self.switch_state_expense.grid(row=2, column=0,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 3
        self.label_date_expense.grid(row=3, column=0,sticky="w", padx=5, pady=5)

        # Linha 4
        self.entry_date_expense.grid(row=4, column=0,sticky="w", columnspan=2, padx=5, pady=5)
        self.button_date_expense.grid(row=4, column=1,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 5
        self.label_descri_expense.grid(row=5, column=0,sticky="w", padx=5, pady=5)

        # Linha 6
        self.entry_descri_expense.grid(row=6, column=0,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 7
        self.label_origin_expense.grid(row=7, column=0,sticky="w", columnspan=2, padx=5, pady=5)
        self.label_account_expense.grid(row=7, column=1,sticky="w", columnspan=2, padx=5, pady=5)
        
        self.optionmenu_origin_expense.grid(row=8, column=0,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 8
        self.optionmenu_account_expense.grid(row=8, column=1,sticky="w", columnspan=2, padx=5, pady=5)
        
        self.button_confirm_expense.grid(row=9, column=0,sticky="w", columnspan=2, padx=5, pady=5)
        self.button_back_expense.grid(row=9, column=1,sticky="w", columnspan=2, padx=5, pady=5)
        
        #self.switch_expense_data
        
        
        


        pass
    
    def _get_data_display(self):
        
        self.value_expense_data = self.entry_value_expense.get()
        self.date_expense_data = self.entry_date_expense.get()
        self.descri_expense_data = self.entry_descri_expense.get()
        
        self.switch_expense_data = self.switch_state_expense.get()
        
        self.account_expense_data = self.optionmenu_account_expense.get()
        self.origin_expense_data = self.optionmenu_origin_expense.get()
        
        widgets = [
        self.value_expense_data,
        self.date_expense_data,
        self.descri_expense_data,
        self.switch_expense_data,
        self.account_expense_data,
        self.origin_expense_data,
        ]
        
        for i in widgets:
            if i:
                print(i)
            else:
                print('vazio')    
        
        
        
        pass
    
    def _add_expense_info(self):    
        pass

    
if __name__=='__main__':
    root = ctk.CTk()
    root.title("expense")
    app = FormExpense()
    root.mainloop()