import sqlite3
import os
from pathlib import Path




class Calculations: 
    def __init__(self) -> None:
        PATH = Path(__file__).parent 
        path_db = os.path.join(PATH, 'database', 'database.db')
        self.conn = sqlite3.connect(path_db)
        self.cursor = self.conn.cursor()
    
    def calc_despesa(self):
        
        calc = self.cursor.execute("SELECT SUM(valor) FROM DESPESAS WHERE DATA_PAG IS NULL OR DATA_PAG = ''")
        return calc.fetchall()[0][0]
        #return calc.fetchall()


if __name__=='__main__':  
    a = Calculations()
    b = a.calc_despesa()
    print(b)      