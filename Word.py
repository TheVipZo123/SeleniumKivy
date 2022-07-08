import docx
import readDocx
import Conversoes
import glob
Diretorio1 = Conversoes.Diretorio1
Diretorio = (glob.glob(Diretorio1 + "/*.docx"))
print(Diretorio)
list_of_list = []
numero = 0
while len(Diretorio) > numero :
    Cae = (Diretorio[numero]).replace(Diretorio1 + "\ ", '')
    print("Cae:"+ Cae)

    print(readDocx.getText(Cae))
    b = readDocx.getText(Cae)
    list_of_list += [b]

    numero = numero + 1

print(list_of_list)