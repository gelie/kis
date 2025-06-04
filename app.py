
import streamlit as st

# Set the title of the app
st.title("KIS Report Registry System")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Upload Form", "Document Repository", "Reporting Module", "Help/Support"])

# Dashboard page
if page == "Dashboard":
    st.header("Dashboard")
    st.write("Overview of total reports received, reports received per department, reports pending, and submission trends.")

# Upload Form page
elif page == "Upload Form":
    st.header("Upload Form")
    st.write("Form to upload new reports.")
    report_type = st.selectbox("Type", ["Letter", "Paper", "Report"])
    title = st.text_input("Title/Description")
    date_tabled = st.date_input("Date Tabled")
    department = st.text_input("Department/Ministry")
    uploaded_file = st.file_uploader("Upload File", type=["pdf", "docx"])
    if st.button("Submit"):
        st.success("Report submitted successfully!")

# Document Repository page
elif page == "Document Repository":
    st.header("Document Repository")
    st.write("Searchable and filterable list of all submissions.")
    search_term = st.text_input("Search")
    filter_date = st.date_input("Filter by Date")
    filter_department = st.text_input("Filter by Department")
    if st.button("Search"):
        st.write("Displaying search results...")

# Reporting Module page
elif page == "Reporting Module":
    st.header("Reporting Module")
    st.write("Generate reports by time period, department, and type of document.")
    report_period = st.selectbox("Time Period", ["Weekly", "Monthly", "Quarterly"])
    report_department = st.text_input("Department")
    report_type = st.selectbox("Type", ["Letter", "Paper", "Report"])
    if st.button("Generate Report"):
        st.write("Displaying generated report...")

# Help/Support page
elif page == "Help/Support":
    st.header("Help/Support")
    st.write("Help section with training materials and contact support form.")
    st.write("For assistance, please contact support@example.com.")
