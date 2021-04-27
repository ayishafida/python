import csv

l = []
with open("city.csv", "w")as file:
    write = csv.writer(file)
    write.writerow(["id", "place", "district"])
    limit = int(input("Enter the lines of data you want to enter:"))
    for i in range(limit):
        row_string = input("Enter data (id,place,district) separated by comma:")
        row_list = row_string.split(",")
        write.writerow(row_list)
    with open("city.csv", "r") as file:
        read = csv.reader(file)
        for row in read:
            print(row)
            l.append(",".join(row))
print(l)