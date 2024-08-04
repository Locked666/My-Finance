from datetime import datetime 

a  = datetime.today()
data_formatada = a.strftime("%Y-%m-%d")
datetime.strptime(data_formatada, "%Y-%m-%d %h:%m:%s").date()

print(a)
print(data_formatada)