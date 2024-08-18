import streamlit as st

from PIL import Image



with open("app.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


about_page = st.Page(
    page= "views/about_me.py",
    title="About me",
    icon=":material/face_6:",
   
    default=True,
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="CHAT ME:",
    icon=":material/robot:",
)


pg = st.navigation(
    {
        "Info": [about_page],
        "motivator":[project_2_page]
    }
)


st.sidebar.text("Made by Caryll Cariño")


pg.run()


