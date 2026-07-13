import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.lista_nodi_totale = DAO.getAllNodes()

        self.idMapObject = {}
        for nodo in self.lista_nodi_totale:
            self.idMapObject[nodo.id] = nodo

        self._grafo = nx.Graph()

    #GRAFO CHE CONTIENE TUTTI I NODI
    def buildWeightGraphAllNodes(self):
        self._grafo.clear()

        self._grafo.add_nodes_from(self.lista_nodi_totale)

        self.addWeightEdges()
    #GRAFO CHE NON CONTIENE TUTTI I NODI PERCHE' FILTRA
    def buildWeightGraphFiltered(self, condizione_nodo1, condizione_nodo2):
        self._grafo.clear()

        lista_id = DAO.getFilteredNode(condizione_nodo1, condizione_nodo2)

        lista_nodi = []

        for id_nodo in lista_id:
            nodo = self.idMapObject[id_nodo]
            lista_nodi.append(nodo)

        self._grafo.add_nodes_from(lista_nodi)

        self.addWeightEdges()

    #SE RIESCO, DENTRO A CREARE UNA LISTA DI TUPLE con la query"(u.id, v.id, peso)"
    def addWeightEdges(self):
        archi_pesi = DAO.getArchiConPeso() # (u_id, v_id, peso)

        for tupla in archi_pesi:
            if tupla[0] in self.idMapObject.keys() and tupla[1] in self.idMapObject.keys():
                u = self.idMapObject[tupla[0]]
                v = self.idMapObject[tupla[1]]
                # attenzione al peso: se si somma deve essere int, sennò ci sono problemi con l'else sotto
                peso = tupla[2]
                if u in self._grafo and v in self._grafo:
                    #se non restituisco il peso completo nella query,
                    #sennò basta il primo if
                    if not self._grafo.has_edge(u, v):
                        self._grafo.add_edge(u, v, weight=peso)
                    else:
                        self._grafo[u][v]["weight"] += peso



    #METODI NETWORKX


    # CON SOURCE SI INTENDE UN NODO SU CUI VOGLIAMO FARE UN'OPERAZIONE
    # è il nodo di partenza ed è un Oggetto nodo
    def vicini_diretti_di_un_nodo(self, source):
        """Trovare i nodi a distanza 1 da source, com'è scritta ritorna una
        lista di nodi"""
        return list(self._grafo.neighbors(source))

        # COMPONENTE CONNNESSA &CO

    def componente_connessa(self, source):
        """Trovare tutti i nodi raggiungibili da source, ordine non importante
        restituisce un set, quindi se voglio una lista devo fare list(..)"""
        return nx.node_connected_component(self._grafo, source)

    def grafo_connesso(self):
        """Restituisce True se tutto il grafo è connesso."""
        return nx.is_connected(self._grafo)

    def numero_componenti_connesse(self):
        """trova, dentro un grafo, quante componenti connesse ci sono
        RITORNA PROPRIO IL NUMERO"""
        return nx.number_connected_components(self._grafo)

    def dimensione_componente_connessa_maggiore(self):
        """trova, dentro un grafo, la componente connessa maggiore,
        ATTENZIONE RITORNA UN SET, (senza len, con len il numero)"""
        return len(max(nx.connected_components(self._grafo), key=len))

    def ottieni_un_grafo_dalla_componente_maggiore(self, componente_maggiore):
        """restituisce un grafo nuovo, della componente"""
        self._grafo.subgraph(componente_maggiore).copy()

    def trova_il_percorso_con_meno_archi_tra_2_nodi(self, u, v):
        """ritorna una lista"""
        if nx.has_path(self._grafo, u, v):
            return nx.shortest_path(self._grafo, u, v)
        return None
    def trova_il_percorso_con_meno_peso_tra_2_nodi(self, u, v):
        """ritorna una tupla con (peso_totale, lista_nodi) quindi
        (peso, [nodo1,nodo2,ecc])"""
        return nx.single_source_dijkstra(self._grafo, u, v)

    def bfs_edges(self, source_oggetto):
        """Visita in ampiezza ricavata dagli archi
        restituisce una lista di tuple [(u,v) .... ]"""
        nx.bfs_edges(self._grafo, source_oggetto)

    def bfs_tree(self, source_oggetto):
        """Visita in ampiezza completa
        restituisce un nuovo grafo, quindi per avere l'elenco dei nodi
        list(nuovo_grafo.nodes())"""
        nx.bfs_tree(self._grafo, source_oggetto)

    def dfs_edges(self, source_oggetto):
        """Visita in profondità ricavata dagli archi
        restituisce una lista di tuple [(u,v) .... ]"""
        nx.dfs_edges(self._grafo, source_oggetto)

    def dfs_tree(self, source_oggetto):
        """Visita in profondità completa"""
        nx.dfs_tree(self._grafo, source_oggetto)









    #metodi random
    def ordina_lista(self):
        lista_archi = list(self._grafo.edges(data=True))
        lista_archi_ordinata = sorted(lista_archi, key=lambda arco: arco[2]["weight"], reverse=True)
        return lista_archi_ordinata

    def pulisci_stringa(self, stringa):
        """ replace("x","y") cambia nella stringa le x con le y
        strip() leva spazi prima e dopo la stringa"""
        stringa_pulita = stringa.replace("$", "").strip()






    def num_nodi(self):
        return len(self._grafo.nodes)

    def num_archi(self):
        return len(self._grafo.edges)