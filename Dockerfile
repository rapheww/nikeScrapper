# Utilise l'image officielle Playwright qui correspond EXACTEMENT à ta version 1.60.0
FROM mcr.microsoft.com/playwright/python:v1.60.0-jammy

# Définit le dossier de travail dans le conteneur
WORKDIR /app

# Variable d'environnement pour forcer Python à afficher les logs en temps réel
ENV PYTHONUNBUFFERED=1

# Copie le fichier des dépendances
COPY requirements.txt .

# Installe toutes tes dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le reste de ton code (bot.py, nike.py, etc.) dans le conteneur
COPY . .

# Lance ton bot Discord
CMD ["python3", "bot.py"]