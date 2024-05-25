# Use a imagem oficial do Python como base
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do aplicativo para o diretório de trabalho
COPY . .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando para rodar o aplicativo Flask
CMD ["flask", "run"]
