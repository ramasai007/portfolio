import streamlit as st
from PIL import Image
st.title("RAMA SAI   KURETI")

col1,col2=st.columns(2)

with col1:
    img_path='./my_image.jpg'
    img=Image.open(img_path)
    st.image(img)
with col2:
    st.write('Linkedin:  www.linkedin.com/in/rama-sai-kureti-b36a41253')
    st.write('GitHub : https://github.com/explore')
    st.write('Discord: sairam#7781')
    st.write('Email: ramasaikureti@gmail.com')
    tab1,tab2,tab3,tab20,tab4=st.tabs(['My Info','Qualification','Projects','Skills','Hobbies'])
    with tab1:
        st.title('Hello')
        st.write('''I am an ever-evolving work of art,
                    Shaped by experiences that left their mark,
                    A reflection of the world around me,
                    And all the lessons it has set free.''')
    with tab2:
        genre = st.radio("MY Qualifications",
                        ('SSC','Intermediate','Graduation'))
        if genre == 'SSC':
            st.write('School: S R S M High School')
            st.write('GPA: 9.0')
        elif genre == 'Intermediate':
            st.write('College: Sree Chaitanya Junior College')
            st.write('Group: MPC')
            st.write('GPA: 8.5')
        elif genre=='Graduation':
            st.write('college: Krishnaveni Degree College')
            st.write('Statistics') 
            st.write('GPA: 7.2')
        else:
            st.write('Select anything')

    with tab3:
        tab1, tab2, tab3, tab19=st.tabs(["Python","EDA","SQL","Tableau"])

        with tab1:
            st.header("Transformer model for SMS spam detection")
            tab9, tab10, tab11 = st.tabs(["Programming Language", "Algorithms Used", "Overview"])

            with tab9:
                st.write("Python")
            
            with tab10:
                st.write("SMS")
                st.write("Decision Tree")
                st.write("Logistic Regression")

            with tab11:
                st.write("Used csv formatted data to train the ML algorithms and used those algorithms to predict whether the given sms is spam or not")
        
        with tab2:
            st.header("Analysis on top 400 youtube channels")
            tab5, tab6, tab7 = st.tabs(["Platform used", "Libraries used", "Overview"])

            
            with tab5:
                st.write("Jupyter Notebook")
            
            with tab6:
                st.write("pandas")
                st.write("numpy")
                st.write("seaborn")
                st.write("Regular Expression")
                st.write("Beautiful Soup")
            
            with tab7:
                st.write("Web scraped data of fifa world cup players  to know the gross of player as per the categories of those Teams")

        with tab3:
            st.header("Library Management ")
            tab12, tab13, tab14 =st.tabs(["DBMS", "Commands", "Overview"])

            with tab12:
                st.write("MySQL")

            with tab13:
                st.write("Select")
                st.write("Update")
                st.write("Join")
                st.write("Delete")
                st.write("Rollback..etc")

            with tab14:
                st.write("By using MySQL joined various tables containg library information then used that RDBMS to solve queries")

        with tab19:
            st.header("Zomato")
            image=Image.open('./tab.jpg')
            st.image(image)
    
    with tab4:
        st.write('Editing video/photographs')
        st.write('Reading Books')
        st.write('Exploring my self')

    with tab20:
        st.write("Skill matrix:")
        st.slider("Python",1,10,(9))
        st.slider("MySQL",1,10,(8))
        st.slider("Tableau",1,10,(9))
