Epithet: An Offline PDF Outline Extractor
Epithet is a Python utility designed to automatically extract titles and hierarchical headings from PDF files, and organize them into a structured outline. The workflow is completely offline and fast, providing a JSON summary of any PDF document’s major sections.

Approach
Epithet works by:

Parsing PDF text using [PyMuPDF] (fitz).

Extracting text spans along with font size, style, and position metadata.

Automatically detecting headings:

The largest font is identified as the title.

Other fonts larger than the main body text are categorized as H1, H2, or H3 headings based on size hierarchy.

Outputting a JSON file containing:

The document’s title

A list of headings, their hierarchy levels, and page numbers

Dependencies
PyMuPDF (fitz) – For text and font analysis in PDFs

Standard libraries: re, os, json, pathlib, and logging

Project Structure
text
EPITHET1A/
│
├── app/
│    ├── process_pdfs.py
│    ├── Dockerfile
│    ├── README.md
│    ├── sample_dataset/
│    ├── input/
│    ├── output/
│    ├── requirement.txt
│    └── schema/
│         └── output_schema.json
Installation & Running
Dependencies

Make sure you have Python 3.7+:

bash
pip install pymupdf jsonschema
Input PDFs

Place your source PDFs in the input folder.

Execute Script

From app directory, run:

bash
python process_pdfs.py input/your_input_file.pdf
Schema Validation

Output JSON is validated using schema/output_schema.json.

Performance & Usage
Fully offline: No internet access required

Average processing time: 4.5 seconds per PDF (tested on various document types)

Output is stored as a structured outline JSON for easy integration or post-processing

Docker Usage
Build the image:

bash
docker build -t epithet:latest .
Run the container (replace local paths as needed):

bash
docker run -v "/path/to/EPITHET1A/input:/app/input" -v "/path/to/EPITHET1A/output:/app/output" --network none epithet:latest

