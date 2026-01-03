# Plano Arquitetural – Books Tech Challenge

## 1. Visão Geral do Projeto

Este projeto consiste em uma **API de consulta de livros** construída em **Flask**, com capacidade de ingestão, processamento, armazenamento, exposição via API e consumo por cientistas de dados/ML.  
O objetivo é fornecer uma arquitetura **modular e escalável**, permitindo integração futura com modelos de Machine Learning e dashboards analíticos.

### Componentes Principais:
1. **Scraping / Ingestão** – coleta de dados de livros do site `books.toscrape.com`.
2. **Processamento e Banco de Dados** – limpeza e armazenamento em SQLite (fácil substituição por DB mais robusto).
3. **API REST** – endpoints organizados em namespaces (Books, Categories, Stats, ML, Auth, Scraping).
4. **Consumo** – dashboards, scripts de ML ou outros serviços externos.

---

## 2. Diagrama do Pipeline

+----------------+ +-----------------+ +------------------+ +----------------+
| | | | | | | |
| Scraping | ----> | Processamento | ----> | Banco de Dados | ----> | API REST |
| (Ingestão) | | e Limpeza | | (SQLite/SQL) | | (Flask) |
| | | | | | | |
+----------------+ +-----------------+ +------------------+ +----------------+
|
v
+----------------+
| Consumidores / |
| Cientistas ML |
| Dashboards |
+----------------+


**Descrição:**  
1. O **scraping** coleta dados (título, preço, categoria, rating, disponibilidade).  
2. O **processamento** realiza limpeza de dados e converte valores numéricos.  
3. O **banco de dados** armazena os registros de forma estruturada.  
4. A **API REST** fornece endpoints para consulta, estatísticas, ML e scraping.  
5. Os **consumidores** podem acessar os dados via endpoints para análises, dashboards ou treinamento de modelos.

---

## 3. Arquitetura para Escalabilidade

Embora o projeto utilize SQLite e Flask localmente, a arquitetura é pensada para crescimento:

- **Banco de dados escalável**: possível migrar para PostgreSQL ou MySQL para suportar grandes volumes.  
- **Serviços desacoplados**: Scraping, API e ML podem ser transformados em microservices.  
- **Fila de processamento**: Celery + RabbitMQ/Kafka para ingestão e tarefas pesadas.  
- **Cache**: Redis ou Memcached para acelerar consultas frequentes.  
- **Autenticação e segurança**: JWT para proteger endpoints sensíveis (como scraping e ML).

---

## 4. Cenário de Uso para Cientistas de Dados / ML

Cientistas de dados podem:

1. **Consultar features prontas** para treinamento de modelos:
   - `GET /api/v1/ml/features` → retorna colunas numéricas e indicadores de disponibilidade.
2. **Obter dataset completo**:
   - `GET /api/v1/ml/training-data` → retorna todas as informações dos livros.
3. **Enviar predições**:
   - `POST /api/v1/ml/predictions` → recebe resultados de modelos ML para análises ou feedback loop.

Exemplo de fluxo ML:


API -> GET /ml/features -> Treinamento Modelo -> POST /ml/predictions -> Feedback / Estatísticas


---

## 5. Plano de Integração com Modelos de ML

O sistema está preparado para consumir e fornecer dados para Machine Learning:

**Formato de Features**:
  json
  [
    {
      "price": 12.99,
      "rating": 5,
      "available": 1
    },
    ...
  ]


Formato de Dataset Completo:

[
  {
    "id": 1,
    "title": "Clean Code",
    "price": 12.99,
    "rating": 5,
    "availability": "In stock",
    "category": "Programming",
    "image_url": "url",
    "product_url": "url"
  },
  ...
]

Envio de Predições:

[
  {
    "id": 1,
    "predicted_rating": 4.8
  },
  ...
]

Possível evolução:

Treinamento de modelos diretamente a partir da API.

Geração de dashboards analíticos com Streamlit ou Grafana.

Integração com pipelines automatizados (Airflow / Prefect).

## 6. Considerações Finais

Arquitetura modular: fácil substituição de DB, autenticação, ou framework web.

Pipeline completo: ingestão → processamento → API → consumo.

Preparada para consumo ML: endpoints de features, dataset e predições.

Segurança e métricas: JWT, logs estruturados, métricas de performance da API.

