from dbConnection import cursor

def getUser(username):

    # Eseguire una query
    query = "SELECT * FROM users WHERE username = %s"
    parametri = (username,)  # i parametri devono essere forniti in una tupla

    cursor.execute(query, parametri)

    # Ottenere i risultati
    result = cursor.fetchall()

    return result

if __name__ == "__main__":
    user = getUser("buitre")
    print(f"user: {user}")
