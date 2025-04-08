import argparse
from docx import Document
import string

parser = argparse.ArgumentParser(description='Words in texts')
parser.add_argument("path", type=str, help="Path to the doc file")
args = parser.parse_args()

tx = ''
doc = Document(args.path)
for par in doc.paragraphs:
    tx += par.text
for x in string.punctuation:
    if x in tx:
        tx = tx.replace(x, '')
lst = tx.split()
print(len(lst))

# 2024_2_КР_ИЛ_ФИПЛ_ЕремченкоКВ.docx --> 9812
