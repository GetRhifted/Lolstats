import matplotlib as plt

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./pngs/{labels}.png')
  plt.close()                     
  

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 250, 60]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)

  