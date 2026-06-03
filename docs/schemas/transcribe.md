# Transcribe API — Response Schema

## Response

```json
{
  "text": "string",
  "segments": [
    {
      "id": "integer",
      "seek": "integer",
      "start": "float",
      "end": "float",
      "text": "string",
      "tokens": ["integer"],
      "temperature": "float",
      "avg_logprob": "float",
      "compression_ratio": "float",
      "no_speech_prob": "float"
    }
  ],
  "language": "string (ISO 639-1)"
}
