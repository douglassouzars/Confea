import PyPDF2

arquivo_pdf = open('arquivo1.pdf','rb')
pdf = PyPDF2.PdfFileReader(arquivo_pdf)
pagina = pdf.getPage(0)
print(pagina.extractText())