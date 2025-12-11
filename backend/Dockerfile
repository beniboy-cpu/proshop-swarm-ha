# 1. On part d'une image Python légère et stable
FROM python:3.9-slim

# 2. On installe les dépendances système nécessaires pour se connecter à PostgreSQL (libpq-dev)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. On définit le répertoire de travail dans le conteneur
WORKDIR /app

# 4. On copie les requirements et on installe les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie tout le code de l'application (app.py, templates/, etc.)
COPY . .

# 6. La commande qui lance l'application au démarrage du conteneur
CMD ["python", "app.py"]