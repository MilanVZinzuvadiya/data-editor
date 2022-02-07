import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz



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
dg = st.sidebar.text_input("Domain Expert")
exp = st.sidebar.text_input("Experiment Name")
number = st.sidebar.number_input('Query Number/Index',value=0)
search_keyword = st.sidebar.text_input('Search Keyword')
#df = pd.read_csv('demo.csv')
#chng = True

#index = 0
l = ['demo.csv','demo2.csv']


#csv = st.sidebar.text_input('CSV FILE:')

#csv=l[]
df = pd.read_csv(l[number])


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

filename = dg+'_'+exp+'_'+l[number]
st.header(filename)
st.dataframe(df.style.apply(red_negatives,axis=0,subset=['relevent']))

if st.button("SaveCSV in gen_data "):
    df.to_csv('gen_data/'+filename)
    st.success('SAVED :: gen_data/'+filename+'.csv')
#with col2: 
#    for ind,row in df.iterrows():
#        if row['relevent'] == 1:
#             st.success("1")
#       else:
#           st.error("0")
#        st.warning(row['relevent'])
#st.warning("Warning")

