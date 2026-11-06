# Lab 06 - Soluzione

#### Argomenti

- Utilizzo pacchetto `Flet` di Python (suggerita v1.0.4)
- Utilizzo Pattern MVC
- Utilizzo dei Package
- Utilizzo di mysql-connector-python (suggerita v8.4.0)

---
> **❗ ATTENZIONE:**
>  Ricordare di effettuare il **fork** del repository principale, quindi clonare su PyCharm il **repository personale**
> (https://github.com/my-github-username/Lab06) e non quello principale.
>
> In caso di dubbi consultare la guida caricata nel lab02:
> https://github.com/Programmazione-Avanzata-2026-27/Lab02/blob/main/Guida.pdf
>

### Setup del Database tramite XAMPP e DBeaver
1. **Installazione del connettore Python**
   - Installare `mysql-connector-python` (v8.4.0) dal terminale di PyCharm con il comando:

     ```bash
     pip install mysql-connector-python==8.4.0
     ```

   - In alternativa, utilizzare la GUI di PyCharm:

     `File → Settings → Python → Interpreter → + → Cercare "mysql-connector-python" + Selezionare versione 8.4.0 → Install Package`

2. **Avvio del server MySQL con XAMPP**
   1. Per utilizzare il database è necessario installare, se non già fatto, [XAMPP](https://www.apachefriends.org/it/download.html) (v8.5.12).
   2. Aprire il pannello di controllo di **XAMPP** e avviare **MySQL** cliccando sul relativo pulsante `Start`.
   ![xampp.png](img/xampp.png)

3. **Avvio di DBeaver e creazione della connessione**
   1. Una volta avviato MySQL tramite XAMPP, aprire **DBeaver**.
   2. Selezionare `Database → Nuova Connessione` (icona a forma di plug, in alto a sinistra).
   3. Nella finestra che si apre, scegliere **MySQL** dall'elenco dei database supportati e cliccare su `Avanti`.
   ![nuova_connessione.png](img/nuova_connessione.png)

4. **Configurazione della connessione**
   1. Inserire i seguenti parametri:
      - **Host**: `localhost`
      - **Port**: `3306` (porta predefinita di MySQL)
      - **Database**: lasciare vuoto per creare una connessione generale al server
      - **Username**: `root`
      - **Password**: lasciare vuoto, se non è stata impostata in XAMPP
   2. Cliccare su `Tenta di Stabilire una Connessione` per verificare che DBeaver riesca a collegarsi correttamente al server MySQL.
   3. Se la connessione è riuscita, premere `Fine`.
   ![configurazione_connessione.png](img/configurazione_connessione.png)

5. **Creazione del database a partire dallo script fornito**
   1. Nel pannello di sinistra (`Navigatore Database`), cliccare con il tasto destro sulla connessione `localhost` e selezionare `Editor SQL → Script SQL`.
   2. Copiare e incollare il contenuto del file `deposito_strumenti.sql` fornito nella traccia sul file script che si apre.
   3. Quindi selezionare il pulsante `Esegui Script SQL`. 
   ![editor_script.png](img/editor_script.png)
   4. Al termine, nel pannello di navigazione sarà visibile il database e tutte le sue tabelle (se necessario, aggiornare la vista del database).
   ![refresh_&_check_database.png](img/refresh_%26_check_database.png)

7. **Verifica del contenuto**
   1. Espandere le tabelle per visualizzarne la struttura.
   2. Per verificare i dati, cliccare con il tasto destro su una tabella (ad esempio `strumento`) e selezionare `Vedi Dati`.
   3. I dati importati saranno visibili in forma tabellare.

8. **(Facoltativo) Query di prova**
   1. Cliccare con il tasto destro sul database e scegliere `SQL Editor → New Script/SQL Script`.
   2. Eseguire la query:

      ```sql
      SELECT * FROM strumento;
      ```

   3. Se gli strumenti vengono visualizzati, il database è pronto per essere utilizzato dall'applicazione Python tramite `mysql-connector-python`.

---

## Deposito di Strumenti Musicali - MVC e Database
Implementare un'applicazione per la gestione di un deposito di strumenti musicali (già visto nel Lab03 e Lab05).
L'applicazione deve consentire di:
- Visualizzare gli strumenti presenti nel deposito;
- Ricercare tutti gli strumenti di un certo tipo.

Prestare attenzione alla gestione di tutte le possibili condizioni di errore. Fare uso del pattern MVC,
utilizzando i pacchetti `flet` e `mysql-connector-python`, come spiegato a lezione.

### Implementazione
Realizzare un'interfaccia grafica con `flet` organizzata come segue, dall'alto verso il basso:
![layout.png](img/layout.png)

La proposta di interfaccia include:
- Titolo pagina ("Lab06") – già fatto ✅
- Pulsante per cambiare tema (default dark mode) utilizzando `Switch` – già fatto ✅
- **Sezione 1**: Intestazione Deposito - già fatto ✅
  - Un controllo `Text` con il nome del deposito.
  - Un controllo `Text` con il nome del responsabile.
- **Sezione 2**: Modificare il nome del responsabile - già fatto ✅
  - Un controllo `Text` con testo "Modifica Informazioni".
  - Un controllo `TextField` per modificare il nome.
  - Un controllo `Button` "Conferma" per confermare la modifica.
- **Sezione 3**: Lista degli Strumenti - TODO 📝
  - Un controllo `Text` con testo "Strumenti".
  - Un controllo `Button` "Mostra" per mostrare tutti gli strumenti presenti nel database.
  - Un contenitore `ListView` da popolare con gli strumenti che vengono letti dal database.
- **Sezione 4**: Ricerca strumento per tipo - TODO 📝
  - Un controllo `Text` con testo "Cerca Strumento per Tipo".
  - Un controllo `TextField` per inserire il tipo dello strumento da cercare (es. "Chitarra").
  - Un controllo `Button` "Cerca" per avviare la ricerca.
  - Un contenitore `ListView` da popolare con l'elenco degli strumenti trovati nel database dato il tipo inserito
  (nel database possono esserci più strumenti dello stesso tipo).

---

## Materiale Fornito
Il repository del lab06 è organizzato con la struttura ad albero mostrata di seguito e contiene tutto il necessario per
svolgere il laboratorio:

```code
Lab06/
├── database/
│   ├── __init__.py
│   ├── connector.cnf
│   └── DB_connect.py
│
├── model/
│   ├── __init__.py
│   ├── strumento.py
│   ├── model.py (DA MODIFICARE)
│   └── prestito.py
│
├── UI/
│   ├── __init__.py
│   ├── alert.py
│   ├── controller.py (DA MODIFICARE)
│   └── view.py (DA MODIFICARE)
│
├── deposito_strumenti.sql (DA IMPORTARE CON DBeaver)
└── main.py (DA ESEGUIRE)
 ```

- Il file `deposito_strumenti.sql` da importare tramite **DBeaver** per creare e popolare il database.
- Il file `main.py` da eseguire per far partire l'applicazione.
- Il package **_database_** contiene il file `DB_connect.py` che effettua la connessione con il database (nel file `connector.cnf` sono contenute le info
  necessarie per effettuare la connessione al database).
- Il package **_model_** contiene i file che implementano il modello, ovvero la struttura dati rappresentata dalla classe
`DepositoStrumenti` (`model.py`), insieme alle classi `Strumento` (`strumento.py`) e `Prestito` (`prestito.py`),
che ne costituiscono e supportano il funzionamento.
- Il package **_UI_** contiene: il file `view.py` che definisce la classe `View`, che implementa l'interfaccia grafica
utilizzando `flet` e il file `controller.py` contenente la classe `Controller` che funge da intermediario tra la View
e il Modello. Inoltre, qui è presente il file `alert.py` in cui è definita la classe `AlertManager` usata per mostrare
gli alert mediante il metodo `show_alert()`.
