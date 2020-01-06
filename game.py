import csv
csv_file = csv.reader(open('game.csv','r'))
print(csv_file)
for game in csv_file:
    print(game)