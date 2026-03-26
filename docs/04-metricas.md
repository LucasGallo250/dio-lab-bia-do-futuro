# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Cenários definidos para validar comportamento, precisão e segurança;
2. **Simulação de uso real:** 2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente responde corretamente com base nos dados | Perguntar total de gastos e receber valor correto |
| **Segurança (Anti-alucinação)** | O agente evita inventar informações | Perguntar algo fora do contexto e ele admitir limitação |
| **Coerência** | A resposta está alinhada ao perfil do cliente | Sugerir investimentos compatíveis com perfil |
| **Clareza** | A resposta é fácil de entender | Resposta organizada com resumo, insight e sugestão |
| **Capacidade Analítica** | O agente gera insights úteis a partir dos dados | Identificar padrões de consumo e sugerir melhorias |

> [!TIP]
> Testes com usuários reais aumentam muito a qualidade da avaliação. Sempre que possível, peça para outras pessoas interagirem com o agente e avaliarem a experiência.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Análise de comportamento
- **Pergunta:** "Estou gastando muito?"
- **Resposta esperada:** Identificação de padrões e possível aumento de gastos
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda?"
- **Resposta esperada:** Sugestão alinhada ao perfil do investidor
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Pergunta fora do escopo
- **Pergunta:** "Qual o rendimento exato desse investimento?"
- **Resposta esperada:** Agente informa que não possui essa informação
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente conseguiu responder com base nos dados disponíveis
- As respostas seguiram uma estrutura clara (Resumo + Insight + Sugestão)
- Boa capacidade de identificar padrões de gastos
- Evitou alucinações na maioria dos testes

**O que pode melhorar:**
- Melhorar a profundidade das recomendações financeiras
- Refinar a personalização com mais dados do usuário
- Aumentar a precisão em perguntas mais específicas
- Evoluir para análises mais avançadas (ex: previsão de gastos futuros)

---

## Métricas Avançadas (Opcional)

Além das métricas funcionais, também foram considerados aspectos técnicos:

- Tempo de resposta: rapidez na geração das respostas
- Consumo de tokens: eficiência no uso do modelo
- Consistência: estabilidade das respostas em perguntas similares
Essas métricas são importantes para avaliar a escalabilidade e eficiência do agente.

---

## Diferencial do Projeto

A avaliação do agente não se limita apenas a respostas corretas, mas também considera:

- Capacidade de análise de dados
- Geração de insights relevantes
- Segurança contra alucinações

Isso aproxima o projeto de um cenário real de uso em sistemas financeiros baseados em IA.

---

## Resultado final

Com isso aqui você mostra:

- Pensamento analítico
- Preocupação com qualidade
-  Noção de avaliação de IA
-  Mentalidade de produto (não só código)

---

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
