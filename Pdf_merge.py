import PyPDF2

pdfiles = ['1.pdf','2.pdf']
merger = PyPDF2.pdfMerger()
for filename in pdfiles:
    pdfFiles = open(filename,'rb')
    pdfreader = PyPDF2.pdfreader(pdfFiles)
    merger.append(pdfreader)
    
pdfFiles.close()
merger.write('merged.pdf')