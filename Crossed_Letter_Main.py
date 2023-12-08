'''
Crossed Letter Image Generator v0.0.1
Last edit made by: Nathaniel Horn
#------------------------------------------------------------------------------#
This Python script is designed to transform text from various file formats 
(text, Word, PDF) into a 'Crossed Letter' image or document. The process involves:

Inputs:
- File path of the text source.
- File type (text, word, pdf).

Steps:
1. Extract text from the input file.
2. Clean the extracted text for processing.
3. Generate an image or document where:
   a. The first set of text runs left to right in blue.
   b. The document/image is then rotated 90 degrees.
   c. A second set of text is overlaid in red.
   d. Where texts overlap, the colors blend to create purple.
4. Save the output as an image or document.

Desired Output:
A Crossed Letter image or document with the specified text, saved in the user's system.
The image will have the first set of text running left to right in blue, and the second
set of text running top to bottom in red. Where the texts overlap, the colors will blend
to create purple.
'''

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
                text = "Program Error"
    except:
        text = "Error! Text document not identified. Please try again."
    #return just a string with all the text from the file
    return text
    
def text_clean(text):
    # Clean text for generation
    cleaned_text = text.replace('\n', '')
    cleaned_text = cleaned_text.replace('\t', '')
    
    # Shape test to fit for the desired image
    for i in range(0, len(cleaned_text), 80):
        if i % 80 == 0:
            cleaned_text = cleaned_text[:i] + '\n' + cleaned_text[i:]
    
    # Count the total number of lines and determine how many images will be processed
    total_lines = len(cleaned_text.split('\n'))
    # split lines after you reach 32 lines so the \n fits the image
    half_length = 32 #Set to a specific number to fit the desired image
    totalImage = round(total_lines // (half_length * 2))

    cleaned_text_lines = cleaned_text.split('\n')

    cleaned_text_1 = '\n'.join(cleaned_text_lines[:half_length])
    cleaned_text_2 = '\n'.join(cleaned_text_lines[half_length:])
    
    return cleaned_text_1, cleaned_text_2, totalImage


'''
The generate_crossed_letter function is designed to create an image that 
displays two layers of text in different colors (blue and red) overlaid 
in a "crossed letter" style
'''
def generate_crossed_letter(text1, text2):
    # Create a new image
    img = Image.new('RGB', (500, 500), color = (255, 255, 255)) #for testing
    draw = ImageDraw.Draw(img)

    # Select a font
    font = ImageFont.load_default()

    # Add first layer of text in blue
    draw.text((10, 10), text1, fill=(0, 0, 255), font=font)

    # Rotate the image
    img = img.rotate(90, expand=1)

    # Create a new drawing context for the rotated image
    draw = ImageDraw.Draw(img)

    # Add second layer of text in red
    draw.text((10, 10), text2, fill=(255, 0, 0), font=font)

    # Save the image
    img.save('crossed_letter.png')


'''
Main function to handle the workflow.


Here i will recieve the text varables in a list and then pass them through the generate_crossed_letter function. 
'''
def main():
    # Get file path and type from user
    # Validate filetype and if wrong file type is entered, ask again
    while True:
        file_path = input("Enter the file path: ")
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
    '''
    clean text for generation and return two lists filled with the text string variables.
    I create the list inside the function because I want to have everything formed befor 
    I pass it to the generate_crossed_letter function.
    '''
    text_1, text_2 = text_clean(text)
    print(text_1, '\n')
    print(text_2)
    # Generate crossed letter
    generate_crossed_letter(text_1, text_2)
    print("Crossed Letter Generated!")

if __name__ == "__main__":
    main()
