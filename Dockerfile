# Utilise une image Python officielle comme image de base
FROM python:3.11-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requirements.txt pour installer les dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste des fichiers de l'application
COPY . .

# Définit la variable d'environnement pour la production
ENV PYTHONUNBUFFERED=1

# Expose le port utilisé par l'application (si nécessaire)
EXPOSE 3000

# Commande pour démarrer le bot
CMD ["python", "main.py"]