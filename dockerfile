# Python 3.12 resmi imajını kullan
FROM python:3.12-slim

# Çalışma dizini oluştur
WORKDIR /app

# Gerekli dosyaları kopyala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı kopyala
COPY app.py .

# Flask 5000 portunu kullanıyor
EXPOSE 5003

# Container başladığında çalışacak komut
CMD ["python", "app.py"]
