import csv

class Drama: 

    def __init__(self, data):

        self.namn = data[0]
        self.rankning = data[1]
        self.data = data

    def __str__(self):
        return f"""Draman "{self.namn}" från {self.data[7]} fick rankningen {self.rankning}!"""

    def __lt__(self, other):
        return self.rankning < other.rankning
    def actors(self):
        return f" Skådespelarna i dramat var: {self.data[2]}"
    def first_director(self):
        directors = self.data[5]
        directors = directors.split(", ")
        director1 = directors[0]
        return f"Den första regisören är: {director1}"



def read_drama():
    with open('kdrama.csv', newline='') as csvfile:
        kdrama = csv.reader(csvfile)
        rubriker = next(kdrama)
        draman = []
        for rad in kdrama:
            draman.append(Drama(rad))
    return draman



def find_drama_from_year(list, year):
    drama_from_year = []
    for drama in list:
        if int(drama.data[7]) == year:
            drama_from_year.append(drama)

    return len(drama_from_year)  


drama = read_drama()
print(drama[0])
print(drama[1])
print(drama[0]<drama[1])
print(drama[0].actors())
print(drama[1].actors())
print(drama[0].first_director())
print(drama[1].first_director())

number_of_dramas_from_2020 = find_drama_from_year(drama,2020)
print(number_of_dramas_from_2020)



