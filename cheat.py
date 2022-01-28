import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def cheat(exercise):
    if exercise==1.8:
        result = (np.arange(1, 17) ** 2).reshape(2, 2, 2, 2)
        print(result)
    elif exercise==1.9:
        result = pd.read_csv('InsectSprays.csv').to_dict()
        print(result.keys())
    elif exercise==2.2:
        result = np.array([])
        for i in np.arange(3, 18, 2):
            result = np.append(result, i)
        print(result)
    elif exercise==3.2:
        data = pd.read_csv(
            "https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv")
        plt.figure()
        sns.histplot(data, x='Sex', hue='Survived', multiple='stack', color=('red', 'cyan'))
        plt.savefig("Q3.2P.2.stacked.png", dpi=300)
    else:
        print("welp")
    return result
