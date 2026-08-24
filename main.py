import csv
with open('kdrama.csv', newline='') as csvfile:
    kdrama = csv.reader(csvfile)
    for row in kdrama:
        print(', '.join(row))



