# API de Processamento de Entregas

Este projeto é uma API FastAPI para processar entregas e calcular o melhor lucro.

## Requisitos

- Python 3.8+
- pip

## Instalação

1. Clone o repositório:

   ```
   git clone https://github.com/arthurvieira2003/copiloto-entregas
   cd copiloto-entregas
   ```

2. Crie um ambiente virtual:

   ```
   python -m venv novo_ambiente
   ```

3. Ative o ambiente virtual:

   - No Windows:
     ```
     novo_ambiente\Scripts\activate
     ```
   - No macOS e Linux:
     ```
     source novo_ambiente/bin/activate
     ```

4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Executando a API

Para iniciar o servidor da API, execute:

```
python main.py
```

A API estará disponível em `http://localhost:8000`.

## Documentação da API (Swagger)

Após iniciar o servidor, você pode acessar a documentação interativa da API (Swagger) em:

    http://localhost:8000/docs

Esta interface permite explorar e testar todos os endpoints da API.

## Uso da API

A API possui um endpoint principal:

### POST /processar_entregas

Processa as entregas e calcula o melhor lucro.

Exemplo de requisição:

```
{
  "conexoes": [
    ["A", "B", 5],
    ["B", "C", 3],
    ["A", "D", 2],
    ["C", "D", 8]
  ],
  "entregas": [
    [0, "B", 1],
    [5, "C", 10],
    [10, "D", 8]
  ]
}
```

Exemplo de resposta:

```
{
  "entregas_realizadas": [
    [
      5,
      "C",
      10
    ]
  ],
  "lucro_total": 10
}
```

## Desenvolvimento

O código principal da API está localizado em `main.py`. A lógica de processamento de entregas está em `services/entrega_service.py`.
