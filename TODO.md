# TODO — VoxGraph Multimodal Agent

Roadmap de evolução do projeto, organizado por prioridade.

---

## Fase 1: Resiliência e Robustez do Grafo

- [ ] Nó de validação pós-transcrição (verificar se o texto faz sentido antes de seguir)
- [ ] Retry com fallback nos agentes (se LLM falha, tentar novamente ou usar resposta padrão)
- [ ] Memória conversacional com LangGraph checkpointer (manter contexto entre turnos)
- [ ] Feedback loop — se a resposta não faz sentido, re-processar
- [ ] Tratamento de timeout nas chamadas ao Ollama
- [ ] Graceful degradation — se o Whisper falhar, informar o usuário em vez de crashar

---

## Fase 2: Qualidade de Engenharia

- [ ] Testes unitários para utils (`bytes_to_numpy`, `router`)
- [ ] Testes unitários para tools (mock do Whisper)
- [ ] Testes de integração do grafo (fluxo completo com mocks)
- [ ] Tipagem correta nos nós — usar `RequestState` em vez de `dict`
- [ ] Error handling adequado — usar `raise ... from e` para preservar traceback
- [ ] Adicionar type hints em todas as funções
- [ ] Lint/format com ruff (já configurado, garantir CI)
- [ ] Structured logging (JSON) em vez de formato texto simples

---

## Fase 3: Novas Modalidades

- [ ] Suporte a imagem — descrição e visual QA (LLaVA via Ollama)
- [ ] Novo nó `image_analyzer` no grafo
- [ ] Router inteligente para detectar tipo de input (texto/áudio/imagem)
- [ ] TTS na resposta — devolver áudio (fechar loop voz → voz)
- [ ] Suporte a vídeo — extrair frames + áudio e processar ambos
- [ ] Multimodal combinado — aceitar áudio + imagem na mesma request

---

## Ideias Futuras (backlog)

- [ ] Streaming — respostas em tempo real no Streamlit
- [ ] Avaliação — medir WER da transcrição e qualidade das respostas (LLM-as-judge)
- [ ] Deploy com Docker (Ollama + app)
