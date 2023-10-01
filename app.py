#streamlit bible
from os import write
import streamlit as st
import random
import streamlit.components.v1 as stc
import neattext.functions as nfx


#EDA packages import pandas as pd


#Data viz pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt
import pandas as pd





#utils
@st.cache_data
def load_bible(data):
    df=pd.read_csv("data/kjv.csv")
    return df

def main():
 st.title("streamlitbible")
menu=["Home","Multiverse","About"]
df=load_bible("data/kjv.csv")


choice=st.sidebar.selectbox("Menu",menu)
if choice =="Home":
    st.subheader("single verse search")
   # st.dataframe(df)
    book_list=df['book_name'].unique().tolist()
    book_name=st.sidebar.selectbox("book",book_list)
    chapter=st.sidebar.number_input("chapter",1)
    verse=st.sidebar.number_input("verse",1)
    bible_df = df[df['book_name'] == book_name]
   # st.dataframe(bible_df)
    #layout
    
    c1,c2=st.columns([2,1])
        # Single Verse Layout
    with c1:

            try:
                selected_passage = bible_df[
                    (bible_df['chapter_number'] == chapter) & (bible_df['verse_number'] == verse)
                   # st.write(selected_passage)
                ]
                passage_details = "{} Chapter::{} Verse::{}".format(
                    book_name, chapter, verse
                )
                st.info(passage_details)
                passage = "{}".format(selected_passage["verse_text"].values[0])
                st.write(passage)
            except  Exception  as e:
                st.warning("Book out of Range")
    with c2:
        st.success("verse of the day")
        chapter_list = range(10)
        verse_list  = range(20)
        ch_choice = random.choice(chapter_list)
        vs_choice = random.choice(verse_list)
        random_book_name = random.choice(book_list)
            
        st.write("Book:{},Ch:{},Vs:{}".format(random_book_name,ch_choice,vs_choice))
    rand_bible_df = df[df["book_name"] == random_book_name]
    randomly_selected_passage=rand_bible_df[(rand_bible_df['chapter_number'] == chapter) & (bible_df['verse_number'] == verse)]
    st.write(randomly_selected_passage['verse_text'])
        
elif choice =="Multiverse":
    st.subheader("Multiverse retrival")
else:
    st.subheader('About')
    
    
    
    
    
    
    
if __name__ == '__main___':
     main()   


    