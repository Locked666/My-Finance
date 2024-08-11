import string
import random
from datetime import *



def convert_date(date,type=None):
    match type:
        case "PtBR":
            date_origim = date
            data_convertida =  datetime.strptime(date_origim,"%Y-%m-%d")
            data_formatada = data_convertida.strftime("%d/%m/%Y")
            return data_formatada
            
        
        case _:    
            date_origim = date
            data_convertida =  datetime.strptime(date_origim,"%d/%m/%Y")
            data_formatada = data_convertida.strftime("%Y-%m-%d")
            return data_formatada
    
def r_date_atual(type='database'):
    a  = datetime.today()

    match type:
        case 'database':
            data_formatada_database = a.strftime("%Y-%m-%d")
            return data_formatada_database
        
        case 'HoraMinuto':
            data_formatada_database = a.strftime("%Y-%m-%d %H:%M:%S")
            return data_formatada_database
            
        case _:
            return a 
            
                    
