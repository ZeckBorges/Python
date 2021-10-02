import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('Animais.csv')
#print(df)
dados = np.array(df.drop("Animal", 1))
rotulos = np.array(df["Animal"])
#print(rotulos)
#print(dados)
kn = KNeighborsClassifier(5)
kn.fit(dados, rotulos)

#animal = [1, 1, 1]

#resultado = kn.predict([animal])

#print("O resultado é:", resultado)

#print("Animal:", kn.predict([[1,1,0]]))
#print("Animal:", kn.predict([[0,1,0]]))
#print("Animal:", kn.predict([[1,0,1]]))
#print("Animal:", kn.predict([[0,0,1]]))
#print("Animal:", kn.predict([[1,1,1]]))
#print("Animal:", kn.predict([[0,1,1]]))

entrada = []
print("Digite 1 para verdadeiro ou 0 para falso")
entrada.append(int(input("Pelo longo?")))
entrada.append(int(input("Perna curta?")))
entrada.append(int(input("Faz au-au?")))

resultado = kn.predict([entrada])
print("O seu animal é:", resultado[0])


