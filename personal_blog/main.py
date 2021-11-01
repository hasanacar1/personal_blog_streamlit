import streamlit as st
from PIL import Image



st.set_page_config(
        page_title="Hasan Acar Blog",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded")

header = st.container()
dataset = st.container()
rf_bar = st.container()
c1 = st.sidebar
modelTraining = st.container()
interactive = st.container()
mapping = st.container()

with header:
    #image = Image.open("https://github.com/hasanacar1/personal_blog_streamlit/blob/main/personal_blog/road_7.png")
    #st.image(image,use_column_width=True)
    st.title("")

with c1:
     st.sidebar.title("Page Selection")
     selected_page = st.selectbox("Which page would you like to go to?", options=["Resume", "Telecommunication", "Data Science", "Map Visualization", "Computer Vision"])
     #st.sidebar.title("Operator Selection")
     #operator = st.selectbox("Which operator do you want to analyze ",options=["O2 (UK)","T-Mobile UK"])
     #st.sidebar.title("Period Selection")
     #period=st.sidebar.radio("Which period do you want to analyze", options=['PreTest','PostTest'])
     #st.sidebar.title("Technology Selection")
     #tech_data=st.sidebar.radio("Which type of tech do you want to analyze", options=['4G','4G/3G','3G', '2G'])
     #type_fail =st.sidebar.radio("Which type of test do you want to analize",options=['Data','Voice','Coverage'])

     #if type_fail == 'Data':
     #   st.sidebar.title("Data Test Types")
     #   type_data=st.sidebar.radio("Which type of data test do you want to analyze", options=["HTTP Browsing", "HTTP Transfer","Youtube"])
     #elif type_fail == 'Data':
     #   st.sidebar.title("Voice Test Types")
     #   st.sidebar.radio("Which type of voice test do you want to analyze", options=["CSFB", "CS","VOLTE"])
     #elif type_fail == 'Coverage':
     #   st.sidebar.title("Coverage Test Types")
     #   st.sidebar.radio("Which type of coverage test do you want to analyze", options=["Crowdsource"])



if selected_page == 'Resume':
    st.markdown("<h1 style='text-align: center; color: black; font-size:80px'>HASAN ACAR</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black; font-size:40px'>(Electronic and Communication Engineer)</h1>", unsafe_allow_html=True)
    st.title("")
    st.title("")
    col1, col2, col3, col4 = st.columns([2, 1, 4, 4])

    with col1:
        #st.title("Personal Info")
        st.markdown("<h1 style='color: DarkBlue; font-size:45px'>Personal Info</h1>", unsafe_allow_html=True)
        st.title("")
        st.info("Name : Hasan Acar")
        st.info("Phone : +90 543 426 78 00")
        st.info("E-mail : hsn144acar@gmail.com")
        st.info("Github : https://github.com/hasanacar1")
        st.info("LinkedIn : https://linkedin.com/in/hasan-acar-3563b1161")
    with col3:
         #st.title("Experience")
         st.markdown("<h1 style='color: DarkBlue; font-size:45px'>Experience</h1>", unsafe_allow_html=True)
         st.markdown("<h1 style='color: black; font-size:30px'>P.I. Works (15.02.2021 -  )</h1>", unsafe_allow_html=True)
         st.markdown("<h1 style='color: black; font-size:25px'>Telecommunication Specialist</h1>", unsafe_allow_html=True)
         st.text("My role within the company is to analyze and report data from drivetest logs or OSS. \n"
                  "During my work, I took part in Azercell Drivetest project, Mexico-TEF SSV project and\n"
                 " Pakistan-Jazz optimization project. I also had experience in developing web-based \n"
                 "analysis tool and reporting automation with python.")

         st.markdown("<h1 style='color: black; font-size:30px'>P.I. Works (04.08.2020 - 15.02.2021)</h1>", unsafe_allow_html=True)
         st.markdown("<h1 style='color: black; font-size:25px'>Telecommunication Intern</h1>", unsafe_allow_html=True)
         st.text("I had the opportunity to learn how 2G, 3G, 4G and 5G technologies work and the historical \n"
                 "development of these technologies. Secondly, I learned to analyze drivetest logs with \n"
                 "drivetest tools such as NQDI, Nemo Analyzer, Actix.In addition, I have experience in \n"
                 "database management with SQL.")

         st.markdown("<h1 style='color: black; font-size:30px'>Ambeent Wireless (10.06.2020 - 15.07.2020)</h1>", unsafe_allow_html=True)
         st.markdown("<h1 style='color: black; font-size:25px'>Telecommunication Intern</h1>", unsafe_allow_html=True)
         st.text("I developed a mobile application that determines the internet speed test considering \n"
                 "the Ookla speed test application,. Throughout this project, I also researched the \n"
                 "operations that take place in the OSI layers.")

    with col4:
        #st.title("Education")
        st.markdown("<h1 style='color: DarkBlue; font-size:45px'>Education</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:30px'>Istanbul Technical University (10.10.2020 -  )</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:25px'>Satellite Communication and Remote Sensing (Master Degree)</h1>", unsafe_allow_html=True)
        st.text("Continues...")
        st.title("")
        st.markdown("<h1 style='color: black; font-size:30px'>Istanbul Technical University  (10.09.2015 - 25.08.2020)</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:25px'>Electronic and Communication Engineering (Bachelor Degree)</h1>", unsafe_allow_html=True)
        st.text("During my university education, I have experience in MIMO antenna design with HFSS, \n"
             "data analysis and processing with machine learning methods, computer vision \n"
             "applications with artificial intelligence methods.In addition, I took useful courses \n"
             "such as signal processing, digital communication, mobile communication, \n"
             "electromagnetic waves, object-oriented programming. My Graduation Project is \n"
             "5G Mobility Management based on machine learning")

        st.title("")
        st.markdown("<h1 style= 'color: black; font-size:30px'>Kastamonu Science High School  (10.09.2011 - 15.06.2015)</h1>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([2, 1, 4, 4])
    with col1:
        st.title("")
    with col2:
        st.title("")
    with col3:
        st.title("")
    with col4:
        st.title("")

    col1, col2, col3, col4 = st.columns([2, 1, 4, 4])
    with col1:
        #st.title("Programming Skills")
        st.markdown("<h1 style='color: DarkBlue; font-size:45px'>Programming Skills</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:20px'>Python</h1>", unsafe_allow_html=True)
        my_bar = st.progress(90)
        st.markdown("<h1 style='color: black; font-size:20px'>SQL</h1>", unsafe_allow_html=True)
        my_bar_2 = st.progress(70)
        st.markdown("<h1 style='color: black; font-size:20px'>Java</h1>", unsafe_allow_html=True)
        my_bar_3 = st.progress(60)
        st.markdown("<h1 style='color: black; font-size:20px'>HTML,CSS,JavaScript</h1>", unsafe_allow_html=True)
        my_bar_4 = st.progress(50)
    with col3:
        st.markdown("<h1 style='color: DarkBlue; font-size:45px'>Projects</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:20px'>-Data preparation, processing and performance measurement with Python.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:20px'>-Object recognition with tensorflow library</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:20px'>-Network Planning Data Discrepancy Check Automation</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:20px'>-5G Handover Simulation with MATLAB</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:20px'>-Radio Access Network KPI Analysis and Reporting using Drive test tools and uSON PM tool</h1>", unsafe_allow_html=True)

    with col4:
        st.markdown("<h1 style='color: DarkBlue; font-size:45px'>Software Tools</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:25px'>Drive Test Log Analysis Tools</h1>", unsafe_allow_html=True)
        st.text("-Actix \n"
                "-Nemo Analyzer\n"
                "-NQDI")
        #st.markdown("<h1 style='color: black; font-size:20px'>-Actix</h1>", unsafe_allow_html=True)
        #st.markdown("<h1 style='color: black; font-size:20px'>-Nemo Analyzer</h1>", unsafe_allow_html=True)
        #st.markdown("<h1 style='color: black; font-size:20px'>-NQDI</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:25px'>Map Visualization Tools</h1>", unsafe_allow_html=True)
        st.text("-Mapinfo")
        #st.markdown("<h1 style='color: black; font-size:20px'>-Mapinfo</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: black; font-size:25px'>Microsoft Office Applications</h1>", unsafe_allow_html=True)
        st.text("-Microsoft Excel \n"
                "-Microsof Word\n"
                "-Microsot Powerpoint\n"
                "-Microsoft Power BI")
        #st.markdown("<h1 style='color: black; font-size:20px'>-Excel</h1>", unsafe_allow_html=True)
        #st.markdown("<h1 style='color: black; font-size:20px'>-Word</h1>", unsafe_allow_html=True)
        #st.markdown("<h1 style='color: black; font-size:20px'>-Powerpoint</h1>", unsafe_allow_html=True)
        #st.markdown("<h1 style='color: black; font-size:20px'>-Power BI</h1>", unsafe_allow_html=True)

elif selected_page == 'Telecommunication':
    st.title("telecommunications")

elif selected_page == 'Data Science':
    st.title("data_science")

elif selected_page == 'Map Visualization':
    st.title("map_visualization")

elif selected_page == 'Computer Vision':
    st.title("computer_vision")



