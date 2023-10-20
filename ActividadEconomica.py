import PyPDF2

# Abrir PDF
with open('Catalogos.pdf', 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    with open('test.txt', 'w', encoding='cp1252') as g:
        for page in range(21,50):
            text = pdf.pages[page].extract_text()
            g.write(text)
         