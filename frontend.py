import streamlit as st
from complaint_bot import generate_complaint_report  

st.set_page_config(page_title="Complaint Report Generator", page_icon="C:/Users/arije/Desktop/Cuba Buddy Complaint Bot/Logo.png", layout="centered")

st.image("C:/Users/arije/Desktop/Cuba Buddy Complaint Bot/Logo.png", width=150)

st.markdown("<h1 style='text-align: center; color: black;'>Complaint Report Generator</h1>", unsafe_allow_html=True)

st.markdown("**Generate detailed complaint reports by entering the Deal ID and the subject of the complaint.**", unsafe_allow_html=True)

deal_id = st.text_input("Enter Deal ID")
complaint_subject = st.text_area("Enter Subject of Complaint")

if st.button("Generate Report"):
    if deal_id and complaint_subject:
        report = generate_complaint_report(deal_id, complaint_subject)
        if "Error" not in report:
            st.success("**Report generated successfully!**", icon="✅")
            st.download_button(
                label="Download Report",
                data=report,
                file_name="complaint_report.txt",
                mime="text/plain"
            )
        else:
            st.error(report)
    else:
        st.error("Please enter both the Deal ID and the subject of the complaint.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    h1, .stMarkdown, .stTextInput label, .stTextArea label {
        color: black;
    }
    .stButton button {
        color: white;
        background-color: #4CAF50;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
    .stAlert {
        font-weight: bold;
        color: black;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
