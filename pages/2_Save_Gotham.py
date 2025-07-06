import streamlit as st
import random
import time
import json
import pandas as pd
import matplotlib.pyplot as plt


with open("data.json") as file:
    data = json.load(file)
    
success_data = pd.DataFrame(data[0])
failure_data = pd.DataFrame(data[1])
success_data["time"]= pd.to_numeric(success_data["time"])
failure_data["time"]= pd.to_numeric(failure_data["time"])



#NEW
st.markdown(""" <style> body{ background-color: #000000; color: white;}.stApp{background-color: #000000; color: white;}h1,h2,h3,h4,h5,h6,p,div,span,label{color=white !important;}.stRadio>div{background-color:#111111 !important; color: white !important; border-radius: 10px; padding: 10px;}.stButton>button{ background-color: #333333; color: white; border: none; border-radius: 10px; padding: 0.5em 1em;}.stButton>button:hover{background-color: #555555; color: white;}.stMetric{color: white !important;}</style> """, unsafe_allow_html = True)


st.set_page_config(page_title="The Nightfall", layout="centered")
#NEW
st.title("🦇🦇🦇The Nightfall🦇🦇🦇")


if "joker_level" not in st.session_state:
    #NEW
    st.session_state.joker_level = random.randint(30,80)
    st.session_state.crime_rate = random.randint(30,80)
    st.session_state.website_progress = random.randint(15,85)


st.subheader("The Current State of the Gotham:")
col1, col2, col3 = st.columns(3)
with col1:
    #NEW
    st.metric("🃏Joker Activity", f"{st.session_state.joker_level}")
with col2:
    st.metric("🚓 Crime Rate", f"{st.session_state.crime_rate}%")
with col3:
    st.metric("💻 Website Progress", f"{st.session_state.website_progress}%")

st.write("---")

st.subheader("What should I do tonight?:")
#NEW
choice = st.radio("Fight Joker if Activity is over 70, Stop Crimes if it's over 50%, else keep CODING:",["Fight Joker", "Stop Crimes", "Code the Website"])

def evaluate_choice(joker = 0, crime = 0, website = 0):
    if joker == 0 and crime == 0 and website == 0:
        joker = st.session_state.joker_level
        crime = st.session_state.crime_rate
        website = st.session_state.website_progress
    

    best_action = ""
    if joker>70:
        best_action =  "Fight Joker"
    elif crime > 50:
        best_action =  "Stop Crimes"
    else:
        best_action =  "Code the Website"

    if choice == best_action:
        #NEW
        st.success("✅ Great choice! Gotham is safer tonight.")
        st.session_state.joker_level = max(0, joker-random.randint(10, 30))
        st.session_state.crime_rate = max(0, crime-random.randint(10,30))
        st.session_state.website_progress = max(0, website+random.randint(5,15))
    else:
        #NEW
        st.error("⚠️ Not the best choice. Gotham gets more dangerous...")
        st.session_state.joker_level = max(0, joker+random.randint(5, 15))
        st.session_state.crime_rate = max(0, crime+random.randint(5,15))
        st.session_state.website_progress = max(0, website)

    #st.session_state.joker_level = max(0, joker+random.randint(5, 6))
    #st.session_state.crime_rate = max(0, crime+random.randint(5,6))
        
   

    st.write("---")
    st.subheader("Update Situation:")
    st.progress(st.session_state.joker_level/100, text =f"Joker Activity = {st.session_state.joker_level}")
    st.progress(st.session_state.crime_rate/100, text = f"Crime Rate = {st.session_state.crime_rate}")
    st.progress(st.session_state.website_progress/100, text= f"Website Progress = {st.session_state.website_progress}")



if st.session_state.joker_level >=90 or st.session_state.crime_rate>=90:
        st.title("Gotham Mission Report")
        st.subheader("🃏🃏🃏Defeated🃏🃏🃏")
        fig, ax = plt.subplots()
        ax.plot(failure_data["time"], failure_data["crime_rate"], label="Crime Rate", color='red')
        ax.plot(failure_data["time"], failure_data["joker_activity"], label="Joker Activity", color='purple')
        ax.plot(failure_data["time"], failure_data["site_progress"], label="Website Progress", color='green')
        ax.set_xlabel("Time")
        ax.set_ylabel("Level")
        ax.set_title("Gotham Trends")
        ax.legend()
        ax.grid(True)
        #NEW
        st.pyplot(fig)



if st.session_state.website_progress >= 80:
            st.title("Gotham Mission Report")
            success_new = success_data
            st.subheader("🦇🦇🦇Victory🦇🦇🦇")
            fig, ax = plt.subplots()
            ax.plot(success_data["time"], success_data["crime_rate"], label="Crime Rate", color='red')
            ax.plot(success_data["time"], success_data["joker_activity"], label="Joker Activity", color='purple')
            ax.plot(success_data["time"], success_data["site_progress"], label="Website Progress", color='green')
            ax.set_xlabel("Time")
            ax.set_ylabel("Level")
            ax.set_title("Gotham Trends")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

if st.button("Make Wise Choices..."):
       evaluate_choice(st.session_state.joker_level, st.session_state.crime_rate, st.session_state.website_progress)






















