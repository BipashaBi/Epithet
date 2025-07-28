FROM python:3.12.2
WORKDIR /app
RUN pip install --no-cache-dir pymupdf jsonschema
COPY process_pdfs.py .
CMD ["python", "process_pdfs.py"]
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

