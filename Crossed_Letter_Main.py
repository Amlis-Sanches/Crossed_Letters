# Import necessary libraries
import docx
import PyPDF2
from PIL import Image, ImageDraw, ImageFont

# Function to extract text from various formats
def extract_text(file_path, file_type):
    # Identify file type. If text, return text
    try:
        match file_type:
            case "text":
                with open(file_path, "r") as file:
                    text = file.read()
            case "word":
                doc = docx.Document(file_path)
                full_text = []
                for para in doc.paragraphs:
                    full_text.append(para.text)
                text = "\n".join(full_text)
            case "pdf":
                pdf_file = open(file_path, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                full_text = []
                for page in range(pdf_reader.numPages):
                    page_obj = pdf_reader.getPage(page)
                    full_text.append(page_obj.extractText())
                text = "\n".join(full_text)
            case _:
                pass
    except:
        text = "Error"
    #return just a string with all the text from the file
    return text
    
def text_clean(text):
    #clean text for generation
    cleaned_text = text.replace('\n', '')
    return cleaned_text

    pass
    

# Function to generate crossed letter image/document
def generate_crossed_letter(text):
    print(text) #currently a test for the extracting test function
    # Create a new image or document
    # Write first set of text in blue
    # Rotate and write second set of text in red
    # Process overlapping areas to create purple
    # Save the output
    pass

# Main function to handle the workflow
def main():
    # Get file path and type from user
    file_path = input("Enter the file path: ")

    # Validate filetype and if wrong file type is entered, ask again
    while True:
        file_type = input("Enter the file type (text/word/pdf): ")
        if file_type in ["text", "word", "pdf"]:
            #try to confirm and extract text from file
            text = extract_text(file_path, file_type)
            if text == "Error":
                print("File Error extracting text. Please try again.")
            else:
                break
        elif file_type == "exit":
            print("Good Bye!")
            exit()
        else:
            print("Invalid file type. Please try again.")

    #clean text for generation
    text = text_clean(text)
    # Generate crossed letter
    generate_crossed_letter(text)

if __name__ == "__main__":
    main()
