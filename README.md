# WiFi Brute Force Attack Script

This script allows you to scan available WiFi networks and perform a brute force attack to crack the passwords using a provided wordlist.

## Features

- **WiFi Network Scan**: Scans available WiFi networks and displays their information (SSID, signal strength, BSSID, security type).
- **Brute Force Attack**: Performs a brute force attack on a specified WiFi network using a wordlist.
- **Network Information Display**: Displays detailed information about a specific WiFi network.
- **Language Switch**: Allows changing the interface language between English, French, and German.

## Prerequisites

Before you begin, make sure the following libraries are installed:

```bash
pip install pywifi
```

## Available Commands

- `scan`: Scans available WiFi networks.
- `attack [number]`: Initiates a brute force attack on the specified WiFi network.
- `info [number]`: Displays detailed information about the specified WiFi network.
- `list`: Lists all detected WiFi networks with additional details.
- `clear`: Clears the console screen for better readability.
- `help`: Displays help with available commands.
- `exit`: Closes the program.
- `lang [en/fr/de]`: Changes the interface language.

## How to Use

1. **Scan WiFi Networks**:
   Use the `scan` command to detect available WiFi networks in your area.

2. **Launch an Attack**:
   Use the `attack [number]` command to attempt to crack the password of a WiFi network. The number corresponds to the index of the network detected by the `scan` command.

3. **Get Information about a Network**:
   Use the `info [number]` command to display detailed information about a specific network.

4. **Change Language**:
   Use the `lang [en/fr/de]` command to change the interface language.

## Example Usage

Here's an example of usage in the terminal:

```bash
$ python wifi_attack.py
> scan
Detected WiFi Networks:
[0] Network_1 - Signal: -50 dBm
[1] Network_2 - Signal: -70 dBm

> attack 0
Starting attack on Network_1 with 500 passwords...
Progress: 23.50%

[SUCCESS] Password found: password123
```

## Warnings

- **Ethical Use**: This script should only be used on WiFi networks for which you have explicit permission.
- **Legality**: Ensure that you comply with local laws and regulations regarding access to WiFi networks.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.


# WiFi Brute Force Attack Script

Ce script permet de scanner les réseaux WiFi disponibles et de tenter une attaque par brute force pour trouver les mots de passe en utilisant une liste de mots de passe fournie.

## Fonctionnalités

- **Scan des réseaux WiFi** : Scanne les réseaux WiFi disponibles et affiche leurs informations (SSID, signal, BSSID, type de sécurité).
- **Attaque par brute force** : Lance une attaque sur un réseau WiFi spécifié en utilisant une liste de mots de passe.
- **Affichage d'informations sur le réseau** : Affiche des informations détaillées sur un réseau WiFi spécifique.
- **Changement de langue** : Permet de changer la langue de l'interface entre anglais, français et allemand.

## Prérequis

Avant de commencer, assurez-vous que les bibliothèques suivantes sont installées :

```bash
pip install pywifi
```

## Commandes disponibles

- `scan` : Scanne les réseaux WiFi disponibles.
- `attack [numéro]` : Lance une attaque sur le réseau WiFi spécifié.
- `info [numéro]` : Affiche des informations détaillées sur le réseau WiFi spécifié.
- `list` : Liste tous les réseaux WiFi détectés avec des détails supplémentaires.
- `clear` : Efface l'écran de la console pour une meilleure lisibilité.
- `help` : Affiche l'aide avec les commandes disponibles.
- `exit` : Ferme le programme.
- `lang [en/fr/de]` : Change la langue de l'interface.

## Comment utiliser

1. **Lancer le scan des réseaux WiFi** :
   Utilisez la commande `scan` pour détecter les réseaux WiFi disponibles dans votre environnement.

2. **Lancer une attaque** :
   Utilisez la commande `attack [numéro]` pour tenter de craquer le mot de passe d'un réseau WiFi. Le numéro correspond à l'index du réseau détecté par la commande `scan`.

3. **Obtenir des informations sur un réseau** :
   Utilisez la commande `info [numéro]` pour afficher des informations détaillées sur un réseau.

4. **Changer de langue** :
   Utilisez la commande `lang [en/fr/de]` pour changer la langue de l'interface.

## Exemple d'utilisation

Voici un exemple d'utilisation dans le terminal :

```bash
$ python wifi_attack.py
> scan
Réseaux WiFi détectés :
[0] Network_1 - Signal: -50 dBm
[1] Network_2 - Signal: -70 dBm

> attack 0
Lancement de l'attaque sur Network_1 avec 500 mots de passe...
Progression : 23.50%

[SUCCESS] Mot de passe trouvé : password123
```

## Avertissements

- **Utilisation éthique** : Ce script doit être utilisé uniquement sur des réseaux WiFi pour lesquels vous avez une autorisation explicite.
- **Légalité** : Assurez-vous que vous respectez les lois locales et les règles concernant l'accès aux réseaux WiFi.

## License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.
