import PyPDF2 as pydf
import os

merge = pydf.PdfFileMerger()

merge.append('file1.pdf')


list_files = os.listdir("./")

for file in list_files:
    if file.endswith(".pdf"):
        merge.append(file)

merge.write('PDF_FINAL.pdf')
