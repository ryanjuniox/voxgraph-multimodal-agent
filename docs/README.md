# VoxGraph - Multimodal Agent

Agente multimodal que aceita entrada de texto ou áudio e responde perguntas em português brasileiro.

## Como funciona

O projeto usa um grafo (LangGraph) com fluxo sequencial:

1. **Message Refiner** — recebe a entrada do usuário. Se for áudio, transcreve para texto. Em seguida, refina a mensagem (corrige erros ortográficos/fonéticos) usando um agente LLM.
2. **Answer Generator** — recebe a mensagem refinada e gera a resposta final.

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
│   └── message_refiner/        # Agente que transcreve áudio e refina mensagens
├── services/                   # Serviços (Whisper local)
└── utils/                      # Constantes, logger, utilitários
```

## Como rodar

```bash
uv sync
streamlit run main.py
```

> Requer Ollama rodando localmente com o modelo `gemma4:e2b`.
