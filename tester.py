from model.model import Model

modello_prova = Model()
print(len(modello_prova.idMapActor))
modello_prova.buildGrafoPesato(1.2,2.7)
print(f"provo a stampare il numero di nodi {modello_prova.num_nodi()}")
print(f"provo a stampare il numero di archi {modello_prova.num_archi()  }")
print(f"provo a stampare il numero di nodi {modello_prova.num_nodi()}")

for i in range(1,101):
    print(i/10)

#print(modello_prova._grafo.edges)
for i in range (0,10):
    print((modello_prova.takeFirst5()[i][2]["weight"]))
print(f"numero componenti connesse = {modello_prova.numero_componenti_connesse()}")
print(f"numero maggiore componente connessa = {modello_prova.componente_connessa_maggiore()}")
print(f"lista nomi della comp magg --> {modello_prova.elenco_componente_connessa_maggiore()}")

print(modello_prova.calcola_path())