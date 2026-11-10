import csv

with open("products.csv", "r", encoding="utf-8") as file:
    content = csv.DictReader(file)
    totals =[]

    for row in content :
        total = float(row["price"]) * float(row["quantity"])
        print(row["product"]," : ",total)
        totals.append(total)

    print("total : ",sum(totals))



        
        
    
    
        
