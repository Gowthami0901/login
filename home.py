import streamlit as st

def main():
    st.title("Home Page")

    if "message" in st.session_state and st.session_state.message:
        st.success(st.session_state.message)
        st.session_state.message = ""

    st.write("Welcome to the home page!")
    

    st.header("Job Opportunities")
    st.write("""
             Explore exciting job opportunities and advance your career with the latest job listings:
    """)

    st.subheader("Featured Jobs")
    st.write("""
    - **Software Engineer at Tech Innovators**  
      Location: San Francisco, CA  
      Description: Join a leading tech company as a software engineer and work on cutting-edge projects. Experience with Python and JavaScript required. [Apply Now](#)

    - **Marketing Manager at Growth Corp**  
      Location: New York
      Description: Lead marketing campaigns and drive growth for an innovative startup. Proven track record in digital marketing is a plus. [Apply Now](#)

    - **Product Designer at Creative Solutions**  
      Location: Remote  
      Description: Design user-friendly products and interfaces for a global audience. Strong portfolio in UX/UI design required. [Apply Now](#)
    """)

    st.subheader("Career Tips")
    st.write("""
    Enhance your career with these essential tips:
    1. Network regularly and build connections.
    2. Keep your resume and LinkedIn profile updated.
    3. Seek feedback and continuously improve your skills.
    4. Stay informed about industry trends and job market changes.
    5. Prepare thoroughly for interviews and practice common questions.
    """)

    st.subheader("Industry News")
    st.write("""
    Stay up-to-date with the latest news and trends in your industry:
    - **Tech Giants Investing in AI**: Major technology companies are increasing their investments in artificial intelligence. [Read More](#)
    - **Remote Work Trends**: The rise of remote work is reshaping the job market. 
    - **Top Skills for 2024**: Discover the most sought-after skills for the upcoming year. 
    """)

    # Uncomment the following lines if you want to include a logout button
    # if st.button("Logout"):
    #     st.session_state.login_state = False
    #     st.session_state.login_successful = False
    #     st.session_state.message = ""
    #     st.session_state.login_inputs = {"email": "", "password": ""}
    #     st.experimental_rerun()

if __name__ == "__main__":
    main()
