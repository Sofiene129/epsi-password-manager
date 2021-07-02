import sqlite3
import sqlite3

Mdp_Maitre = "Epsi123!"

password = input("Entrez votre mot de passe principal: ")
while password != Mdp_Maitre:
    print("Votre mot de passe est incorrecte merci de le resaisir ")
    password = input("Merci de saisir le bon mot de passe : ")

ConnectDB = sqlite3.connect("passwords.db")

cursor = ConnectDB.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    Outils TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")


def menu():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("#        E : Entrez un nouveau mot de passe        #")
    print("#      L : Listes de services enregistrées#")
    print("#       R : Récupérer un mot de passe#")
    print("#              s : Sortir#")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def Obtenir_mdp(Outils):
    cursor.execute(f"""
        SELECT username, password FROM users
        WHERE Outils = '{Outils}';
    """)
    if cursor.rowcount == 0:
        print("Outils non enregistré (utiliser' pour vérifier les services.)")
    else:
        for user in cursor.fetchall():
            print(user)


def ajout_mdp(Outils, username, password):
    cursor.execute(f"""
        INSERT INTO users (Outils, username, password)
        VALUES ('{Outils}', '{username}', '{password}');
    """)
    ConnectDB.commit()


def Voir_mdp():
    cursor.execute("""
        SELECT * FROM users;
    """)
    for Outils in cursor.fetchall():
        print(Outils)


while True:
    menu()
    op = input("Choisis une option: ")
    if op not in ["E", "L", "R", "s"]:
        print("Option invalide.")
        continue

    if op == "s":
        break

    if op == "E":
        Outils = input("quel est le nom du Outils? ")
        username = input("Quel est le nom d'utilisateur ? ")
        password = input("Quel est le mot de passe? ")
        ajout_mdp(Outils, username, password)

    if op == "L":
        Voir_mdp()

    if op == "R":
        Outils = input("Pour quel Outils voulez-vous le mot de passe ? ")
        Obtenir_mdp(Outils)


ConnectDB.close()