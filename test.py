from model.model import Model

modello_prova = Model()
#print(modello_prova.idMapActor.values())
modello_prova.buildGrafoPesato(1.2,2.7)
print(f"i nodi sono {modello_prova.num_nodi()}")
print(f"il numero di archi è {modello_prova.num_archi()}")
#print(list(modello_prova._grafo.edges(data=True)))

#print(list(modello_prova.componente_connessa_maggiore()))
print(modello_prova.crea_path())



