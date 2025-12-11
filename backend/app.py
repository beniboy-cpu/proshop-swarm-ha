import os
import time
import psycopg2
from psycopg2 import OperationalError
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    max_retries = 15
    retry_delay = 3  # secondes

    for attempt in range(1, max_retries + 1):
        try:
            conn = psycopg2.connect(
                host=os.environ['DB_HOST'],
                database=os.environ['DB_NAME'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD'],
                connect_timeout=5
            )
            print(f"Connexion à la base de données réussie ! (après {attempt} tentative(s))")
            return conn
        except OperationalError as e:
            print(f"DB pas encore prête... tentative {attempt}/{max_retries} - ({e})")
            if attempt == max_retries:
                raise
            time.sleep(retry_delay)
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            raise

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Création table + données de démo
        cur.execute('CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(100), price integer);')
        cur.execute('SELECT count(*) FROM products;')
        if cur.fetchone()[0] == 0:
            products_data = [
                ('Super Laptop Gamer', 1200),
                ('Souris RGB Pro', 80),
                ('Écran 4K Ultra', 450)
            ]
            cur.executemany('INSERT INTO products (name, price) VALUES (%s, %s)', products_data)
            conn.commit()
            print("Données de démonstration insérées.")

        cur.execute('SELECT name, price FROM products ORDER BY id;')
        products = cur.fetchall()
        cur.close()
        conn.close()

        return render_template('index.html', products=products)

    except Exception as e:
        return f"Erreur de connexion à la base de données ou de l'application: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)