# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:59:15 2021

@author: Junio
"""
# import
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# Fiche de la formation IDU
file = 'Programme_IDU_2021_2025.pdf'


# convertir le pdf en chaine de caracter
def convert_pdf_to_string(file):
    output_string = StringIO()
    with open(file, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return (output_string.getvalue())


# Contenue du pdf
pdfContent = convert_pdf_to_string(file)


# ETAPE 1
# Creer un fichier a partir des donnees obtenues
# afin de faciliter la gestion des données
def textCreator(pdfContent):
    splitPdfContent = pdfContent.split('\n')
    with open('pdfContent.text', 'w') as texte:
        for mot in splitPdfContent:
            texte.write(mot + '\n')
    texte.close()
    return texte


texte = textCreator(pdfContent)
