import json

print("1 - Show all clients\n 2 - Add a client\n 3 - Serach for client")
choice = input("enter you choice(1, 2 or 3)")
if choice =="1":
        with open("clients.json", "r") as file:
            clients = json.load(file)
            print(clients)

elif choice== "2":
        with open ("clients.json","r") as file:
            clients = json.load(file)
            name =input("enter the name of the new client: ")
            email = input("enter the email of the new client: ")
            age = input("enter the age of the new client: ")
            new_client = {"name":name,
                          "email":email,
                          "age":age
                          }
            clients.append(new_client)
        with open("clients.json","w") as file:
            json.dump(clients,file,indent=4)

elif choice =="3":
    with open("clients.json","r") as file:
        clients = json.load(file)
        name = input("enter the name of client to searsh: ")
        

    found = False
    for client in clients:
        if client["name"].lower() == name.lower():
            found = True
            print("client found")
            print(client)
            break

    if found == False:
        print("client not found")



            




            

        
