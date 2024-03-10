import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

input_prompt1 = """
 You are an experienced Technical Human Resource Manager with Tech Experience in the field of Data Science, Full Stack Web Development, Big Data Engineering, Devops, your task is to review the provided resume against the job description for these profiles. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.

 resume:{text}
description:{jd}
"""

input_prompt2 = """
You are an Technical Human Resource Manager with expertise in Data Science, Full Stack Web Development, Big Data Engineering, Devops, 
your role is to scrutinize the resume in light of the job description provided. 
Share your insights on the candidate's suitability for the role from an HR perspective. 
Additionally, offer advice on enhancing the candidate's skills and identify areas where improvement is needed.

resume:{text}
description:{jd}
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science, Full Stack Web Development, Big Data Engineering, Devops and Deep ATS functionality, 
your task is to evaluate the resume against the provided job description. As a Human Resource manager,
 assess the compatibility of the resume with the role. Give me what are the keywords that are missing.

resume:{text}
description:{jd}
"""

input_prompt4 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science, Full Stack Web Development, Big Data Engineering, Devops and Deep and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.

resume:{text}
description:{jd}
"""
input_prompt5="""
You are an expert mentor who is guiding everyone to improve their resume which will be score top in any ATS (Applicant Tracking System) scanner and you have expertise in deep understanding of data science, Full Stack Web Development, Big Data Engineering, your task is to evaluate the resume against the provided job description.
and provide the input user particularly where he/she has to edit the resume against the provided job description.

resume:{text}
description:{jd}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("What are the Keywords That are Missing")

submit4 = st.button("Percentage match")

submit5 = st.button("Where to edit")


if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)

if submit1:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt1)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit2:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt2)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit3:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt3)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit4:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt4)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit5:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt5)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")