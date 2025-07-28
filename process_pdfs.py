import os
import json
import re
import logging
from pathlib import Path
import fitz  # PyMuPDF

# Set up logging for informative output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Threshold constants for deciding heading levels by font size ratio
H1_THRESHOLD = 1.8
H2_THRESHOLD = 1.4

def extract_text_with_fonts(doc):
    """
    Extract text spans with font, size, and page info from the PDF document.
    Returns a list of spans.
    """
    spans = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict", flags=11).get("blocks", [])
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if text:
                            spans.append({
                                "text": text,
                                "font": span["font"],
                                "size": round(span["size"], 2),
                                "flags": span["flags"],
                                "page": page_num
                            })
    return spans

def clean_text(text):
    """Clean and normalize text to remove excessive whitespace."""
    return re.sub(r'\s+', ' ', text).strip()

def extract_title_and_headings(spans):
    """
    Extract document title and outline (headings with levels and pages) from spans.
    Returns (title, outline).
    """
    spans = [s for s in spans if s["text"] and len(s["text"]) > 3]
    if not spans:
        return None, []

    # Determine normal font size by frequency
    size_counts = {}
    for s in spans:
        sz = s["size"]
        size_counts[sz] = size_counts.get(sz, 0) + 1

    sorted_sizes = sorted(size_counts.items(), key=lambda x: -x[1])
    if not sorted_sizes:
        return None, []

    normal_size = sorted_sizes[0][0]
    heading_spans = [s for s in spans if s["size"] > normal_size]

    if not heading_spans:
        title_span = max(spans, key=lambda s: s["size"])
        return title_span["text"], []

    title_span = max(spans, key=lambda s: s["size"])
    title = title_span["text"]

    outline = []
    for s in heading_spans:
        size_ratio = s["size"] / normal_size
        if size_ratio >= H1_THRESHOLD:
            level = "H1"
        elif size_ratio >= H2_THRESHOLD:
            level = "H2"
        else:
            level = "H3"
        outline.append({
            "level": level,
            "text": clean_text(s["text"]),
            "page": s["page"]
        })

    # Sort outline by page and position for logical ordering
    outline.sort(key=lambda x: (x["page"], spans.index(next(t for t in spans if clean_text(t["text"]) == x["text"]))))

    return title, outline

if __name__ == "__main__":
    input_dir = "/app/input"
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]
    if not pdf_files:
        logging.warning(f"No PDF files found in {input_dir}")
        exit(0)

    logging.info(f"Processing {len(pdf_files)} PDF file(s)...")

    for filename in pdf_files:
        pdf_path = os.path.join(input_dir, filename)
        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            logging.error(f"Cannot open {filename}: {e}")
            continue

        try:
            spans = extract_text_with_fonts(doc)
            title, outline = extract_title_and_headings(spans)
            if title is None:
                logging.warning(f"No title extracted from {filename}")
                title = ""
        except Exception as e:
            logging.error(f"Error processing {filename}: {e}")
            continue

        output_data = {
            "title": title,
            "outline": outline
        }

        output_file = output_dir / (Path(filename).stem + ".json")
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            logging.info(f"Saved outline for {filename} → {output_file.name}")
        except Exception as e:
            logging.error(f"Failed to write JSON for {filename}: {e}")
