import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def aggiorna_lista_strumenti(self, e):
        self._view.lista_strumenti.controls.clear()
        lista_strumenti = self._model.get_strumenti()
        if lista_strumenti is not None:
            if len(lista_strumenti) > 0:
                for strumento in lista_strumenti:
                    stato = "✅" if strumento.disponibile else "⛔"
                    self._view.lista_strumenti.controls.append(ft.Text(f"{stato} {strumento}"))
                self._view.update()
            else:
                self._view.show_alert("❌ Non ci sono strumenti nel database")
        else:
            self._view.show_alert("❌ Non è stato possibile connettersi al database")

    def cerca_strumenti_per_tipo(self, e):
        self._view.lista_strumenti_ricerca.controls.clear()
        tipo = self._view.input_tipo_strumento.value
        lista_strumenti_trovati = self._model.cerca_strumenti_per_tipo(tipo)
        if lista_strumenti_trovati is not None:
            if len(lista_strumenti_trovati) > 0:
                for strumento in lista_strumenti_trovati:
                    self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"{strumento}"))
                self._view.update()
            else:
                self._view.show_alert("❌ Nessuno strumento trovato")
        else:
            self._view.show_alert("❌ Non è stato possibile connettersi al database")
