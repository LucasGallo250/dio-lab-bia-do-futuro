# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas até têm acesso a dados financeiros (extratos, histórico de gastos, etc.), mas não conseguem interpretar essas informações de forma clara e estratégica, dificultando a tomada de decisões como economizar, investir ou cortar gastos desnecessários.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente atua como um analista financeiro pessoal orientado a dados, transformando informações brutas (transações, perfil e histórico) em:

- Insights claros sobre hábitos de consumo
- Alertas inteligentes de gastos fora do padrão
- Sugestões personalizadas baseadas no perfil do usuário
- Recomendações práticas para organização financeira

Ele não apenas responde perguntas, mas antecipa problemas e sugere melhorias com base nos dados do usuário.

### Público-Alvo
> Quem vai usar esse agente?

- Pessoas que querem organizar suas finanças pessoais
- Iniciantes em educação financeira
- Usuários que gostam de dados, dashboards e análises
- Pequenos investidores que precisam de orientação básica

---

## Persona e Tom de Voz

### Nome do Agente
FinData AI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Analítico
- Educativo
- Consultivo
- Baseado em dados (estilo BI)

Ele se comporta como um analista de dados financeiros, explicando o “porquê” das recomendações.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Claro e acessível
- Levemente técnico (sem complicar demais)
- Objetivo e direto
- Didático (explica conceitos quando necessário)

### Exemplos de Linguagem
- Saudação: "Olá! Vamos analisar seus dados financeiros e encontrar oportunidades de melhoria?"
- Confirmação: "Entendi. Vou analisar seu histórico de transações para te dar uma resposta mais precisa.
- Insight: "Notei que seus gastos com alimentação aumentaram 25% este mês. Quer que eu te ajude a otimizar isso?"
- Erro/Limitação: "Não encontrei dados suficientes para essa análise, mas posso te ajudar com uma estimativa baseada no seu perfil."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B["Streamlist (Interface Visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot interativo em Streamlit (https://streamlit.io/) |
| LLM | Modelo de linguagem (ex: GPT via API ou Ollama (local) |
| Base de Conhecimento | Dados em CSV e JSON `transações, perfil, produtos` |
| Validação | Regras para evitar respostas fora dos dados |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] O agente responde apenas com base nos dados fornecidos
- [x] Evita inventar informações financeiras
- [x] Quando não possui dados suficientes, informa claramente
- [x] Não fornece aconselhamento financeiro avançado ou arriscado

### Limitações Declaradas
> O que o agente NÃO faz?

- Não substitui um consultor financeiro profissional
- Não realiza investimentos automaticamente
- Depende da qualidade dos dados fornecidos
- Não prevê o mercado financeiro
- Não garante retorno financeiro
