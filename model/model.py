from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
- Rappresenta la struttura dati

- Si occupa di gestire lo stato dell'applicazione

- Interagisce con il database

'''


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    # Il decoratore @property trasforma il metodo in un "getter", permettendo di leggere
    # l'attributo privato _nome dall'esterno scrivendo semplicemente oggetto.nome
    @property
    def nome(self):
        return self._nome

    # Il decoratore @nome.setter permette di modificare l'attributo privato _nome
    # dall'esterno scrivendo oggetto.nome = "Nuovo Nome"
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # 1. Apro la connessione al database MySQL tramite la funzione fornita in DB_connect
        cnx = get_connection()
        # Controllo di sicurezza: se MySQL è spento o la connessione fallisce, restituisco None
        if cnx is None:
            return None

        # 2. Creo il cursore con dictionary=True: così ogni riga letta dal DB sarà un dizionario Python
        # dove le chiavi sono i nomi delle colonne della tabella (es. row["codice"], row["marca"])
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM strumento"
        cursor.execute(query)

        # 3. Scorro i risultati della query e trasformo ogni riga del DB in un oggetto Strumento (ORM manuale)
        risultato = []
        for row in cursor:
            strumento = Strumento(
                row["codice"],
                row["tipo"],
                row["marca"],
                row["anno_acquisto"],
                row["valore"],
                bool(row["disponibile"])
                # Converto il valore TINYINT(1) di MySQL (0 o 1) in un booleano Python (True/False)
            )
            risultato.append(strumento)

        # 4. Chiudo sempre sia il cursore che la connessione per liberare le risorse del server MySQL
        cursor.close()
        cnx.close()
        return risultato

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # 1. Apro la connessione e verifico che sia attiva
        cnx = get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)

        # 2. Uso una query parametrica con il segnaposto %s invece di concatenare le stringhe con f-string.
        # Questo protegge il database da attacchi di tipo SQL Injection e gestisce in automatico gli apici.
        query = "SELECT * FROM strumento WHERE tipo = %s"
        # Il secondo argomento di execute() deve essere obbligatoriamente una tupla: per questo c'è la virgola in (tipo,)
        cursor.execute(query, (tipo,))

        # 3. Costruisco la lista di oggetti Strumento filtrati
        risultato = []
        for row in cursor:
            strumento = Strumento(
                row["codice"],
                row["tipo"],
                row["marca"],
                row["anno_acquisto"],
                row["valore"],
                bool(row["disponibile"])
            )
            risultato.append(strumento)

        # 4. Chiudo cursore e connessione prima di restituire la lista al Controller
        cursor.close()
        cnx.close()
        return risultato