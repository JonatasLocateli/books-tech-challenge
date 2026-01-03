# Design da API

## Princípios
- RESTful
- Versionamento (`/api/v1`)
- Respostas em JSON
- Uso de HTTP status codes

## Endpoints Principais
- GET /api/v1/books
- GET /api/v1/books/{id}
- GET /api/v1/categories
- GET /api/v1/health

## Endpoints Opcionais
- Estatísticas
- Filtros avançados
- Ranking de categorias

## Segurança
- Autenticação JWT
- Proteção de rotas sensíveis

## Documentação
- Swagger integrado à aplicação
