import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def riempiDropDown(self):
        #se lo chiamo dopo un azione deve essere (self, e), guarda esame flights
        #prima di avviarlo 3 pulizie
        self._view.DDNOME.options.clear()
        self._view.DDNOME.value = None
        self.result1 = None #salvato nell'init

        lista_da_caricare = [1,2,3,4]

        for elemento in lista_da_caricare:
            self._view.ddNodo.options.append(
                ft.dropdown.Option(
                    text=str(elemento),
                    data=elemento,
                    on_click=self.readResult1
                )
            )

    def readResult1(self, e):
        if e.control.data is None:
            self.result1 = None
        else:
            self.result1 = float(e.control.data)


        #se i dropdown sono 2 e devono essere entrambi selezionati per
        # attivare un pulsante, sia qui, sia in readresult2 devo fare un metodo
        #         self.check_btn_not_disabled() come in esame lab12




    #CREAZIONE GRAFO STANDARD
    def handleCreaGrafo(self, e):
        # ============================================================
        # CREAZIONE GRAFO SENZA FILTRI
        # ============================================================

        self._view.txt_result.controls.clear()

        # Creare il grafo da model
        self._model.buildWeightGraphAllNodes()

        #scrivere all'utente che è tutto ok
        self._view.txt_result.controls.append(
            ft.Text(
                f"Grafo creato con "
                f"{self._model.num_nodi()} nodi e "
                f"{self._model.num_archi()} archi."
            )
        )

        # Se dopo la creazione del grafo bisogna riempire i dropdown
        self.riempi_dropdown()

        self._view.update_page()

    #CONTROLLI SULL'INSERIMENTO DI TESTO DELL'UTENTE
    def handleDopoTXTin(self, e):
        self._view.txt_result.controls.clear()

        txt_in = self._view.NOMEVIEW.value


        if txt_in is None or txt_in.strip() == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(
                "Devi inserire qualche valore valido", color="red"))
            self._view.update_page()
            return

        try:
            number = int(txt_in)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text(
                "Attenzione, gli unici caratteri ammessi sono da 0 a 9, puoi inserire solo numeri", color="red"))
            self._view.NOMEVIEW.value = ""
            self._view.update_page()
            return

    def handleCammino(self, e):
        pass