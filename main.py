import os
import sys
import subprocess
import time
import pyfiglet
from colorama import init, Fore, Back, Style

init(autoreset=True)

def clear_screen():
    os.system('cls')

os.system('title Windows multi-tool by Ryx / Instagram: @ryx.exe / Discord: @3chf')

def print_ascii_title(font="slant"):
    ascii_title = pyfiglet.figlet_format("Multi Tool", font=font)
    print(Fore.MAGENTA + ascii_title)

def is_admin():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return subprocess.run("net session", capture_output=True, text=True).returncode == 0

def check_admin_privileges():
    if not is_admin():
        print(Fore.RED + "Il programma non è eseguito come amministratore. Assicurati di eseguilo con privilegi elevati.")
        time.sleep(5)
        sys.exit()

print_ascii_title("slant")

def color_gradient():
    colors = [Fore.MAGENTA, Fore.MAGENTA, Fore.CYAN, Fore.BLUE, Fore.BLUE]
    for i, color in enumerate(colors):
        print(color + " " * 100)

def run_sfc():
    print(Fore.YELLOW + "Esecuzione di 'sfc /scannow'... Attendere qualche minuto.")
    subprocess.run("sfc /scannow", shell=True)

def run_chkdsk():
    print(Fore.YELLOW + "Esecuzione di 'chkdsk /f'... Potrebbero essere necessari alcuni minuti.")
    subprocess.run("chkdsk /f", shell=True)

def run_ipconfig():
    print(Fore.GREEN + "Esecuzione di 'ipconfig'...")
    subprocess.run("ipconfig", shell=True)

def run_tasklist():
    print(Fore.CYAN + "Esecuzione di 'tasklist'...")
    subprocess.run("tasklist", shell=True)

def run_taskkill():
    pid = input(Fore.RED + "Inserisci l'ID del processo da terminare: ")
    subprocess.run(f"taskkill /PID {pid} /F", shell=True)

def run_ping():
    host = input(Fore.YELLOW + "Inserisci l'indirizzo IP o il dominio da pingare: ")
    subprocess.run(f"ping {host}", shell=True)

def run_defrag():
    drive = input(Fore.CYAN + "Inserisci la lettera del disco da deframmentare (es. C:): ")
    subprocess.run(f"defrag {drive} /O", shell=True)

def run_netstat():
    print(Fore.GREEN + "Esecuzione di 'netstat -an'...")
    subprocess.run("netstat -an", shell=True)

def run_systeminfo():
    print(Fore.GREEN + "Esecuzione di 'systeminfo'...")
    subprocess.run("systeminfo", shell=True)

def run_wmic():
    print(Fore.YELLOW + "Esecuzione di 'wmic cpu get caption' per informazioni sulla CPU...")
    subprocess.run("wmic cpu get caption", shell=True)

def run_license_info():
    print(Fore.GREEN + "Esecuzione di PowerShell per ottenere la Product Key...")
    powershell_script = """
    $key = (Get-WmiObject -Query 'SELECT * FROM SoftwareLicensingService').OA3xOriginalProductKey
    Write-Output $key
    """
    result = subprocess.run(['powershell', '-Command', powershell_script], capture_output=True, text=True)
    if result.stdout:
        print(Fore.YELLOW + "Product Key di Windows: " + result.stdout.strip())
    else:
        print(Fore.RED + "Impossibile recuperare la Product Key.")

def run_system_resources():
    print(Fore.CYAN + "Esecuzione di 'systeminfo' per risorse di sistema...")
    subprocess.run("systeminfo", shell=True)

def run_manage_services():
    print(Fore.GREEN + "Gestisci i servizi di Windows.")
    subprocess.run("services.msc", shell=True)

def run_firewall_status():
    print(Fore.YELLOW + "Controllo dello stato del firewall di Windows...")
    subprocess.run("netsh advfirewall show allprofiles state", shell=True)

def run_configure_ip():
    print(Fore.CYAN + "Configura le impostazioni IP...")
    subprocess.run("ncpa.cpl", shell=True)

def run_windows_updates():
    print(Fore.GREEN + "Ricerca di aggiornamenti di Windows...")
    subprocess.run("ms-settings:windowsupdate", shell=True)

def run_cpu_temperature():
    print(Fore.RED + "Visualizzazione della temperatura della CPU non supportata direttamente...")
    subprocess.run("wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature", shell=True)

def run_backup_files():
    print(Fore.CYAN + "Eseguo il backup dei file... (implementazione base)")
    subprocess.run("xcopy /s /e C:\\Users\\*\\Documents D:\\Backup", shell=True)

def run_disk_space():
    print(Fore.YELLOW + "Mostra lo spazio su disco disponibile...")
    subprocess.run("wmic logicaldisk get size,freespace,caption", shell=True)

def run_windows_version():
    print(Fore.GREEN + "Visualizzazione della versione di Windows...")
    subprocess.run("ver", shell=True)

def run_manage_users():
    print(Fore.CYAN + "Gestione degli utenti di Windows...")
    subprocess.run("lusrmgr.msc", shell=True)

def main():
    check_admin_privileges()

    page = 1
    options_per_page = 10

    while True:
        clear_screen()
        color_gradient()
        print_ascii_title()

        start_index = (page - 1) * options_per_page
        end_index = start_index + options_per_page

        options = [
            "1. Analizza e ripara file di sistema (sfc /scannow)",
            "2. Analizza e ripara il disco (chkdsk /f)",
            "3. Visualizza configurazione IP (ipconfig)",
            "4. Visualizza processi in esecuzione (tasklist)",
            "5. Termina un processo (taskkill)",
            "6. Testa la connessione di rete (ping)",
            "7. Deframmenta il disco (defrag)",
            "8. Monitora connessioni di rete (netstat)",
            "9. Visualizza informazioni sul sistema (systeminfo)",
            "10. Visualizza informazioni sulla CPU (wmic)",
            "11. Visualizza la ProductKey di Windows",
            "12. Visualizza risorse di sistema",
            "13. Gestisci i servizi di Windows",
            "14. Visualizza stato del firewall",
            "15. Configura le impostazioni IP",
            "16. Esegui aggiornamenti di Windows",
            "17. Visualizza temperatura CPU",
            "18. Esegui backup di file",
            "19. Visualizza spazio su disco",
            "20. Visualizza versione di Windows",
            "21. Gestisci gli utenti di Windows"
        ]

        print(Fore.CYAN + "Seleziona un'operazione da eseguire:")
        for i in range(start_index, min(end_index, len(options))):
            print(Fore.MAGENTA + options[i])

        if len(options) > end_index:
            print(Fore.YELLOW + ">> Pagine successive")
        
        choice = input(Fore.YELLOW + "Inserisci il numero dell'opzione scelta (o '>' per avanti, '<' per indietro, 'exit' per uscire): ")

        if choice.lower() == 'exit':
            print(Fore.RED + "Uscita dal programma...")
            break
        elif choice == '>':
            if (page * options_per_page) < len(options):
                page += 1
            else:
                print(Fore.RED + "Sei già nell'ultima pagina.")
                continue
        elif choice == '<':
            if page > 1:
                page -= 1
            else:
                print(Fore.RED + "Sei già nella prima pagina.")
                continue
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            clear_screen()
            if choice == "1":
                run_sfc()
            elif choice == "2":
                run_chkdsk()
            elif choice == "3":
                run_ipconfig()
            elif choice == "4":
                run_tasklist()
            elif choice == "5":
                run_taskkill()
            elif choice == "6":
                run_ping()
            elif choice == "7":
                run_defrag()
            elif choice == "8":
                run_netstat()
            elif choice == "9":
                run_systeminfo()
            elif choice == "10":
                run_wmic()
            elif choice == "11":
                run_license_info()
            elif choice == "12":
                run_system_resources()
            elif choice == "13":
                run_manage_services()
            elif choice == "14":
                run_firewall_status()
            elif choice == "15":
                run_configure_ip()
            elif choice == "16":
                run_windows_updates()
            elif choice == "17":
                run_cpu_temperature()
            elif choice == "18":
                run_backup_files()
            elif choice == "19":
                run_disk_space()
            elif choice == "20":
                run_windows_version()
            elif choice == "21":
                run_manage_users()

            input(Fore.YELLOW + "Premi Enter per tornare alla home...")

if __name__ == "__main__":
    main()
