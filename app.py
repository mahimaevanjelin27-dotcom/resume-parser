import streamlit as st

from extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education,
    extract_experience
)

# Page configuration
st.set_page_config(
    page_title="AI Resume Parser",
    page_icon="📄",
    layout="wide"
)


# Title
st.title("📄 AI Resume Parser")

st.write(
    "Upload a resume and extract important information automatically."
)


# Upload resume
uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["txt"]
)


# Process uploaded file
if uploaded_file is not None:

    # Read the uploaded file
    resume_text = uploaded_file.read().decode(
        "utf-8",
        errors="ignore"
    )


    # Extract information
    name = extract_name(resume_text)

    email = extract_email(resume_text)

    phone = extract_phone(resume_text)

    skills = extract_skills(resume_text)

    education = extract_education(resume_text)

    experience = extract_experience(resume_text)


    # Display results
    st.success("Resume processed successfully!")


    st.subheader("👤 Personal Information")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.write("**Name**")

        st.write(name)


    with col2:

        st.write("**Email**")

        st.write(email)


    with col3:

        st.write("**Phone**")

        st.write(phone)


    # Skills
    st.subheader("🛠️ Skills")

    if skills:

        st.write(", ".join(skills))

    else:

        st.write("No skills found")


    # Education
    st.subheader("🎓 Education")

    if education:

        for item in education:

            st.write("•", item)

    else:

        st.write("No education information found")


    # Experience
    st.subheader("💼 Experience")

    if experience:

        for item in experience:

            st.write("•", item)

    else:

        st.write("No experience information found")


    # Display resume text
    with st.expander("📃 View Resume Text"):

        st.text(resume_text)