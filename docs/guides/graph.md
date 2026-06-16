# Agent Graph

## Descrição do fluxo

O grafo segue um fluxo sequencial com dois nós:

1. **`message_refiner`** — se `request_type == "audio"`, transcreve o áudio para texto via Whisper. Em seguida, refina a mensagem (corrige erros ortográficos e fonéticos) usando um agente LLM. Se `request_type == "text"`, apenas refina o texto recebido.
2. **`answer_generator`** — recebe a pergunta refinada e gera a resposta final.

```mermaid
graph TD;
	__start__([<p>__start__</p>]):::first
	message_refiner(message_refiner)
	answer_generator(answer_generator)
	__end__([<p>__end__</p>]):::last
	__start__ --> message_refiner;
	message_refiner --> answer_generator;
	answer_generator --> __end__;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
```
