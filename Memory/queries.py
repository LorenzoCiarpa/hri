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

def checkLevelQuery(username):

    # Eseguire una query
    query = '''
    SELECT 
        SUM(CASE WHEN winner = 'AI' THEN 1 ELSE 0 END) AS AI_wins,
        SUM(CASE WHEN winner = 'HUMAN' THEN 1 ELSE 0 END) AS human_wins,
        SUM(CASE WHEN winner = 'DRAW' THEN 1 ELSE 0 END) AS draw
    FROM 
        tris_match
    WHERE 
        idUser = (SELECT idUser from user where username = %s);
    '''
    parametri = (username,)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)
    # Ottenere i risultati
    result = cursor.fetchall()

    return result

def getLevel(username):

    # Eseguire una query
    query = '''
    SELECT 
        level 
    FROM 
        tris_instance 
    WHERE 
        idUser = (SELECT idUser from user where username = %s)
    '''
    parametri = (username,)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)

    # Ottenere i risultati
    result = cursor.fetchall()

    return result

def setLevel(username, level):

    
    query = '''
    INSERT INTO tris_instance
        (idUser, level) 
    values 
        ((SELECT idUser FROM user WHERE username = %s), %s)
    ON DUPLICATE KEY
    UPDATE
        level = %s
    '''
    # Eseguire una query
    
    parametri = (username, level, level,)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)
    # Ottenere i risultati
    dbConnection.commit()


    return True
    

if __name__ == "__main__":
    # user = getUser("buitr")
    # print(f"user: {user}")

    # createUser("buitr")
    # res = checkLevel('b')
    res = setLevel('b', 'PRO')
    # res = getLevel('b')
    print(res)