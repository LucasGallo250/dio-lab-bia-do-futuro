# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve no FinData |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e entender dúvidas recorrentes |
| `perfil_investidor.json` | JSON | Personalizar recomendações com base no perfil (conservador, moderado, arrojado) |
| `produtos_financeiros.json` | JSON | Sugerir produtos compatíveis com o perfil do usuário |
| `transacoes.csv` | CSV | Analisar padrões de gastos, detectar excessos e gerar insights financeiros |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram utilizados como base, com foco em simular um cenário real de análise financeira.

Foram consideradas possíveis melhorias, como:

- Padronização de categorias de gastos (ex: alimentação, transporte, lazer)
- Organização temporal das transações para análise mensal
- Estruturação dos dados para facilitar geração de insights
- Preparação dos dados para análises futuras (ex: detecção de anomalias)

O objetivo foi deixar os dados mais próximos de um cenário utilizado em projetos de **Análise de Dados e Business Intelligence (BI)**.

---

## Estratégia de Integração

### Como os dados são carregados?
Os dados são carregados no início da aplicação utilizando Python, com apoio da biblioteca pandas para arquivos CSV e o módulo json para arquivos JSON.

``` Python
import pandas as pd
import json

# Carregar transações
df_transacoes = pd.read_csv("data/transacoes.csv")

# Carregar histórico de atendimento
df_atendimento = pd.read_csv("data/historico_atendimento.csv")

# Carregar perfil do investidor
with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
    perfil_investidor = json.load(f)

# Carregar produtos financeiros
with open("data/produtos_financeiros.json", "r", encoding="utf-8") as f:
    produtos_financeiros = json.load(f)

# Pré-processamento básico dos dados

# Converter datas
df_transacoes["data"] = pd.to_datetime(df_transacoes["data"])

# Criar coluna de mês/ano (útil para análises)
df_transacoes["mes_ano"] = df_transacoes["data"].dt.to_period("M")

# Agrupar gastos por categoria
gastos_categoria = df_transacoes.groupby("categoria")["valor"].sum()

```
Esses dados são mantidos em memória durante a execução da aplicação.


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são organizados e estruturados antes de serem enviados ao modelo, garantindo que o agente tenha contexto suficiente para gerar respostas precisas e personalizadas.

A construção do prompt segue uma estrutura padronizada, separando as informações por tipo:

---

📦 Estrutura do Contexto Enviado ao Modelo

```text
DADOS DO CLIENTE E PERFIL (JSON):
{
  "nome": "João Silva",
  "perfil": "Moderado",
  "saldo_disponivel": 5000,
  "objetivos": ["economizar", "investir"]
}

TRANSAÇÕES DO CLIENTE (RESUMO):
[
  {"data": "2025-11-01", "categoria": "Alimentação", "valor": 450},
  {"data": "2025-11-03", "categoria": "Streaming", "valor": 55},
  {"data": "2025-11-05", "categoria": "Restaurante", "valor": 120}
]

ANÁLISE DE GASTOS (AGREGADA):
| Categoria     | Total (R$) |
|---------------|-----------|
| Alimentação   | 1200      |
| Transporte    | 400       |
| Lazer         | 650       |

HISTÓRICO DE ATENDIMENTO:
- Cliente já demonstrou interesse em investimentos conservadores
- Dúvidas anteriores sobre controle de gastos

PRODUTOS FINANCEIROS DISPONÍVEIS:
- CDB (baixo risco)
- Tesouro Direto
- Fundos de investimento moderados
```
---

## Exemplo de Contexto Montado

```
Dados do Cliente:
- Nome: Lucas Fernandes
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Resumo de Gastos (últimos 30 dias):
- Alimentação: R$ 1.200
- Transporte: R$ 400
- Lazer: R$ 650

Insights identificados:
- Gastos com lazer aumentaram 30% em relação ao mês anterior
- Alimentação representa a maior categoria de despesa

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Restaurante - R$ 120

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
