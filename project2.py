import csv

with open ("file_csv..csv", "r", encoding="utf-8") as file:
    clients = csv.DictReader(file)

    new_content = []
    for client in clients:
        client2 ={}
        for k, v in client.items():
            k = k.strip()
            v = v.strip()
            client2[k] = v
        new_content.append(client2)


with open("file2.csv", "w", encoding="utf-8",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["name","email","city"])

    writer.writeheader()
    writer.writerows(new_content)

    
        

    
