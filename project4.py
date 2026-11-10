import csv,json

with open ("file2.csv", "r", encoding="utf-8") as file:
    content = csv.DictReader(file)
    clients =[]

    for row in content:
        clients.append(row)

with open("clients2.json", "w", encoding="utf-8",newline="") as file:
    
    json.dump(clients, file, indent=4)
    





    