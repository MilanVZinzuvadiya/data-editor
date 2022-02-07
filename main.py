import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz

import pickle

try:
    index = pickle.load(open("var.pickle", "rb"))
except (OSError, IOError) as e:
    index = 0
    pickle.dump(index, open("var.pickle", "wb"))


def red_negatives(series):
    highlight = 'background-color: #ffe6e6;'
    default = ''
    return [highlight if e == 0 else default for e in series]

def fuzzy_bold(s):
    wrds = s.split(' ')
    prnt = ""
    for w in wrds:
        if fuzz.ratio(w.lower(),search_keyword.lower())>50:
            prnt = prnt + "**"+w+"** "
        else:
            prnt = prnt + w + " "
    return prnt

st.write("""
# Search Sythetic DATA
""")
st.subheader('by Milan Zinzuvadiya')
st.sidebar.header('MetaDATA')
dg = st.sidebar.text_input("Data generator")

#df = pd.read_csv('demo.csv')
#chng = True


l = ['demo.csv','demo2.csv']


def create_csv(s):

    df = pd.read_csv(s)
    search_keyword = st.text_input('Search Keyword')

    relevents = []
    for ind,row in df.iterrows():
        prnt = row['title']
        if search_keyword !='':
            prnt = fuzzy_bold(prnt)
        
        st.markdown("""---""")
        st.info(prnt)
        if row['relevent'] == 1:
            relevents.append(st.checkbox("relevent",key=ind,value=True))
        else:
            relevents.append(st.checkbox("relevent",key=ind))
        
        st.text("")


    #st.text(list(map(lambda x: 1 if x else 0,relevents)))
    #st.text(relevents)

    df['new'] = list(map(lambda x: 1 if x else 0,relevents))

    st.header(dg)
    st.dataframe(df.style.apply(red_negatives,axis=0,subset=['relevent']))

if st.button("ChangeCSV"):
    create_csv(l[index])
    index = index + 1
    pickle.dump(index, open("var.pickle", "wb"))

#with col2: 
#    for ind,row in df.iterrows():
#        if row['relevent'] == 1:
#             st.success("1")
#       else:
#           st.error("0")
#        st.warning(row['relevent'])
#st.warning("Warning")

