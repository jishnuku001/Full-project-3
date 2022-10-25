from pyrsistent import v
import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('model.sav', 'rb'))

st.title('University Rank List')
st.sidebar.header('Rank List')
image = Image.open('Rankers.jpg')
st.image(image,'Rankers')

def user_report():
    ar_score = st.sidebar.slider('ar score', 0, 143, 465 )
    ar_rank = st.sidebar.slider('ar rank', 0, 364, 490 )
    er_score = st.sidebar.slider('er score', 0,20, 98 )
    er_rank = st.sidebar.slider('er rank', 0,362, 487 )
    fsr_score = st.sidebar.slider('fsr score', 0,29, 99 )
    fsr_rank = st.sidebar.slider('fsr rank', 0,417, 561 )
    cpf_score = st.sidebar.slider('cpf score', 0,23, 97 )
    cpf_rank = st.sidebar.slider('ecpf rank', 0,425, 574 )
    ifr_score = st.sidebar.slider('ifr score', 0,30, 98 )
    ifr_rank = st.sidebar.slider('ifr rank', 0,435, 595 )
    isr_score = st.sidebar.slider('isr score', 25,0, 98 )
    isr_rank = st.sidebar.slider('isr rank', 433,0, 590 )
    irn_score = st.sidebar.slider('irn score', 49,0, 99 )
    irn_rank = st.sidebar.slider('irn rank', 429,0, 583 )
    ger_score = st.sidebar.slider('ger score', 25,0, 99 )
    ger_rank = st.sidebar.slider('ger rank', 423,0, 572 )
    scoreger_score = st.sidebar.slider('scoreger score', 50,0, 315 )




    user_report_data = {
    'ar score':ar_score,
    'ar rank':ar_rank,
    'er score ':er_score ,
    'er rank ':er_rank ,
    'fsr score':fsr_score,
    'fsr rank':fsr_rank,
    'cpf scoreat':cpf_score,
    'cpf rank':cpf_rank,
    'ifr score':ifr_score,
    'ifr rank':ifr_rank,
    'isr score':isr_score,
    'isr rank':isr_rank,
    'irn score':irn_score,
    'irn rank':irn_rank,
    'ger score':ger_score, 
    'ger rank':ger_rank,
    'scoreger score':scoreger_score,
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


user_data = user_report()
st.header('Rank List Data')
st.write(user_data)

Rank = model.predict(user_data)
st.subheader('Rank List')
st.subheader(str(np.round(Rank[0], 2)))