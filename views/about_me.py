import streamlit as st


from form.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


resume_file_path = "cv.pdf"

# Read the PDF file as bytes
with open(resume_file_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

# Define the file name for the download button
resume_filename = "cv.pdf"


# Adjust the width ratios and add a spacer column between col1 and col2
col1, spacer, col2 = st.columns([1, 1, 4], gap="small")

with col1:
    st.image("pic.jpg", width=230)

with col2:
    st.title("Caryll Franz M. Cariño", anchor=False)
    st.write(
        "Aspiring Data Analyst | Recent Computer Engineering Graduate from Adamson University | Based in the Philippines"
    )

    st.write(
      "📧 caryllcarino@gmail.com"
    )
   
    st.download_button(
    label="Download Resume",
    data=pdf_bytes,
    file_name=resume_filename,
    mime="application/pdf"
)




    # if st.button("📩 Contact me"):
    #     show_contact_form()





st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" '
    'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" '
    'crossorigin="anonymous">',
    unsafe_allow_html=True
)

# #--SKILLS

# st.write("\n")

# st.subheader("Hard Skills", anchor=False)

# st.write(
#     """
#     - Technical skills: Excel, Sql, Figma, Cisco, MS Word, Tinkercad, Tableau, Power BI

#     - Programming and Development: Python, Javascript, HTML, CSS, Arduino (C++), XAML, PHP

#     - Specialized Tools and Libraries: Roboflow, Open CV, Pandas

#     """
# )

# # EXPERIENCES

# st.write("\n")

# st.subheader("Education", anchor=False)

# st.write(
#     """
#     **Adamson University**


#     - BS IN COMPUTER ENGINEERING Aug 2020 – July 2024


#     **Kings Montessori School**
#     - ABM  (ACCOUNTANCY, BUSINESS, AND MANAGEMENT) Aug 2018 – April 2020


#     """
# )

# st.write("\n")
# st.subheader("Experience", anchor=False)
# st.write(
#     """
#     **Technomancer**

#     - Web developer intern July 2023 – Aug 2023

#     - developed web applications with PHP, created CRUD functionalities, and gained experience with Laravel routing, while assisting with
#     front-end development.



#     """
# )


# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**BS Computer Engineering**, *Adamson University*, Philippines',
'2020-2024')
st.markdown('''
- GPA: `2.00`
- Research thesis entitled `SPOTSECURE:PARKING RESERVATION SYSTEM WITH PLATE NUMBER RECOGNITION THROUGH IMAGE PROCESSING`.
''')

txt('**ABM** (ACCOUNTANCY, BUSINESS, AND MANAGEMENT), *Kings Montessori School*, Philippines',
'2018-2020')
st.markdown('''
- GPA: `3.65`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Technomancer**', 'July 2023- Aug 2023')
st.markdown('''

- Developed web applications with PHP
- Created CRUD functionalities
- Gained experience with Laravel routing
- Assisted with front-end development
''')

########

st.markdown('''
## Projects
''')

# Use HTML to set the text color to red
st.markdown('**SPOTSECURE: PARKING RESERVATION SYSTEM WITH PLATE NUMBER RECOGNITION THROUGH IMAGE PROCESSING**', unsafe_allow_html=True)

st.markdown('`HTML, Flutter, CSS, SQLite, Python, YOLOv5, API, Arduino`')


st.markdown('''
A mobile app for parking reservations and a web app for admin users, displaying user details and vehicle plate numbers. Includes a Python script using AI for automatic plate recognition and database comparison. 
            The script interfaces with an Arduino to control pneumatic barriers when a match is detected or activates a buzzer if no match is found
''')

##2nd project

st.markdown('**YOLOv5-based Object Detection for AC, DC, and Battery Chargers**')

st.markdown('`Python, Google Collab, Roboflow`')


st.markdown('''
Developed an object detection system using YOLOv5 to accurately detect and classify AC power supplies, DC power supplies, and battery chargers in real-time images and videos

''')

##third project

st.markdown('**Designing a Scalable Network Topology for Region 2 in the Philippines Using EIGRP and VLSM**')

st.markdown('`Cisco`')


st.markdown('''
Developed a scalable and efficient network topology using Enhanced Interior Gateway Routing Protocol (EIGRP) and Variable Length Subnet Masking (VLSM) techniques for Region 2 in the Philippines

''')

##4th project
st.markdown('**Designing a Scalable Network Topology for Region 2 in the Philippines Using EIGRP and VLSM**')



st.markdown('[https://cert-caryll.vercel.app/](https://cert-caryll.vercel.app/)')

st.markdown('`Next.js, Hardhat`')
st.markdown('''
Developed a simple web app for generating meme coins, featuring locking and staking functionalities. Utilized Hardhat for smart contract development and deployment.
''')


#####################
st.markdown('''
## Skills
''')


# Replacing with your skills
txt3('Programming', '`Python`, `JavaScript`, `HTML`, `CSS`, `Arduino (C++)`, `XAML`, `PHP`')
txt3('Data processing/wrangling', '`Excel`, `SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `Power BI`, `Tableau`')
txt3('Machine Learning', '`YOLO`, `Roboflow`, `OpenCV`')
txt3('Web development', '`Bootstrap`, `HTML`, `CSS`, `PHP`')
txt3('Model deployment', '`streamlit`, `Vercel`')
txt3('Additional skills', '`Figma`, `MS Office`,`Cisco`')



#####################
st.markdown('''
## Social Media
''')



txt2('LinkedIn', 'https://www.linkedin.com/in/caryllfmc/')
txt2('GitHub', 'https://github.com/caryllfranz')
txt2('Facebook', 'https://www.facebook.com/seeshaboat/')
