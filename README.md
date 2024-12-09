## PDF to JSONL for Gemini Model Fine-tuning

This repository contains a Python script to extract text from PDF books and convert it into JSONL files formatted for fine-tuning Google’s Gemini models.

**Purpose:**

The goal of this project is to simplify the data preparation process for fine-tuning Gemini models. The script automates the extraction of text from PDFs and its formatting into JSONL, a format suitable for training these models.

**Features:**

* Extracts text from PDF files.
* Segments the text into smaller chunks.
* Formats the text into JSONL, with each line containing a text chunk.
* Outputs a .jsonl file in the format suitable for fine-tuning Gemini via Google Cloud.

**How to use:**

1. **Install dependencies:**

```bash
pip install -r PyPDF2 json
```

2. **Run the script:**

```bash
python datasetMaker.py
```

<!-- **Example usage:**

```bash
python pdf_to_jsonl.py --input_dir ./pdfs --output_dir ./jsonl --chunk_size 500
```

**Parameters:**

* `--input_dir`: Path to the directory containing the PDF files.
* `--output_dir`: Path to the directory where the JSONL files will be saved.
* `--chunk_size`: Size of the text chunks (in number of words). -->

**JSONL File Format:**

Each line in the JSONL file will contain a JSON object with the following structure:

```json
{"text": "This is an example of a text chunk."}
```

**Notes:**

* The script uses the PyPDF2 library to extract text from PDFs and json to create the .jsonl file.
<!-- * The chunk size can be adjusted according to need. -->
* Ensure that the PDF files are in a format that can be read by the PyPDF2 library.

**Contributions:**

Contributions are welcome! Feel free to open issues or pull requests.

**License:**

This project is licensed under the GPL license.
