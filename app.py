import streamlit as st
from email_generator import generate_email,improve_email

st.set_page_config(
    page_title="Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Generator")
st.write("Generate or improve professional emails using AI")

# Email Types presets
email_types={
    "Custom": "",
    "Leave Request": "Requesting leave for few days dur to some reasons",
    "Job Application": "Applying for the position of Data Engineer",
    "Follow-up": "Following up on our previous meeting regarding project updates",
    "Apology": "Apologizing for missing the deadline"
}
preset = st.selectbox("Select Email Type",list(email_types.keys()))
if preset !="Custom":
    purpose=preset
    details=email_types[preset]
else:
    purpose=st.text_input("Email Purpose")
    details=st.text_area("Additional Details")

tone=st.selectbox("Select Tone",['Formal','Polite','Friendly','Professional'])
length=st.selectbox("Email Length",["Short","Medium","Detailed"])
temperature=st.slider("Creativity",min_value=0.0,max_value=1.0,value=0.7,step=0.05) # not soo necessary.

# Generate Email
if st.button("Generate Email🚀")and purpose and details:
    with st.spinner("Generating Email........."):
        email=generate_email(purpose,tone,details,length)
    st.success("Email generated successfully!")
    st.text_area("Generated email",email,height=300)

# improve exisitng enail
st.markdown("---")
st.subheader("Or improve exisitng email")
existing_email= st.text_area('Paste existing email to improve')

if st.button("Improve Email")and existing_email:
    with st.spinner("Improving email....."):
        improved=improve_email(existing_email,tone,temperature)
    st.success("Email improved successfully!")
    st.text_area("Improved Email",improved,height=300)



