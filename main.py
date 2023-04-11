import pandas as pd
import matplotlib.pyplot as plt


def run():
    # Leer el archivo CSV y obtener los datos del campeón
    data = pd.read_csv('stats.csv', sep=';')
    data['Win %'] = data['Win %'].str.strip('%').astype(float)
    data['Pick %'] = data['Pick %'].str.strip('%').astype(float)
    data['Ban %'] = data['Ban %'].str.strip('%').astype(float)
    
    
    # Obtener el nombre del campeón y su información
    champ_name = input('Indica el nombre del campeón: ').title()
    champ_info = data[data['Name'] == champ_name]
    
    # Verificar que se haya encontrado la información del campeón
    if not champ_info.empty:
        # Generar la gráfica de torta para el campeón
        labels = ['Pick %', 'Ban %', 'Win %']
        values = [champ_info['Pick %'].values[0], champ_info['Ban %'].values[0], champ_info['Win %'].values[0]]
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.set_title(champ_name)
        plt.savefig(f'./pngs/{champ_name}.png')
        plt.close()
    else:
        print(f'El campeón {champ_name} no se encuentra en la lista.')
        return


if __name__ == '__main__':
    run()







