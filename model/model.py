import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):

        lista_all_nodi = DAO.getAllActor()
        self.idMapActor= {}
        for nodo in lista_all_nodi:
            self.idMapActor[nodo.id] = nodo
        self._grafo = nx.Graph()




    def buildGrafoPesato(self, rangeA, rangeB):
        self._grafo.clear()
        lista_nodi = []

        lista_id_nodi = DAO.getAllNodi(rangeA, rangeB)
        for actor_id in lista_id_nodi:
            nodo_oggetto = self.idMapActor[actor_id]
            lista_nodi.append(nodo_oggetto)
        #nodi
        self._grafo.add_nodes_from(lista_nodi)

        self.addEdges(rangeA, rangeB)

    def addEdges(self,rangeA, rangeB):

        connessione_attori = DAO.getAllConnessioni(rangeA, rangeB) #(u_id, v_id)
        for connessione in connessione_attori:
            if connessione[0] in self.idMapActor.keys() and connessione[1] in self.idMapActor.keys():
                u = self.idMapActor[connessione[0]]
                v = self.idMapActor[connessione[1]]
                peso_sporco = connessione[2]
                peso_pulito = int(peso_sporco.replace("$","").strip())
                if u in self._grafo and v in self._grafo:
                    if not self._grafo.has_edge(u,v):
                        self._grafo.add_edge(u, v, weight = peso_pulito)
                    else:
                        self._grafo[u][v]["weight"] += peso_pulito

    def takeFirst5(self):
        lista_archi = list(self._grafo.edges(data= True))
        lista_archi_ordinata = sorted(lista_archi, key = lambda arco: arco[2]["weight"], reverse=True)
        return lista_archi_ordinata

    def numero_componenti_connesse(self):
        return nx.number_connected_components(self._grafo)

    def componente_connessa_maggiore(self):
        set_nodi_componente_connessa_magg = max(nx.connected_components(self._grafo), key=len)
        return len(set_nodi_componente_connessa_magg)

    def elenco_componente_connessa_maggiore(self):
        lista_nomi = []
        lista_nodi_componente = list(max(nx.connected_components(self._grafo), key=len))
        for nodo in lista_nodi_componente:
            nome = nodo.name
            lista_nomi.append(nome)
        return lista_nomi

    def calcola_path(self):
        self.soluzione = []
        for nodo in self._grafo.nodes():
            self.ricorsione([nodo])
        return self.soluzione

    def ricorsione(self, parziale):

        #termina quando non posso aggiungere più nodi

        #ottimizzazione
        if len(parziale) > len(self.soluzione):
            self.soluzione = copy.deepcopy(parziale)

        vicini_di_ultimo = self._grafo.neighbors(parziale[-1])
        for vicino in vicini_di_ultimo:
            if vicino not in parziale:
                if self.is_lower_age(parziale[-1], vicino):

                    parziale.append(vicino)
                    self.ricorsione(parziale)
                    parziale.pop()


    def is_lower_age(self, ultimo, vicino):
        if ultimo.date_of_birth < vicino.date_of_birth:
            return True
        return False










    def num_nodi(self):
        return len(self._grafo.nodes)

    def num_archi(self):
        return len(self._grafo.edges)