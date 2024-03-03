import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q2_K.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response






st.set_page_config(page_title="Generate Blogs",
                    page_icon=':computer:',
                    layout='wide',
                    initial_sidebar_state='auto',
                    menu_items={
        'Get Help': 'mailto:sayanmondal2098@gmail.com?subject=Need help about blog generation Site',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Created by Sayan"
    })

st.header("Generate Blogs")

input_text=st.text_input("Enter Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([7,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Common People'),index=0)
    
submit=st.button("Generate Blog")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))