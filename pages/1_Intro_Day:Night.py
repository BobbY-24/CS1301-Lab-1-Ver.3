import streamlit as st
import info
import pandas as pd


st.set_page_config(layout = 'wide')
st.title("👤 Portfolio")

night_mode = st.toggle("Night", value = False)

if night_mode:
    st.markdown("""<style> body{background-color: #121212; color: #f5f5f5;} . st-emotion-cache-1avcm0n{ background-color: #1e1e1e;} </style> """, unsafe_allow_html=True)
else: st.markdown(""" <style> body{ background-color: #ffffff; color: #000000;} </style> """, unsafe_allow_html = True)


#DAYBOB

info.profile_picture_night = "images/profile.jpeg"

                       
def about_me_section():
    
    st.header('About Me')
    st.image("images/profile_day.jpg", width = 200)
   
    st.write(info.about_me)
    st.write("---")




def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link =  f'<a href="{info.my_linkedin_url}"><img src= "{info.linkedin_image_url}" alt = "LinkedIn" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt = "Github" width = "65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="malito:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width = "75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f'**Degree:**{education_data["Degree"]}')
    st.write(f'**Graduation Date:**{education_data["Graduation Date"]}')
    st.write(f'**GPA:**{education_data["GPA"]}')
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I learned"},
        hide_index = True 
                 )
    st.write("---")
    
    


def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image)in experience_data.items():
        expander = st.expander(f'{job_title}')
        expander.image(image, width = 250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

def project_section(projects_data):
    st.header("Project")
    for project_name, project_description in projects_data.items():
        expander= st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
    


def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill)} = {percentage}%")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken)}:{proficiency}")
    st.write('---')

def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("leadership")
        for title,(detail, image) in leadership_data.items():
            expander= st.expander(f"{title}")
            
            for bullet in detail:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)



#NIGHTBOB
def about_me_section_night():
    
    st.header('About Me')
    st.image(info.profile_picture_night, width = 200)
   
    st.write(info.about_me_night)
    st.write("---")




def links_section_night():
    st.sidebar.header("BATCAVE")
    st.sidebar.text("Welcome to Gotham")
    linkedin_link =  f'<a href="{info.bat_cave}"><img src= "{info.linkedin_image_url}" alt = "BATCAVE" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)



    
#CTRL


if night_mode:
    st.markdown("""<style>body {background-color: black;color: white;}.stApp {background-color: black;color: white;}h1, h2, h3, h4, h5, h6, p, div {color: white;}.stTextInput, .stSelectbox, .stButton { background-color: #333;color: white;}</style>""",unsafe_allow_html=True)
    about_me_section_night()
    links_section_night()
    education_section(info.education_data_night, info.course_data_night)
    experience_section(info.experience_data_night)
    project_section(info.projects_data_night)
    skills_section(info.programming_data_night, info.spoken_data_night)

else:
    st.markdown(""" <style> body{ background-color: #ffffff; color: #000000;} </style> """, unsafe_allow_html = True)
    about_me_section()
    links_section()
    education_section(info.education_data, info.course_data)
    experience_section(info.experience_data)
    project_section(info.projects_data)
    skills_section(info.programming_data, info.spoken_data)
    activities_section(info.leadership_data, info.activity_data)
    
    
    
    

    




    
