Here’s a cleaner, professional, and properly formatted version of your README for the GitHub project **Epithet**:

---

# 📘 Epithet: An Offline PDF Outline Extractor

**Epithet** is a lightweight Python utility that extracts titles and hierarchical headings from PDF files and organizes them into a structured outline. The entire workflow is performed **offline**, making it fast, secure, and privacy-friendly. It generates a JSON summary of any PDF document’s major sections.

---

## 🔍 Features

* 📄 Parses PDF text and analyzes font metadata
* 🧠 Automatically detects:

  * Document title
  * H1, H2, and H3 headings based on font size hierarchy
* ⚡ Fully offline with quick processing (\~4.5s per document)
* ✅ Outputs a structured and schema-validated JSON outline

---

## 🧠 How It Works

Epithet follows these steps:

1. **Parse PDF**
   Uses [PyMuPDF (`fitz`)](https://pymupdf.readthedocs.io/) to extract:

   * Text spans
   * Font size, style, and positional data

2. **Detect Headings**

   * The largest font is treated as the **title**
   * Larger-than-body fonts are categorized as:

     * `H1`, `H2`, or `H3` based on size thresholds

3. **Generate Output**
   Produces a JSON file containing:

   * The **title**
   * A **list of headings** with:

     * Hierarchical level
     * Page number

---

## 📦 Dependencies

* [PyMuPDF (fitz)](https://pypi.org/project/PyMuPDF/) – for PDF parsing
* Standard Python libraries:

  * `re`, `os`, `json`, `pathlib`, `logging`

Install with:

```bash
pip install pymupdf jsonschema
```

---

## 📁 Project Structure

```
EPITHET1A/
├── app/
│   ├── process_pdfs.py
│   ├── Dockerfile
│   ├── README.md
│   ├── requirement.txt
│   ├── sample_dataset/
│   ├── input/
│   ├── output/
│   └── schema/
│       └── output_schema.json
```

---

## 🚀 Usage

### 🔧 Local Execution

1. **Prepare Input**
   Place PDFs in the `input/` folder.

2. **Run Script**

   From the `app/` directory, run:

   ```bash
   python process_pdfs.py input/your_input_file.pdf
   ```

3. **View Output**
   The structured outline will be saved as a JSON file in the `output/` folder.

### ✅ Schema Validation

All output is validated against:
`schema/output_schema.json`

---

## 🐳 Docker Usage

### Build the Image

```bash
docker build -t epithet:latest .
```

### Run the Container

```bash
docker run \
  -v "/path/to/EPITHET1A/input:/app/input" \
  -v "/path/to/EPITHET1A/output:/app/output" \
  --network none \
  epithet:latest
```

> Replace `/path/to/EPITHET1A/` with the actual local path.

---

## 📈 Performance

* ✅ **Offline-only** — No external requests
* ⚡ **Average Speed** — \~4.5 seconds per PDF
* 🔗 **Output Format** — Clean JSON for downstream use or integration

---

Let me know if you'd like me to create a badge-enhanced version or a `GIF demo` section.
