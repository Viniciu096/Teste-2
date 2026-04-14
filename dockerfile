# Imagem base com Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências
RUN pip install --no-cache-dir --upgrade pip

# Comando para rodar o programa
CMD ["python", "Tete.py"]