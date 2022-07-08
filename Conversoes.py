import os

import Analyzer


nomeDoCaminho = Analyzer.NomeDoDiretorio
print(nomeDoCaminho)
try:
    # Change the current working Directory
    os.chdir(nomeDoCaminho)
    print("Directory changed")
except OSError:
    print("Can't change the Current Working Directory")

print("Current Working Directory ", os.getcwd())

# Check if New path exists
if os.path.exists("/home/varun/temp"):
    # Change the current working Directory
    os.chdir("/home/varun/temp")
else:
    print("Can't change the Current Working Directory")


Diretorio1 = str(os.getcwd())
print(Diretorio1)
print(nomeDoCaminho)