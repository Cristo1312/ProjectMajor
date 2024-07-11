# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro nell'immagine Docker
WORKDIR /app

# Copia il file di requirements nella directory di lavoro
COPY requirements.txt ./

# Installa le dipendenze Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia il file dell'applicazione nella directory di lavoro
COPY app.py ./

# Copia la cartella dei template nella directory di lavoro
COPY templates/ templates/

# Espone la porta 5006 per Flask
EXPOSE 5006

# Comando per eseguire l'applicazione Flask
CMD ["python", "app.py"]
