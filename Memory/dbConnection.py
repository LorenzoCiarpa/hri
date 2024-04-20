import mysql.connector
from config import dbConfig

# Stabilire la connessione
conn = mysql.connector.connect(**dbConfig)

# Creare un cursore
cursor = conn.cursor(dictionary=True)



