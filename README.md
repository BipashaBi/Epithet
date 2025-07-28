# Epithet : An Offline PDF Outline Extractor

A sincere attempt by team Hack-A-Dobe to extract titles and headings from PDF files, organized in a clear outline. This solution is made to meet the Adobe Hackathon Challenge 1A requirements.

## Approach

The script works by:
1. **Parsing PDF text** using [PyMuPDF](`fitz`).
2. **Extracting all text spans** with font size, style, and position.
3. **Determining headings** by comparing font sizes:
   - Largest font → treated as the **title**
   - Other fonts larger than the body text → categorized as **H1**, **H2**, or **H3** headings.
4. Outputs a JSON file containing:
   - The document title
   - A list of headings with level and page number
---

## Models / Libraries Used

- [`PyMuPDF`](https://pypi.org/project/PyMuPDF/) (`fitz`) – for parsing and analyzing PDF text and fonts.
- `re`, `os`, `json`, `pathlib`, and `logging` – for text cleanup, file handling, and logging.

---
## Build & Run Instructions

### Directory Structure

├── EPITHET1A/
|     ├── app
│          ├── process_pdfs.py
│          ├── Dockerfile
│          ├── README.md
│          ├── sample_dataset/
│          ├── input/
│          ├── output/
|          ├── requirement.txt
│          └── schema/
│               └── output_schema.json

## Install Dependecies

Install Dependencies

Make sure you have Python 3.7+ and required packages installed:

```bash
pip install pymupdf jsonschema
```

## Place Input PDFs

Put your PDFs into the folder named input

## Run the script

Use the terminal to run the script with your desired input file : python process_pdfs.py input/your_input_file.pdf

## Schema Validation

The output is validated against the schema in:  output/output_schema.json

*This project works completely offline, takes an average time of 4.5 seconds and has processed 10 various kinds of PDFs for verification.*

## **How to run the code project**

docker build -t epithet:challenge1a .

docker pull epithet

docker run -v "path of Epithet(1A)\input:/app/input" -v "path of Epithet(1A)\output:/app/output" --network none epithet:latest
