import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="EcoSortAI",
    page_icon="♻️",
    layout="wide"
)

# -----------------------
# LOAD API
# -----------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------
# CSS
# -----------------------

st.markdown("""
<style>

.stApp{
    background:#05070d;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0b0f17;
    border-right:1px solid #00ff88;
}

/* Title */
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:#00ff88;
    text-shadow:0px 0px 20px #00ff88;
}

.sub-title{
    text-align:center;
    color:white;
    font-size:20px;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:#00ff88;
    color:black;
    border:none;
    border-radius:12px;
    font-weight:bold;
    box-shadow:0 0 15px #00ff88;
}

/* Inputs */
.stTextInput input{
    background:#111827;
    color:white;
    border:1px solid #00ff88;
}

/* Upload box */
[data-testid="stFileUploader"]{
    border:1px solid #00ff88;
    border-radius:12px;
    background:#111827;
}

/* Tabs */
.stTabs [data-baseweb="tab"]{
    background:#111827;
    color:white;
    border-radius:10px;
}

.stTabs [aria-selected="true"]{
    background:#00ff88 !important;
    color:black !important;
}

/* Result card */
.result-card{
    background:#0f172a;
    border:1px solid #00ff88;
    border-radius:15px;
    padding:20px;
    color:white;
    box-shadow:0 0 20px rgba(0,255,136,0.3);
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# SIDEBAR
# -----------------------

with st.sidebar:
    st.title("♻️ EcoSortAI")
    st.markdown("---")
    st.write(" Text Analysis")
    st.write(" Image Upload")
    st.write(" Camera Scan")
    st.write("🌱 Sustainability")

# -----------------------
# HEADER
# -----------------------

st.markdown("""
<div class="main-title">
♻️ EcoSortAI
</div>

<div class="sub-title">
Smart AI Waste Segregation & Sustainability Assistant
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------
# ANALYSIS FUNCTION
# -----------------------

def analyze_content(content):

    prompt = """
You are a Waste Management Expert.

Analyze the waste item.

Return EXACTLY in this format:

Object Name:
Waste Category:
Recyclable:
Disposal Method:
Environmental Impact:
Sustainability Tip:

Keep every field on a separate line.
Do not write paragraphs.
"""

    response = model.generate_content(
        [prompt, content]
    )

    return response.text

# -----------------------
# TABS
# -----------------------

tab1, tab2, tab3 = st.tabs(
    [
        " Text Analysis",
        " Image Upload",
        " Camera Scan"
    ]
)

# -----------------------
# TEXT ANALYSIS
# -----------------------

with tab1:

    st.subheader("Analyze Waste Using Text")

    waste_item = st.text_input(
        "Enter Waste Item"
    )

    if st.button("Analyze Text"):

        if waste_item.strip():

            try:

                result = analyze_content(
                    waste_item
                )

                st.markdown(
                    f"""
                    <div class='result-card'>
                    <pre>{result}</pre>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.warning(
                    f"Error: {e}"
                )

# -----------------------
# IMAGE UPLOAD
# -----------------------

with tab2:

    st.subheader("Upload Waste Image")

    uploaded_file = st.file_uploader(
        "Choose Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        image = Image.open(
            uploaded_file
        )

        col1,col2,col3 = st.columns([1,2,1])
        with col2:
            st.image(
                image,
                width=300
            )

        if st.button(
            "Analyze Uploaded Image"
        ):

            try:

                result = analyze_content(
                    image
                )

                st.markdown(
                    f"""
                    <div class='result-card'>
                    <pre>{result}</pre>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.warning(
                    f"Error: {e}"
                )

# -----------------------
# CAMERA SCAN
# -----------------------

with tab3:

    st.subheader("Camera Waste Scanner")

    camera_image = st.camera_input(
        "Capture Waste Image"
    )

    if camera_image:

        image = Image.open(
            camera_image
        )

        col1,col2,col3 = st.columns(
            [1,2,1]
        )

        with col2:
            st.image(
                image,
                width=300
            )

        if st.button(
            "Analyze Camera Image"
        ):

            try:

                result = analyze_content(
                    image
                )

                st.markdown(
                    f"""
                    <div class='result-card'>
                    <pre>{result}</pre>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.warning(
                    f"Error: {e}"
                )

# -----------------------
# FOOTER
# -----------------------

st.markdown("---")

st.markdown("""
<div class='result-card'>

### 🌱 About EcoSortAI

EcoSortAI is an AI-powered waste segregation system that helps users:

✅ Identify waste items

✅ Classify waste categories

✅ Recommend disposal methods

✅ Promote sustainable waste management

Powered by Gemini AI + Streamlit
Developed by Saurav Kumar Rana...

</div>
""", unsafe_allow_html=True)

