# example_02.py
 
import docx2txt
 
 
def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
 
if __name__ == '__main__':
    print(extract_text_from_docx('./SOUMYA 126 RESUME.docx'))  # noqa: T001