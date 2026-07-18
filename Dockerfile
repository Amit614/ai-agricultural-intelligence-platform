FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python","-m","agri_platform.api.main"]
