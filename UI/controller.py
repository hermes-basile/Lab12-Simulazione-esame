import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.result1 = None
        self.result2 = None

    def fillDDsRating(self):
        self._view._ddrating1.options.clear()
        self._view._ddrating2.options.clear()
        self._view._ddrating1.value = None
        self._view._ddrating2.value = None
        self.result1 = None
        self.result2 = None

        for i in range(1, 101):
            i_new = i/10
            self._view._ddrating1.options.append(
                ft.dropdown.Option(text = i_new,
                                   data = i_new,
                                   on_click = self.readResult1 ))


            self._view._ddrating2.options.append(
                ft.dropdown.Option(text= i_new,
                                   data = i_new,
                                   on_click = self.readResult2 )
            )

        self._view.update_page()

    def readResult1(self, e):
        if e.control.data is None:
            self.result1= None
        else:
            self.result1 = float(e.control.data)
        print(self.result1)
        self.check_btn_not_disabled()



    def readResult2(self, e):
        if e.control.data is None:
            self.result2 = None
        else:
            self.result2 = float(e.control.data)
        print(self.result2)
        self.check_btn_not_disabled()


    def check_btn_not_disabled(self):
        if self.result1 is not None and self.result2 is not None:
            self._view._btnCreaGrafo.disabled = False
        self._view.update_page()



    def handleCreaGrafo(self, e):
        N = 5
        self._view.txt_result.controls.clear()
        rangeA = self.result1
        rangeB = self.result2
        self._model.buildGrafoPesato(rangeA , rangeB)
        self._view.txt_result.controls.append(ft.Text(
            f"grafo corettamente creato, abbiamo {self._model.num_nodi()} nodi e {self._model.num_archi()} archi.", color = "green"))
        self.top_N_archi(N)
        self.stampa_n_componente_connessa()
        self.componente_connessa_maggiore()
        self.elenco_attori_CCM()

        self._view.update_page()


    def top_N_archi(self, N):
        lista_ordinata = self._model.takeFirst5()
        if len(lista_ordinata) >= N:
            for i in range(0,N):
                arco = lista_ordinata[i]
                nodo1 = arco[0]
                nodo2 = arco[1]
                peso = arco[2]
                attore1 = nodo1.name
                attore2 = nodo2.name
                self._view.txt_result.controls.append(ft.Text(
                    f"{attore1} --> {attore2} : {peso}"
                ))
                self._view.update_page()

    def stampa_n_componente_connessa(self):
        n_componenti = self._model.numero_componenti_connesse()
        self._view.txt_result.controls.append(ft.Text(
            f"il numero delle componenti connesse è di {n_componenti}"
        ))

    def componente_connessa_maggiore(self):
        componente_magg = self._model.componente_connessa_maggiore()
        self._view.txt_result.controls.append(ft.Text(
            f"la componente connessa maggiore è di {componente_magg}"
        ))

    def elenco_attori_CCM(self):
        lista_nomi = self._model.elenco_componente_connessa_maggiore()
        for nome in lista_nomi:
            self._view.txt_result.controls.append(ft.Text(nome))






    def handleCammino(self, e):
        pass