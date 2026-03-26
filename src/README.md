# Código da Aplicação

Esta pasta contém todo o código do agente financeiro FinData AI, responsável por processar dados do cliente, gerar insights e interagir via interface web.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit ou Gradio)
├── agente.py           # Lógica do agente e integração com LLM
├── config.py           # Configurações (ex: API keys, parâmetros de prompt)
├── utils.py            # Funções auxiliares (ex: parsing CSV/JSON, formatação de dados)
├── data_loader.py      # Carregamento e normalização da base de conhecimento
└── requirements.txt    # Dependências do projeto
```
> Dica: Separar a lógica do agente (agente.py) da aplicação web (app.py) facilita testes, manutenção e futuras integrações.

## Exemplo de requirements.txt

```
streamlit
openai
pandas
python-dotenv
```
> Incluímos pandas para manipulação de CSV/JSON e python-dotenv para carregar variáveis de ambiente de forma segura.

## Como Rodar

```bash
1. Instalar dependências
pip install -r requirements.txt

2. Configurar variáveis de ambiente
OPENAI_API_KEY="sua_chave_aqui"

3. Rodar a aplicação
streamlit run app.py
```
4. Acessar a interface
Abra o navegador no link informado pelo Streamlit (geralmente `http://localhost:8501)`.

---

## Boas Práticas
- Nunca exponha sua API key em commits públicos.
- Valide os dados antes de enviar para o agente.
- Mantenha requirements.txt atualizado.
- Teste cenários diferentes para garantir que o agente não alucine.
- Documente funções e módulos para facilitar manutenção futura.

---

## Observações
- O código está estruturado para facilitar expansão, como inclusão de novos dados ou integração com outros LLMs.
- A arquitetura separa interface, lógica do agente e carregamento de dados, seguindo boas práticas de engenharia de software.
- Este projeto é facilmente escalável para produção com pequenas adaptações (ex: dockerização ou deploy na nuvem).
