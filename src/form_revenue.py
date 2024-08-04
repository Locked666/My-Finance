from typing import Tuple
import customtkinter as ctk 
from CTkMessagebox import CTkMessagebox
import os 
from pathlib import Path
from tkcalendar import *
from datetime import datetime
from PIL import Image
try :   
    from .config_app import *
except: 
    from config_app import * 

class FormRevenue(ctk.CTkToplevel):
    def __init__(self,id:int = None, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.id_revenue = id 
        if self.id_revenue:
            self._add_revenue_info()
        
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
        self.entry_date_revenue.delete(0, 'end')
        data_nascimento = self.calendario.get_date()
        self.entry_date_revenue.insert('end', data_nascimento)
        self.pop.destroy()

    def _fecha_calendario(self):
        self.pop.destroy()    
        
    def _conf_display(self):
 
        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'assets','imagens','icons')
        self.calendar_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "calendar_light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "calendar_light.png")), size=(20, 20))
        self.tabview_revenue = ctk.CTkTabview(self)
        self.tabview_revenue.add('Receita')
        #self.tabview_revenue.add('Mais Deta.')
        self.tabview_revenue.pack(fill='both',expand=True)
        
        self.label_valor_revenue = ctk.CTkLabel(self.tabview_revenue.tab('Receita'),text='Valor da Receita:',anchor='w')
        self.label_cifrao_revenue = ctk.CTkLabel(self.tabview_revenue.tab('Receita'),text='R$:',anchor='w')
        self.entry_value_revenue =  ctk.CTkEntry(self.tabview_revenue.tab('Receita'),)
        
        def __switch_event():
            e = self.switch_state_revenue.get()
            l = self.label_date_revenue.cget("text")
            
            if e == 1:
                self.switch_state_revenue.configure(text='Foi Recebido')
                if l != "Data da Receita:":
                    self.label_date_revenue.configure(text='Data da Receita:')   
                     
                
            else: 
                self.switch_state_revenue.configure(text='Não recebido')
                if l != "Data Prevista:":
                    self.label_date_revenue.configure(text='Data Prevista:')               
        
        self.switch_state_revenue = ctk.CTkSwitch(self.tabview_revenue.tab('Receita'),text='Não recebido',command=__switch_event)
        
        self.label_date_revenue = ctk.CTkLabel(self.tabview_revenue.tab('Receita'),text='Data Prevista:',anchor='w')
        self.entry_date_revenue = ctk.CTkEntry(self.tabview_revenue.tab('Receita'))
    
        
        self.button_date_revenue = ctk.CTkButton(self.tabview_revenue.tab('Receita'),image=self.calendar_image,text='',width=20,height=20,command=self._pop_calendario)
        
        self.label_descri_revenue = ctk.CTkLabel(self.tabview_revenue.tab('Receita'),text=' Descrição:',anchor='w')
        self.entry_descri_revenue = ctk.CTkEntry(self.tabview_revenue.tab('Receita'),width=380)
        
        self.label_origin_revenue = ctk.CTkLabel(self.tabview_revenue.tab('Receita'),text=' Origem da receita:',anchor='w')
        self.optionmenu_origin_revenue = ctk.CTkOptionMenu(self.tabview_revenue.tab('Receita'))
        
        self.label_account_revenue = ctk.CTkLabel(self.tabview_revenue.tab('Receita'),text=' Conta Destino:',anchor='w')
        self.optionmenu_account_revenue =  ctk.CTkOptionMenu(self.tabview_revenue.tab('Receita'))
        
        self.button_confirm_revenue = ctk.CTkButton(self.tabview_revenue.tab('Receita'),text="Confirmar", command=self._get_data_display)
        self.button_back_revenue = ctk.CTkButton(self.tabview_revenue.tab('Receita'),text="Cancelar",command=lambda e=None: self.destroy())
        

                # Linha 0
        self.label_valor_revenue.grid(row=0, column=0, padx=5, pady=5,sticky="w")

        # Linha 1
        self.label_cifrao_revenue.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_value_revenue.grid(row=1, column=1,sticky="w", padx=0, pady=5)
        


        # Linha 2
        self.switch_state_revenue.grid(row=2, column=0,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 3
        self.label_date_revenue.grid(row=3, column=0,sticky="w", padx=5, pady=5)

        # Linha 4
        self.entry_date_revenue.grid(row=4, column=0,sticky="w", columnspan=2, padx=5, pady=5)
        self.button_date_revenue.grid(row=4, column=1,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 5
        self.label_descri_revenue.grid(row=5, column=0,sticky="w", padx=5, pady=5)

        # Linha 6
        self.entry_descri_revenue.grid(row=6, column=0,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 7
        self.label_origin_revenue.grid(row=7, column=0,sticky="w", columnspan=2, padx=5, pady=5)
        self.label_account_revenue.grid(row=7, column=1,sticky="w", columnspan=2, padx=5, pady=5)
        
        self.optionmenu_origin_revenue.grid(row=8, column=0,sticky="w", columnspan=2, padx=5, pady=5)

        # Linha 8
        self.optionmenu_account_revenue.grid(row=8, column=1,sticky="w", columnspan=2, padx=5, pady=5)
        
        self.button_confirm_revenue.grid(row=9, column=0,sticky="w", columnspan=2, padx=5, pady=5)
        self.button_back_revenue.grid(row=9, column=1,sticky="w", columnspan=2, padx=5, pady=5)
        
        #self.switch_revenue_data
        self.entry_value_revenue.bind('<Return>',lambda event=None: self.entry_date_revenue.focus())
        self.entry_value_revenue.bind("<KeyRelease>",lambda event=None:self._format_value(widget=self.entry_value_revenue))
        
        self.entry_date_revenue.bind("<Return>",lambda event=None: self._format_date(widget=self.entry_date_revenue))
        self.entry_date_revenue.bind("<Return>",lambda event=None: self.entry_descri_revenue.focus())
        
        self.switch_state_revenue.select()
        __switch_event()


        pass
    
    def _get_data_display(self):
        error_log = []
        hoje = datetime.today()
        hoje =  hoje.strftime("%d/%m/%Y")
        erro_format = ''
        
        self.value_revenue_data = self.entry_value_revenue.get()
        self.date_revenue_data = self.entry_date_revenue.get()
        self.descri_revenue_data = self.entry_descri_revenue.get().strip()
        
        self.switch_revenue_data = self.switch_state_revenue.get()
        
        self.account_revenue_data = self.optionmenu_account_revenue.get()
        self.origin_revenue_data = self.optionmenu_origin_revenue.get()
        
        widgets = [
       [1, self.value_revenue_data],
       [2, self.date_revenue_data],
       [3, self.descri_revenue_data],
       [4, self.switch_revenue_data],
       [5, self.account_revenue_data],
       [6, self.origin_revenue_data],
       [7, "Continue_true_execut"]
        ]
        
        for index,i in enumerate(widgets):

            match index:
                case 0:
                    if self.value_revenue_data  :
                        pass
                    else: 
                        self.entry_value_revenue.configure(fg_color=('#8B0000'))
                        error_log.append('O valor não pode ser menor que zero')
                        
                case 1:
                    if self.date_revenue_data:
                        if self.date_revenue_data < hoje:
                            error_log.append("Não poderá ser lançada receita com a data anterior a atual")
                            pass
                    else:
                        error_log.append('O campo data não pode estar Vazio') 
                        
                
                case 2:
                    if self.descri_revenue_data:
                        pass
                        
                    else:
                        error_log.append("O campo descrição não pode estar vazio")
                        
                
                case 3,4,5:
                    pass

                case 6:
                    if len(error_log) == 0 :
                        self._save_revenue_data()
                        print("teste_save")
                    else:
                        for i in error_log:
                            if erro_format == "":
                                erro_format =  i
                            else:
                                erro_format = erro_format +',' + '\n'+ i
                            
                        msg = CTkMessagebox(title="Warning", message=f"{erro_format}",
                        icon="cancel", option_1="Okay")
                        
 
    
    def _save_revenue_data(self):
        msg = CTkMessagebox(title="Sucesso", message=f"Receita Gerada com sucesso. !",
                        icon="check", option_1="Okay") 
        
        
    
    def _add_revenue_info(self): 

        pass
    
    def _format_value(self, widget=None):
        # try:
        value = widget.get().strip()
        
        value = ''.join(filter(str.isdigit, value))

        if len(value) < 3:
            value = value.zfill(3)

        # Pega os centavos (últimos dois dígitos) e o restante dos números para a parte inteira
        centavos = value[-2:]
        inteiro = value[:-2] or '0'

        # Formata o valor como R$ XXX,XXX.XX
        value_format = f"{int(inteiro):,},{centavos}"
        widget.delete(0, 'end')
        widget.insert(0, value_format)
        # except: 
        #     widget.configure(fg_color=('Blue' ))   
    
    def _format_date(self,widget=None):
        try: 
            value_date = str(widget.get().strip())
            #value_date = str(value_date)
            dt = datetime.strptime(value_date,"%d%m%Y")
            dtv = dt.strftime("%d/%m/%Y")
            widget.delete(0,"end")
            widget.insert(0,dtv)
            widget.configure(fg_color=('#F9F9FA', '#343638'))

        except:
            widget.configure(fg_color=('#8B0000' ))
            pass    
        
       

if __name__=='__main__':
    root = ctk.CTk()
    root.title("Revenue")
    app = FormRevenue
    bnt = ctk.CTkButton(root, text="abra",command=lambda: app())
    bnt.pack()
    root.mainloop()