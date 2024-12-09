## PDF para JSONL para Fine-tuning de Modelos Gemini

Este repositório contém um script Python para extrair texto de livros em PDF e convertê-los em arquivos JSONL formatados para o fine-tuning de modelos Gemini do Google.

**Objetivo:**

O objetivo deste projeto é facilitar a preparação de dados para o fine-tuning de modelos Gemini. O script automatiza o processo de extração de texto de PDFs e formatação em JSONL, um formato adequado para o treinamento desses modelos.

**Funcionalidades:**

* Extrai texto de arquivos PDF.
* Segmenta o texto em chunks menores.
* Formata o texto em JSONL, com cada linha contendo um chunk de texto.
* Devolve um arquivo .jsonl no formato adequando para o fine-tuning do Gemini pela Google Cloud

**Como usar:**

1. **Instale as dependências:**

```bash
pip install -r PyPDF2 json
```

2. **Execute o script:**

```bash
python datasetMaker.py
```

<!-- **Exemplo de uso:**

```bash
python pdf_to_jsonl.py --input_dir ./pdfs --output_dir ./jsonl --chunk_size 500
```

**Parâmetros:**

* `--input_dir`: Caminho para o diretório contendo os arquivos PDF.
* `--output_dir`: Caminho para o diretório onde os arquivos JSONL serão salvos.
* `--chunk_size`: Tamanho dos chunks de texto (em número de palavras). -->

**Formato do arquivo JSONL:**

Cada linha do arquivo JSONL conterá um objeto JSON com a seguinte estrutura:

```json
{"text": "Este é um exemplo de chunk de texto."}
```

**Observações:**

* O script utiliza a biblioteca PyPDF2 para extrair texto de PDFs e json para criar o arquivo .jsonl
<!-- * O tamanho dos chunks de texto pode ser ajustado de acordo com a necessidade. -->
* Certifique-se de que os arquivos PDF estejam em um formato legível pela biblioteca PyPDF2.

**Contribuições:**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

**Licença:**

Este projeto está licenciado sob a licença GPL.
