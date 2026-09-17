import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDsRating(self):
        lista_ratings = self._model.getAllaRatings()
        for element in lista_ratings:
            self._view._ddrating1.options.append(ft.dropdown.Option(str(element)))
            self._view._ddrating2.options.append(ft.dropdown.Option(str(element)))
        self._view.update_page()




    def handleCreaGrafo(self, e):
        choice1 = self._view._ddrating1.value
        choice2 = self._view._ddrating2.value
        self._view.txt_result.controls.clear()
        self._model.buildGrafoPesato(choice1, choice2)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.num_nodi()} nodi e { self._model.num_archi()} archi"))

        lista_5_archi = self._model.five_archi_peso_maggiore()
        self._view.txt_result.controls.append(ft.Text(f"i 5 archi di peso maggiore sono:"))
        for arco in lista_5_archi:
            self._view.txt_result.controls.append(ft.Text(f"{arco[0].name} --> {arco[1].name} peso:{arco[2]["peso"]}"))

        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.numero_componenti_connesse()} componenti connesse:"))

        lista_attori = list(self._model.componente_connessa_maggiore())
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa maggiore è lunga {len(lista_attori)}:"))


        for actor in lista_attori:
            self._view.txt_result.controls.append(ft.Text( f"{actor.name}"))

        self._view.update_page()


    def handleCammino(self, e):
        self._view.txt_result.controls.append(ft.Text(f"Cerco il cammino più lungo del grafo:"))
        self._view.txt_result.controls.append(ft.Text(f"il cammino è:"))
        lista_nodi = self._model.crea_path()
        testo = ""
        cnt = 1
        for nodo in lista_nodi:
            if cnt < len(lista_nodi):
                cnt += 1
                testo+= nodo.name +" -->"
            if cnt == len(lista_nodi):
                testo+= nodo.name
        self._view.txt_result.controls.append(ft.Text(f"{testo}"))
        self._view.update_page()

