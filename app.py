import streamlit as st
from text_translator import translator
from pdf_reader import msaPdfReader
from text_to_speech import lang_keys, lang_values, position, TextToSpeech

# Defining functions required to display user text and converted text
def text_conv_display(user_text,language):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Entered Text")
        st.write(user_text)
    with col2:
        st.subheader("Converted Text")
        conv_text = translator(text = user_text, convert_to = language, api_key = st.secrets["OPENAI_API_KEY"])
        st.write(conv_text)
    return conv_text

# Defining function to reset the app to initialization stage.
def reset():
    st.session_state.name = ''

# Streamlit app "Multilingual Storytelling with Accents" starts here.
# app title
st.title(':blue[Multilingual SWA]') 
# creating a list of conversions in the app for user selection.
list_of_values = ["Select source for conversion","Text to Text Conversion","Text file to Text conversion", "PDF File to Text conversion"]
# creating a list of user names to access the app functionality.
allowed_names = ["Edureka", "Nagaraju"] 
# prmpting user to enter login name to access app.
name = st.text_input(':blue[Enter your name or organization name]', key = 'name')
# validating user input for name with names allowed to access.
if name in allowed_names:
    st.success('Access granted')
    # creating a form enabling user selection and executing the functions based on user selection.
    with st.form(key="Submit"):
        # enabling the users to select conversions and langauges available.        
        operation = st.selectbox(":blue[Please select operation]", list_of_values)
        language = st.selectbox(":blue[Enter the target language]", lang_values, key='language')
        position = lang_values.index(language)
        # Code to execute when user selection is "Text to Text conversion"
        if operation == "Text to Text Conversion": # validating user selections.
            user_text = st.text_area(':blue[Enter your text]', max_chars=1000) # Enabling the user to enter free hand text with max of 1000 charecters.
            st.write(':orange[*If text is more than 1000 charecters, please use "Text file to Text conversion".]') # Display mesg if more than 1000 chars required.
            submit1 = st.checkbox(label= ":blue[Select to convert Text]") # getting confirmation from user to convert.
            
            if submit1: # validating user confirmation for conversion.
                st.success(':green[Text submitted for conversion]')
                conv_text = text_conv_display(user_text,language = language) # calling text conversion display function with user input text and target langauge.
                audio_check_box = st.checkbox(":blue[Select if Audio is required]") # getting confirmation from user if audio is needed.
                if audio_check_box:
                    audio_file = TextToSpeech(text = conv_text, lang=lang_keys[position]) # calling text to audio conversion function.
                    st.audio(audio_file) # playing audio
                    st.write(':red[**To download the audio file, please click on ellipsis next to the audio and chose downlaod option.]')
                            
        if operation == "PDF File to Text conversion":
            uploaded_file = st.file_uploader(':blue[Choose your .pdf file]', type="pdf") # Only accepting pdf file and if other files are uploaded it shows error message.
            submit1 = st.checkbox(":blue[Confirm file upload]")
            user_text = ""

            if submit1:
                if uploaded_file is not None:
                    user_text = msaPdfReader(uploaded_file) # passing uploaded file to pdf reader function from pdf_reader module and storing extracted text to user_text variable.
                    st.success(':green[File submitted for conversion]')
                    conv_text = text_conv_display(user_text,language = language) # calling text conversion to target language function.
                    audio_check_box = st.checkbox(":blue[Select if Audio is required]")
                    if audio_check_box:
                        audio_file = TextToSpeech(text = conv_text, lang=lang_keys[position]) # generating audio for converted text.
                        st.audio(audio_file) #playing audio
                        st.write(':red[**To download the audio file, please click on ellipsis next to the audio and chose downlaod option.]') 
        
        if operation == "Text file to Text conversion":
            uploaded_file = st.file_uploader(":blue[Choose your .txt file]", type="txt") # Allowing users to upload text file.
            submit1 = st.checkbox(":blue[Confirm file upload]")
            user_text = ""

            if submit1:
                if uploaded_file is not None:
                    user_text = uploaded_file.read() #Reading text file
                    st.success(':green[File submitted for conversion]')
                    conv_text = text_conv_display(user_text,language = language) #calling text conversion function.
                    audio_check_box = st.checkbox(":blue[Select if Audio is required]")
                    if audio_check_box:
                        audio_file = TextToSpeech(text = conv_text, lang=lang_keys[position]) # calling audio conversion function.
                        st.audio(audio_file) 
                        st.write(':red[**To download the audio file, please click on ellipsis next to the audio and chose downlaod option.]')

        st.form_submit_button("Submit") # This form button allows user to submit selection.
                    
else:
    st.error("No access, please enter a valid name.")

st.button('Exit', on_click=reset) # This Exit button calls reset function to clear the user access, making app to initiate from start.
