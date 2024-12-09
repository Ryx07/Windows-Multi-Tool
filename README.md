# 🚀 **Windows Multi-Tool by Ryx** 

Un potente strumento multiuso per la gestione e la manutenzione del sistema Windows. Questo tool ti permette di eseguire una serie di operazioni utili per ottimizzare e mantenere il tuo PC al massimo delle prestazioni. 💻⚙️

## 🛠️ **Funzionalità**

Il tool offre le seguenti opzioni:

1. **🛠️ Analizza e ripara i file di sistema** (`sfc /scannow`)
2. **💾 Analizza e ripara il disco** (`chkdsk /f`)
3. **🌐 Visualizza configurazione IP** (`ipconfig`)
4. **🔄 Visualizza processi in esecuzione** (`tasklist`)
5. **❌ Termina un processo** (`taskkill`)
6. **📡 Testa la connessione di rete** (`ping`)
7. **🗃️ Deframmenta il disco** (`defrag`)
8. **🌍 Monitora le connessioni di rete** (`netstat`)
9. **🖥️ Visualizza informazioni sul sistema** (`systeminfo`)
10. **🧑‍💻 Visualizza informazioni sulla CPU** (`wmic`)
11. **🔑 Visualizza la Product Key di Windows**
12. **📊 Visualizza risorse di sistema**
13. **⚙️ Gestisci i servizi di Windows**
14. **🛡️ Visualizza stato del firewall di Windows**
15. **🔧 Configura le impostazioni IP** (`ncpa.cpl`)
16. **🔄 Esegui aggiornamenti di Windows** (`ms-settings:windowsupdate`)
17. **🌡️ Visualizza la temperatura della CPU** (se supportata)
18. **🗂️ Esegui backup di file** (base, esempio di backup della cartella Documenti)
19. **📀 Visualizza spazio disponibile su disco**
20. **🖥️ Visualizza la versione di Windows**
21. **👥 Gestisci gli utenti di Windows** (`lusrmgr.msc`)

## 📋 **Requisiti**

- **Sistema operativo:** Windows (7, 8, 10, 11)
- **Privilegi amministrativi:** Il programma richiede privilegi di amministratore per eseguire alcune operazioni.

## 💡 **Installazione**

### 1. **Clona o scarica il repository:**

Puoi scaricare il tool come file `.zip` o clonare il repository direttamente sul tuo computer.

```bash
git clone https://github.com/ryx07/windows-multi-tool.git
```

### 2. **Installa le dipendenze:**

Assicurati di avere Python installato sul tuo sistema (Python 3.7 o versioni successive). Puoi installare le librerie necessarie eseguendo:

```bash
pip install pyfiglet colorama
```

### 3. **Esegui il programma:**

Per eseguire il programma, apri il terminale **come amministratore** e naviga nella cartella del progetto, quindi esegui:

```bash
python windows_multi_tool.py
```

In alternativa, puoi anche avviare direttamente il file `.py` da un editor di codice.

## 🖱️ **Uso**

Il programma si avvierà con una schermata iniziale che mostrerà un menu di opzioni numerate. Puoi scegliere un'operazione inserendo il numero corrispondente. Ecco come navigare:

- Inserisci il numero dell'opzione per eseguire un'operazione.
- Usa le frecce `>` e `<` per navigare tra le pagine.
- Digita `exit` per uscire dal programma.

## ⚠️ **Note**

- Alcune operazioni richiedono l'accesso come amministratore per poter funzionare correttamente.
- Le opzioni come la visualizzazione della temperatura della CPU potrebbero non essere supportate su tutte le macchine.

## 📜 **Licenza**

Questo software è rilasciato sotto la licenza **MIT**, ma con le seguenti restrizioni:

- **Modifica:** È permesso modificare il codice sorgente.
- **Redistribuzione:** Non è consentita la redistribuzione o la vendita del software modificato o non modificato.
- **Uso personale:** Puoi utilizzare il software per scopi personali.

## 🧑‍💻 **Autore**

**Ryx**

- Instagram: [@ryx.exe](https://www.instagram.com/ryx.exe/)
- Discord: [@3chf](https://discord.com/users/3chf)

## 🤝 **Contribuire**

Se desideri contribuire al progetto, fai un fork del repository, aggiungi nuove funzionalità, correggi bug, e invia una pull request. Sarà apprezzato! 😄
