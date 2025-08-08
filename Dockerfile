# Étape 1 : build frontend
FROM node:18 AS build_frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build && ls -la /app/frontend

# Étape 2 : backend Flask
FROM python:3.11-slim
WORKDIR /app

# Installer dépendances backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier backend
COPY backend/ .

# Copier build frontend dans dossier static
COPY --from=build_frontend /app/frontend/dist ./static

EXPOSE 5200
CMD ["python", "app.py"]
