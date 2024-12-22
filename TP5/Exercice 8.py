import os 

file = r"g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\inexistant.txt"


if os.path.exists(file):
    print(f"File existed !")
else:
    print(f"File does not existed !")

