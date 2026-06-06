# Agent Graph

## Descrição do fluxo

O grafo utiliza um router condicional no início que verifica o `request_type`:

- **`request_type == "audio"`** → direciona para o `transcriber`, que transcreve o áudio e corrige erros ortográficos fonéticos, depois encaminha o resultado para o `answer_generator`.
- **`request_type == "text"`** → direciona diretamente para o `answer_generator`.

```mermaid
graph TD;
	__start__([<p>__start__</p>]):::first
	answer_generator(answer_generator)
	transcriber(transcriber)
	__end__([<p>__end__</p>]):::last
	__start__ -. "request_type == audio" .-> transcriber;
	__start__ -. "request_type == text" .-> answer_generator;
	transcriber --> answer_generator;
	answer_generator --> __end__;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
```
