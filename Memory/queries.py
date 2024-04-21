import os
import sys

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Memory.dbConnection import cursor, dbConnection

def getUser(username):

    # Eseguire una query
    query = "SELECT * FROM user WHERE username = %s"
    parametri = (username,)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)

    # Ottenere i risultati
    result = cursor.fetchall()

    return result

def createUser(username):

    # Eseguire una query
    query = "INSERT ignore INTO user (username) values (%s)"
    parametri = (username,)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)
    dbConnection.commit()

    new_account = True
    if cursor.lastrowid == 0:
        new_account = False
    
    return {
            'success': True,
            'new_account': new_account
        }

def setWinner(username, winner):

    # Eseguire una query
    query = '''
    INSERT ignore INTO tris_match 
        (idUser, winner) 
    values 
        ((SELECT idUser FROM user WHERE username = %s), %s)'''
    parametri = (username, winner)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)
    dbConnection.commit()
    
    return {
            'success': True
        }

if __name__ == "__main__":
    # user = getUser("buitr")
    # print(f"user: {user}")

    createUser("buitr")