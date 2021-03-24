import csv

header = ["place", "name", "age"]
with open("city.csv", "w")as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "delhi", "name": "ram", "age": 56})
    write.writerow({"place": "mumbai", "name": "raj", "age": 44})
    write.writerow({"place": "kochi", "name": "devika", "age": 21})
    write.writerow({"place": "bangalore", "name": "das", "age": 36})
with open("city.csv", "r") as file:
    c = csv.DictReader(file);
    n = input("Enter the column name you want(place,name,age):")
    for i in c:
        print(i[n])
