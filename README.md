
Crossed Letter Image Generator v0.2.3
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