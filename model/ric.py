
#CS
def cercaSoluzione(self, source):
    self._soluzione = []
    self._costo_ottimo = float("-inf")

    self.ricorsione([source])

    return self._soluzione, self._costo_ottimo


def ricorsione(self, parziale):

    possibili = []

    ultimo = parziale[-1]

    for vicino in self._grafo.neighbors(ultimo):
        if vicino not in parziale:
            if self.isAmmissibile(parziale, vicino):
                possibili.append(vicino)

    # CASO TERMINALE
    if self.isTerminale(parziale, possibili):

        costo = self.calcolaCosto(parziale)
        if costo > self._costo_ottimo:
            self._costo_ottimo = costo
            self._soluzione = parziale.copy()

    # CASO RICORSIVO
    else:
        for vicino in possibili:
            parziale.append(vicino)
            self.ricorsione(parziale)
            parziale.pop()



#-----------------------------------------------------------------------------------------

def cercaPercorsoKArchiPesoMax(self, source, k):
    self._soluzione = []
    self._costo_ottimo = float("-inf")

    self.ricorsione([source], k)

    return self._soluzione, self._costo_ottimo


def ricorsione(self, parziale, k):

    # CASO TERMINALE:
    # k archi corrispondono a k + 1 nodi
    if len(parziale) == k + 1:

        costo = nx.path_weight(
            self._grafo,
            parziale,
            weight="weight"
        )

        if costo > self._costo_ottimo:
            self._costo_ottimo = costo
            self._soluzione = parziale.copy()

    # CASO RICORSIVO
    else:
        ultimo = parziale[-1]

        for vicino in self._grafo.neighbors(ultimo):

            if vicino not in parziale:
                parziale.append(vicino)
                self.ricorsione(parziale, k)
                parziale.pop()


#-----------------------------------------------------------------------------------------


def cercaPercorsoDaSourceATargetConPesoMax(self, source, target):
    self._soluzione = []
    self._costo_ottimo = float("-inf")

    self.ricorsione([source], target)

    return self._soluzione, self._costo_ottimo


def ricorsione(self, parziale, target):

    ultimo = parziale[-1]

    # CASO TERMINALE:
    # ho raggiunto la destinazione
    if ultimo == target:

        costo = nx.path_weight(
            self._grafo,
            parziale,
            weight="weight"
        )

        if costo > self._costo_ottimo:
            self._costo_ottimo = costo
            self._soluzione = parziale.copy()

    # CASO RICORSIVO
    else:
        for vicino in self._grafo.neighbors(ultimo):

            if vicino not in parziale:
                parziale.append(vicino)
                self.ricorsione(parziale, target)
                parziale.pop()

#-----------------------------------------------------------------------------------------


def cercaPercorsoPiuLungoConDateCrescenti(self, source):
    self._soluzione = []

    self.ricorsione([source])

    return self._soluzione


def ricorsione(self, parziale):

    ultimo = parziale[-1]
    possibili = []

    for vicino in self._grafo.neighbors(ultimo):

        if vicino not in parziale:

            if ultimo.date_of_birth < vicino.date_of_birth:
                possibili.append(vicino)

    # CASO TERMINALE:
    # non posso aggiungere nessun altro nodo
    if len(possibili) == 0:

        if len(parziale) > len(self._soluzione):
            self._soluzione = parziale.copy()

    # CASO RICORSIVO
    else:
        for vicino in possibili:
            parziale.append(vicino)
            self.ricorsione(parziale)
            parziale.pop()