def translator(text, convert_to = "English"):


    import os

    #key_file = open('C:\\Users\\nagar\\OneDrive\\Documents\\GenAI - LangChain\\OAIAPI_KEY.txt')
    #api_key = key_file.read()
    api_key = st.secrets["OPENAI_API_KEY"]

    from langchain_openai.chat_models import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.prompts import SystemMessagePromptTemplate, ChatMessagePromptTemplate
    from langchain_core.prompts import AIMessagePromptTemplate, HumanMessagePromptTemplate

#def translator(text, convert_to = "English"):

    #Creating a chat object 
    chat = ChatOpenAI(model = "gpt-3.5-turbo", openai_api_key = api_key)
    
    #Defining the model role through system template
    system_template = """ 
    You are a effective Translator,
    Translates given text to {convert_to} language without changing meaning and context.   
    """ 
    
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    #Defining the user request with human message template
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    #Creating chat template
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    prompt = chat_prompt.format_prompt(text = text,
                                       convert_to = convert_to).to_messages()
    
    result = chat.invoke(prompt)

    return result.content



    

