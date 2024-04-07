#from langchain_community.document_loaders import PDFMinerLoader

# def msaPdfReader(file):
    
#     from langchain_community.document_loaders import PyPDFLoader

#     loader = PyPDFLoader(file)
#     pages = loader.load_and_split()

#     result = ''''''

#     while pages:
#         for i in range(0,len(pages)):
#             result = result + pages[i].page_content
#         break

#     return result

# using pdfminer python module to read python files.
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

# defning function to accept file object and go through each file and read text available in PDF containers.
def msaPdfReader(file):
    text = ""
    for page_layout in extract_pages(file):
                    for element in page_layout:
                        if isinstance(element, LTTextContainer):
                            text = text + element.get_text()
    
    return text