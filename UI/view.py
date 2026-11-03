import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
- Rappresenta l'interfaccia utente

- Riceve i dati dal MODELLO e li presenta senza modificarli

'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Elementi UI
        self.txt_titolo = None
        self.txt_responsabile = None

        # Non obbligatorio mettere già qui tutti gli elementi UI

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        """ Imposta il controller alla pagina """
        self.controller = controller

    def update(self):
        # Ricarica l'interfaccia grafica per rendere visibili a schermo le modifiche apportate ai controlli
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge Elementi di UI alla pagina e la aggiorna. """
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        # TextField per responsabile
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")

        # ListView per mostrare la lista di strumenti aggiornata (expand=True le permette di occupare lo spazio disponibile)
        self.lista_strumenti = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # TextField per ricerca strumento per tipo (salvato in self. così il Controller può leggerne il .value)
        self.input_tipo_strumento = ft.TextField(label="Tipo")

        # ListView per mostrare il risultato della ricerca strumenti per tipo
        self.lista_strumenti_ricerca = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- PULSANTI e TOGGLE associati a EVENTI ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.Button("Conferma", on_click=self.controller.conferma_responsabile)

        # Altri Pulsanti da implementare (es. "Mostra" e "Cerca")
        # Con il parametro on_click collego l'evento del clic del mouse alla relativa funzione (Event Handler) nel Controller
        pulsante_mostra_strumenti = ft.Button("Mostra", on_click=self.controller.mostra_strumenti)
        pulsante_cerca_strumento = ft.Button("Cerca", on_click=self.controller.cerca_strumenti)

        # --- LAYOUT ---
        # Aggiungo tutti i controlli alla pagina dall'alto verso il basso usando ft.Row per allinearli in orizzontale
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Visualizzazione di tutti gli strumenti
            # Uso ft.Row per affiancare l'intestazione "Strumenti" e il pulsante "Mostra", centrandoli nella pagina
            ft.Row(spacing=200,
                   controls=[ft.Text("Strumenti", size=20), pulsante_mostra_strumenti],
                   alignment=ft.MainAxisAlignment.CENTER),
            # Sotto la riga inserisco il contenitore ListView che verrà popolato dinamicamente dal Controller
            self.lista_strumenti,
            ft.Divider(),

            # Sezione 4: Ricerca degli strumenti filtrati per tipo
            ft.Text("Cerca Strumento per Tipo", size=20),
            # Affianco la casella di testo (input_tipo_strumento) e il pulsante "Cerca" in una riga centrata
            ft.Row(spacing=200,
                   controls=[self.input_tipo_strumento, pulsante_cerca_strumento],
                   alignment=ft.MainAxisAlignment.CENTER),
            # Sotto la riga inserisco la seconda ListView dedicata ai risultati della ricerca
            self.lista_strumenti_ricerca
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()