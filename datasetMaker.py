import PyPDF2
import json
import os

#===================================================================================================
def extract_text_from_pdf(pdf_path, output_txt_path=None):
    """
    Extracts all text from a given PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
        output_txt_path (str, optional): Path to save the extracted text as a .txt file.
                                         If None, the text is just returned.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            extracted_text = ""

            for page in pdf_reader.pages:
                extracted_text += page.extract_text() + "\n"
        
        if output_txt_path:
            with open(output_txt_path, 'w') as txt_file:
                txt_file.write(extracted_text)
        
        return extracted_text
    
    except Exception as e:
        print(f"Error: {e}")
        return None

#===================================================================================================
def txt_to_jsonl(input_txt_path, output_jsonl_path):
    """
    Reads an input .txt file, processes it into JSONL format, 
    and writes the output into the specified JSONL file.
    """
    try:
        with open(input_txt_path, 'r') as txt_file:
            lines = txt_file.readlines()

        jsonl_data = []
        for line in lines:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            entry = {
                "contents": [
                    {"role": "user", "parts": [{"text": line}]},
                    {"role": "model", "parts": [{"text": "Placeholder response"}]}
                ]
            }
            jsonl_data.append(entry)

        with open(output_jsonl_path, 'w') as jsonl_file:
            for entry in jsonl_data:
                jsonl_file.write(json.dumps(entry) + '\n')

        print(f"Conversion successful!") 
    except Exception as e:
        print(f"Error during conversion: {e}")

#===================================================================================================
def remove_placeholder_sequence(input_jsonl_path, output_jsonl_path):
    """
    Removes the exact sequence:
    '{"role": "model", "parts": [{"text": "Placeholder response"}]}'
    from a .jsonl file.

    Args:
        input_jsonl_path (str): Path to the input .jsonl file.
        output_jsonl_path (str): Path to save the cleaned .jsonl file.
    """
    target_sequence = '"role": "model", "parts": [{"text": "Placeholder response"}]'
    
    try:
        with open(input_jsonl_path, 'r') as infile, open(output_jsonl_path, 'w') as outfile:
            for line in infile:
                # Remove target sequence from the line
                cleaned_line = line.replace(target_sequence, "")
                outfile.write(cleaned_line)

        print(f"File extracted, converted and cleaned as: {output_jsonl_path}")
    except Exception as e:
        print(f"Error processing file: {e}")

#===================================================================================================
def delete_residual_files(file_paths):
    """
    Deletes a list of residual files if they exist.

    Args:
        file_paths (list): A list of file paths to delete.
    """
    for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")        

#===================================================================================================
#pdf_file_path = "M. Shifman - Advanced Topics in Quantum Field Theory. A Lecture Course.pdf" 
pdf_file_path = input("Enter the exactly path/name of the PDF file (e.g. /home/user/book.pdf): ")
output_txt_file_path = "extracted_text.txt" 
input_txt_path = output_txt_file_path
output_jsonl_path = 'converted_text.jsonl'

extracted_text = extract_text_from_pdf(pdf_file_path, output_txt_file_path)
if extracted_text:
    print("Text extraction successful!")
    # print(extracted_text)
txt_to_jsonl(input_txt_path, output_jsonl_path)

input_jsonl = "converted_text.jsonl"  
output_jsonl = "output_cleaned.jsonl"  
remove_placeholder_sequence(input_jsonl, output_jsonl)

residual_files = [
    "converted_text.jsonl",  
    "extracted_text.txt",
    # "debug_log.txt"
]
delete_residual_files(residual_files)
