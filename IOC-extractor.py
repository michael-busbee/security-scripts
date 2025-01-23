from pathlib import Path
import docx
import PyPDF2
from email import policy
from email.parser import BytesParser

def read_text(file_path):

    file_path = Path(file_path)
    
    if not file_path.is_file():
        raise ValueError(f"The path '{file_path}' is not a valid file.")

    file_extension = file_path.suffix.lower()
    extracted_text = ""

    try:


        if file_extension == ".pdf":
            # Read PDF file
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                extracted_text = "".join([page.extract_text() for page in pdf_reader.pages])


        elif file_extension == ".docx":
            # Read DOCX file
            doc = docx.Document(file_path)
            extracted_text = "\n".join([paragraph.text for paragraph in doc.paragraphs])


        elif file_extension == ".eml":
            # Read EML file
            with open(file_path, 'rb') as file:
                msg = BytesParser(policy=policy.default).parse(file)
                extracted_text = msg.get_body(preferencelist=('plain')).get_content() if msg.is_multipart() else msg.get_content()
        
        else:
            # Read text file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                extracted_text = file.read()

    except Exception as e:
        raise ValueError(f"An error occurred while reading the file '{file_path}': {e}")

    return extracted_text

def main():
    print(read_text("testdoc.docx"))


if __name__ == "__main__":
    main()