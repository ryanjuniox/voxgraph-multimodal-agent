# VoxGraph - Multimodal Agent

Agente multimodal que aceita entrada de texto ou áudio e responde perguntas em português brasileiro.

## Como funciona

O projeto usa um grafo (LangGraph) com roteamento condicional:

- **Texto** → vai direto para o agente de respostas.
- **Áudio** → passa pelo agente transcritor (que converte áudio em texto e corrige erros fonéticos) e depois segue para o agente de respostas.

## Tecnologias

- **Streamlit** — interface do usuário
- **LangGraph** — orquestração do fluxo de agentes
- **pydantic_ai** — definição dos agentes e tools
- **Ollama** — execução local de modelos LLM (gemma4:e2b)
- **Whisper** — transcrição de áudio (speech-to-text), executado localmente

## Estrutura

```
src/
├── agent/
│   ├── graph.py                # Definição do grafo
│   ├── state.py                # Estado compartilhado (RequestState)
│   ├── answer_generator/       # Agente que gera respostas
│   └── transcriber/            # Agente que transcreve e corrige áudio
├── tools/                      # Tools usadas pelos agentes
├── services/                   # Serviços (Whisper local)
├── routers/                    # Router condicional (audio/text)
└── utils/                      # Constantes, logger, utilitários
```

## Como rodar

```bash
uv sync
streamlit run main.py
```

> Requer Ollama rodando localmente com o modelo `gemma4:e2b`.
