# MultilingualTextToSpeech
## Multilingual Storytelling with Accents (MSA) 
# Introduction
Multilingual Storytelling with Accents (MSA) is a Streamlit application designed to facilitate seamless text translation and speech synthesis across multiple languages. It integrates various modules to enable efficient text extraction from TEXT, PDF files, translation using state-of-the-art language models, and conversion of text to speech. 
With MSA, users can effortlessly translate their stories to diverse languages and emphasize their storytelling experiences.
This application is built using Python 3.11.8

# Required Python Packages
Ensure the following Python packages are installed to run MSA:
•	streamlit: Used for creating interactive web applications.
•	pdfminer.six: A PDF parsing library for extracting text from PDF files.
•	langchain-openai: Provides access to the LangChain OpenAI model for text translation.
•	gtts: Google Text-to-Speech library for converting text to speech.

# Modules Overview
1.	pdf_reader.py: This module facilitates the extraction of text content from PDF files. It utilizes the pdfminer.high_level library to parse PDF files and extract text from each page.
2.	text_translator.py: The translator function within this module leverages the LangChain OpenAI model to perform text translation between different languages. It ensures that the meaning and context of the text are preserved during translation.
3.	text_to_speech.py: This module enables the conversion of text to speech using the gTTS (Google Text-to-Speech) library. It supports various languages and provides the flexibility to generate speech output in the desired language.
4.	app.py: The main Streamlit application integrates the functionalities of the modules. It provides a user-friendly interface for users to interact with the application, including options for text translation, PDF text extraction, and text-to-speech conversion.

# Access Control
Access to the MSA application is restricted based on predefined usernames or organization names. Only users with specified names are granted access to the application functionalities.
Users should enter the given username for access in “Your Name or Organization name” input area of the app.  Once provided app validate provided name with Streamlit cloud app secrets for authentication.

# Functionality
App enables the authenticated users to provide input text in form of “free text”, “.txt or .pdf” files and select target language to convert the provided text. Once submitted, app will display both given text and converted text and provide option for user to create audio from the converted text and download the audio file. Once completed, user can click on “Exit” button to exit from his session.

# Text to Text Conversion: 
Users select this option to provide input text in form of free text and convert to select target language.
•	Operation: Once selected and submitted, allows users to translate text from one language to another.
•	Usage:
•	Enter the text to be translated in the provided text area.
•	Select the target language from the dropdown menu and submit selection.
•	Click the checkbox labeled "Select to convert Text" and submit your text, to confirm and initialize the translation process.
•	Optionally, enable the checkbox for audio generation if speech synthesis is required.
•	Limitation: Supports translation of text up to 1000 characters. If text is more than limit, user can select “Text file to Text conversion”.

# PDF File to Text Conversion
•	Operation: Enables extraction of text content from uploaded PDF files.
•	Usage:
•	Upload a PDF file from user computer using file browser option.
•	Click "Confirm file upload" and submit to initiate the conversion process.
•	Optionally, enable the checkbox for audio generation to convert the extracted text to speech.
•	Limitation:  Based on the PDF file and structure within the file submitted, there is a chance of loss of data or misrepresentation of data. Advised to use PDF files with less complex layouts.

# Text File to Text Conversion
•	Operation: Reads text content from uploaded text files (.txt).
•	Usage:
•	Upload a text file using the file uploader component.
•	Click "Confirm file upload" and submit to initiate the conversion process.
•	Optionally, enable the checkbox for audio generation to convert the extracted text to speech.

# Exit
•	Click the "Exit" button to reset the application and clear user access, initiating the app from the start.

