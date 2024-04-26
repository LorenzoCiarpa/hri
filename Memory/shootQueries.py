import os
import sys

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_folder)

from Memory.dbConnection import cursor, dbConnection

def setWinnerShoot(username, winner):

    # Eseguire una query
    query = '''
    INSERT ignore INTO shoot_match 
        (idUser, winner) 
    values 
        ((SELECT idUser FROM user WHERE username = %s), %s)'''
    parametri = (username, winner)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)
    dbConnection.commit()
    
    return {
            'success': True
        }