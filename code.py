import csv 

data = []

with open ("brown_dwarfs.csv", "r") as f:
    csv_reader = csv.reader(f)

    for read_row in csv_reader:
        data.append(read_row)

headers = data[1]
star_data = data[2:]

for data_point in star_data :
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order 
star_data.sort(key=lambda star_data: star_data[2])

with open("brown_dwarfs_sorted.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(star_data)