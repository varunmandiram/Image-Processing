from pdf2image import convert_from_path
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

def pdf_convertor(filename): 
    filenames=[]
    pages = convert_from_path(filename,300)
    filename = filename[:-4]
    for page in pages:
        page.save("%s.jpg" % (filename), "JPEG")
        filenames.append("%s.jpg" % (filename))        
    return filenames


def pdf_split_convertor(file_name): 
    filenames=[]
    fname = os.path.splitext(os.path.basename(file_name))[0]
    pdf = PdfFileReader(file_name)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}-{}.pdf'.format(
            fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        jpg_file_name=pdf_convertor(output_filename)
        filenames.append(jpg_file_name[0])
 
    return filenames

if __name__ == "__main__":
    filename= sys.argv[1]
    ##Input an pdf here
    pdf_split_convertor(filename)