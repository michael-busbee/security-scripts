from pathlib import Path
import docx
import PyPDF2
from email import policy
from email.parser import BytesParser
from openpyxl import load_workbook  # For .xlsx files
from pptx import Presentation  # For .pptx files
from pyrtf_ng import Rtf15Reader, plaintext  # For .rtf files


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
        
        
        elif file_extension == ".xlsx":
            # Read XLSX file
            workbook = load_workbook(file_path, read_only=True)
            lines = []
            for sheet in workbook:
                for row in sheet.iter_rows(values_only=True):
                    cells = [(str(cell) if cell is not None else "") for cell in row]
                    lines.append("\t".join(cells))
            extracted_text = "\n".join(lines)

        
        elif file_extension == ".pptx":
            # Read PPTX file
            presentation = Presentation(file_path)
            slides_text = []
            for slide in presentation.slides:
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        slides_text.append(shape.text)
            extracted_text = "\n".join(slides_text)

        
        elif file_extension == ".rtf":
            # Read RTF file
            with open(file_path, "rb") as f:
                doc = Rtf15Reader.read(f)
            extracted_text = plaintext.PlaintextWriter.write(doc).getvalue()
        
        
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