# Llama 3.2 Vision

## November 6, 2024

[Llama 3.2 Vision](https://ollama.com/library/llama3.2-vision) is now available to run in Ollama, in both 11B and 90B sizes.

## Get started

[Download Ollama 0.4](https://ollama.com/download), then run:

```bash
ollama run llama3.2-vision

```

To run the larger 90B model:

```bash
ollama run llama3.2-vision:90b

```

To add an image to the prompt, drag and drop it into the terminal, or add a path to the image to the prompt on Linux.

> Note: Llama 3.2 Vision 11B requires least 8GB of VRAM, and the 90B model requires at least 64 GB of VRAM.

## Examples

### Handwriting

![handwriting example](/public/blog/llama3.2-vision-handwriting.png)

### Optical Character Recognition (OCR)

![OCR example](/public/blog/llama3.2-vision-ocr.png)

### Charts & tables

![charts and tables example](/public/blog/llama3.2-vision-charts.png)

### Image Q&A

![image Q&A example](/public/blog/llama3.2-vision-imageqa.png)

## Usage

First, pull the model:

```bash
ollama pull llama3.2-vision

```

### Python Library

To use Llama 3.2 Vision with the Ollama [Python library](https://github.com/ollama/ollama-python):

```python
import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{\
        'role': 'user',\
        'content': 'What is in this image?',\
        'images': ['image.jpg']\
    }]
)

print(response)

```

### JavaScript Library

To use Llama 3.2 Vision with the Ollama [JavaScript library](https://github.com/ollama/ollama-js):

```javascript
import ollama from 'ollama'

const response = await ollama.chat({
  model: 'llama3.2-vision',
  messages: [{\
    role: 'user',\
    content: 'What is in this image?',\
    images: ['image.jpg']\
  }]
})

console.log(response)

```

### cURL

```shell
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2-vision",
  "messages": [\
    {\
      "role": "user",\
      "content": "what is in this image?",\
      "images": ["<base64-encoded image data>"]\
    }\
  ]
}'

```

[![Ollama Vision logo](/public/blog/ollama-vision.png)](https://ollama.com/download)