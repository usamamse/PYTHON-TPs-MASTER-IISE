import csv

with open(r"g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\contacts.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nom", "Âge", "Ville"])  
    writer.writerow(["ELMESSAOUDI", "22", "Taroudant"])  
    writer.writerow(["ZAHRI", "25", "Houara"])
    writer.writerow(["BEIHI", "18", "Laayoune"])

print("contacts.csv has been created.")

with open(r"g:\Mon Drive\Workspace\Python\PYTHON TP IISE MASTER\TP5\contacts.csv", mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)

    print("==== Contacts ====")
    for row in reader:
        print(f"Nom: {row[0]} Age: {row[1]} Ville: {row[2]}")