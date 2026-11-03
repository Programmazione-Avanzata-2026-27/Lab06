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
        # Il Controller mantiene i riferimenti sia al Modello (dati) che alla View (interfaccia)
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
    def mostra_strumenti(self, e):
        # 1. Chiamo il metodo del Modello per interrogare il database e ottenere la lista di oggetti Strumento
        strumenti = self._model.get_strumenti()

        # 2. Se il Modello restituisce None, significa che la connessione al DB è fallita: mostro un popup di errore
        if strumenti is None:
            self._view.show_alert("Errore di connessione al database!")
            return

        # 3. Pulisco la ListView prima di inserire i nuovi elementi, altrimenti cliccando più volte "Mostra" la lista si duplicherebbe
        self._view.lista_strumenti.controls.clear()

        # 4. Se la lista è vuota avviso l'utente, altrimenti aggiungo ogni strumento alla ListView come controllo grafico ft.Text
        if len(strumenti) == 0:
            self._view.show_alert("Nessuno strumento presente nel database.")
        else:
            for s in strumenti:
                # str(s) richiama automaticamente il metodo __str__ della classe Strumento
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))

        # 5. Aggiorno la View per disegnare a schermo i nuovi elementi appena aggiunti alla ListView
        self._view.update()

    def cerca_strumenti(self, e):
        # 1. Prelevo il testo scritto dall'utente nel TextField della View; .strip() rimuove eventuali spazi vuoti prima e dopo
        tipo = self._view.input_tipo_strumento.value.strip()

        # 2. Validazione dell'input: se la stringa è vuota, blocco l'operazione e mostro un Alert senza interrogare inutilmente il DB
        if not tipo:
            self._view.show_alert("Inserire un tipo di strumento da cercare!")
            return

        # 3. Chiedo al Modello di eseguire la query filtrata per il tipo inserito
        strumenti = self._model.cerca_strumenti_per_tipo(tipo)

        # 4. Controllo se c'è stato un problema di connessione al database MySQL
        if strumenti is None:
            self._view.show_alert("Errore di connessione al database!")
            return

        # 5. Svuoto la ListView dedicata alla ricerca per rimuovere i risultati di eventuali ricerche precedenti
        self._view.lista_strumenti_ricerca.controls.clear()

        # 6. Se non ci sono strumenti di quel tipo mostro un Alert, altrimenti popolo la ListView con i controlli ft.Text
        if len(strumenti) == 0:
            self._view.show_alert(f"Nessuno strumento trovato per il tipo: {tipo}")
        else:
            for s in strumenti:
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))

        # 7. Aggiorno la pagina Flet per mostrare i risultati a schermo
        self._view.update()