# Pipeline de Dados

## Etapas do Pipeline

### 1. Ingestão
- Web scraping do site https://books.toscrape.com
- Extração de título, preço, rating, disponibilidade, categoria e imagem

### 2. Processamento
- Normalização de preços
- Conversão de rating textual para numérico
- Tratamento de encoding

### 3. Persistência
- Armazenamento dos dados em SQLite
- Estrutura tabular pronta para consultas analíticas

### 4. Exposição via API
- API RESTful com Flask
- Endpoints versionados (`/api/v1`)

### 5. Consumo
- Dashboards
- Pipelines de Machine Learning
- Serviços de recomendação
