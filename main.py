# pelo curto?
# perna curta?
# late?
cachorro1 = [1, 0, 1]
cachorro2 = [0, 0, 1]
cachorro3 = [1, 1, 1]
cachorro4 = [0, 0, 0]

gato1 = [0, 0, 0]
gato2 = [1, 0, 0]
gato3 = [0, 0, 1]
gato4 = [0, 1, 0]

dados_de_treino = [cachorro1, cachorro2, cachorro3, cachorro4, gato1, gato2, gato3, gato4]
dados_classe = [1, 1, 1, 1, 0, 0, 0, 0,]

from sklearn.svm import LinearSVC

modelo = LinearSVC(dual=True)
modelo.fit(dados_de_treino, dados_classe)
animal1 = [0, 0, 0]
animal2 = [1, 1, 1]
animal3 = [1, 0, 1]
animal4 = [1, 1, 0]

teste = [animal1, animal2, animal3, animal4]

previsoes = modelo.predict(teste)
resultado = [1, 1, 1, 0]

previsoes == resultado

from sklearn.metrics import accuracy_score

taxa_de_acerto = accuracy_score(resultado, previsoes)

print("acerto=", taxa_de_acerto * 100, "%")

print(previsoes)