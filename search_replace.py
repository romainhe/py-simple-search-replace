import argparse
import os

def replace_value_in_file(file_path, search_value=None, replace_value=None, require_confirmation=False):
    # Vérifie si le fichier existe
    if not os.path.isfile(file_path):
        print(f"Le fichier {file_path} n'existe pas.")
        return

    # Lis le contenu du fichier avec encodage UTF-8
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Erreur de décodage lors de la lecture du fichier {file_path}.")
        return

    # Demande la valeur à rechercher si non fournie
    if search_value is None:
        search_value = input("Veuillez entrer la valeur à rechercher : ")

    # Compte les occurrences de la valeur recherchée
    occurrences = content.count(search_value)
    print(f"La valeur '{search_value}' apparaît {occurrences} fois dans le fichier.")

    # Demande la valeur de remplacement si non fournie
    if replace_value is None:
        replace_value = input("Veuillez entrer la valeur de remplacement : ")

    if occurrences > 0:

        # Si les valeurs de recherche et de remplacement sont fournies, demander une confirmation
        if require_confirmation:
            confirmation = input(f"Confirmez-vous le remplacement de {occurrences} occurrences de '{search_value}' par '{replace_value}' (y/n) ? ")
            if confirmation.lower() != 'y':
                print("Remplacement annulé.")
                return

        # Remplace la valeur recherchée par la valeur de remplacement
        content = content.replace(search_value, replace_value)

        # Écris le contenu modifié dans le fichier avec encodage UTF-8
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except UnicodeEncodeError:
            print(f"Erreur d'encodage lors de l'écriture du fichier {file_path}.")
            return

        print(f"Les occurrences de '{search_value}' ont été remplacées par '{replace_value}' dans le fichier {file_path}.")

    else:
        print(f"Aucune occurrence de '{search_value}' n'a été trouvée dans le fichier {file_path}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remplacer une valeur par une autre dans un fichier.')
    parser.add_argument('file', help='Le chemin du fichier à modifier')
    parser.add_argument('-s', '--search', help='La valeur à rechercher')
    parser.add_argument('-r', '--replace', help='La valeur de remplacement')

    args = parser.parse_args()

    require_confirmation = args.search is not None and args.replace is not None
    replace_value_in_file(args.file, args.search, args.replace, require_confirmation)
