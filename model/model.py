import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.soluzione1 = None
        lista_all_actor = DAO.getAllActor()
        self.idMapActor ={}
        for actor in lista_all_actor:
            self.idMapActor[actor.id_attore] = actor

        self._grafo = nx.Graph()

    def getAllaRatings(self):
        ratings = DAO.getAllRatings()
        return ratings


    def buildGrafoPesato(self, rangeA, rangeB):
        self._grafo.clear()
        lista_id = DAO.getActorValutation(rangeA,rangeB)
        lista_nodi = []
        for nome_id in lista_id:

            if nome_id in self.idMapActor:
                    nodo_actor = self.idMapActor[nome_id]
                    if nodo_actor not in lista_nodi:
                        lista_nodi.append(nodo_actor)
        # nodi
        self._grafo.add_nodes_from(lista_nodi)
        self.addEdges(rangeA, rangeB)

    def addEdges(self, rangeA, rangeB):
        lista_connessioni = DAO.getAllConnessioni(rangeA,rangeB)
        for connessione in lista_connessioni:
            if connessione[0] in self.idMapActor.keys() and connessione[1] in self.idMapActor.keys():
                u = self.idMapActor[connessione[0]]
                v = self.idMapActor[connessione[1]]
                peso_sporco = connessione[2]
                peso_pulito = int(peso_sporco.replace("$","").strip())
                if u in self._grafo and v in self._grafo:
                    if self._grafo.has_edge(u,v):
                        self._grafo[u][v]["peso"] += peso_pulito
                    else:
                        self._grafo.add_edge(u, v, peso = peso_pulito)


    def five_archi_peso_maggiore(self):
        lista_5_magg = []
        lista_archi = list(self._grafo.edges(data=True))
        lista_archi_ordinata = sorted(lista_archi, key=lambda elemento_lista: elemento_lista[2]["peso"], reverse=True)
        for i in range(0,6):
            lista_5_magg.append(lista_archi_ordinata[i])
        return lista_5_magg

    def numero_componenti_connesse(self):
        return nx.number_connected_components(self._grafo)

    def componente_connessa_maggiore(self):
        return max(nx.connected_components(self._grafo), key=len)

    def crea_path(self):
        self.soluzione1 = []
        for nodo in self._grafo.nodes():
            self.ricorsione1([nodo])
        return self.soluzione1

    def ricorsione1(self, soluzione_parziale):

        if len(soluzione_parziale) > len(self.soluzione1):
            self.soluzione1 = copy.deepcopy(soluzione_parziale)

        for vicino in self._grafo.neighbors(soluzione_parziale[-1]):

            if vicino not in soluzione_parziale:

                soluzione_parziale.append(vicino)
                self.ricorsione1(soluzione_parziale)
                soluzione_parziale.pop()

    def crea_path_eta(self):
        self.soluzione = []

        for nodo in self._grafo.nodes():
            self.ricorsione([nodo])
        return self.soluzione
    def ricorsione(self, parziale):

        if len(parziale) > len(self.soluzione):
            self.soluzione = copy.deepcopy(parziale)

        for vicino in self._grafo.neighbors(parziale[-1]):
            if vicino not in parziale:
                if vicino.date_of_birth > parziale[-1].date_of_birth:
                    parziale.append(vicino)
                    self.ricorsione(parziale)
                    parziale.pop()








    def num_nodi(self):
        return len(self._grafo.nodes)

    def num_archi(self):
        return len(self._grafo.edges)
