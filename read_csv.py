import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ';')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header,row)
      champ_dict = {key : value for key, value in iterable}
      data.append(champ_dict)
    return data
     
    

if __name__ == '__main__':
  data = read_csv('./lolstats/stats.csv')
  print(data[0])