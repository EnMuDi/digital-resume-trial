from pathlib import Path

import streamlit as st
from PIL import Image

# ------ PATH SETTINGS -------

current_dir = Path(__file__).parent if "__file" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"




# -------- GENERAL SETTINGS -----------

PAGE_TITLE = "Digital CV | Enes Mücahit Dikmen"
PAGE_ICON = ":wave:"
NAME = "Enes Mücahit Dikmen"
DESCRIPTION = """
Makine muhendisligine tutku ile bagliyim. Tasarim ve imalat alaninda tecrube kazanmak istiyorum. Disiplinli, gelisime acik ve uyumlu bir insanim 
"""
EMAIL = "dikmenenesmucahit@gmail.com"
SOCIAL_MEDIA = { "Youtube" : "https://www.youtube.com/channel/UCnU6sanzGLyzvL_lWmBdcag",
                 "LinkedIn" : "https://www.linkedin.com/in/enes-m%C3%BCcahit-dikmen-08a943179/",
                 "GitHub" : "https://github.com/EnMuDi"                


}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

# ------ LOAD CSS, PDF & PROFIL PIC -------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# ------- HERO SECTION ---------

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= "Download Resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"

    )
    st.write("@", EMAIL)



# ------ SOCIAL LINKS --------

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# -------- EXPERIENCE & QUALIFICATIONS -------
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- AutoCAD
- Solidworks
- Fusion360
- MS Office  
    """
)

# ------- SKILLS ------
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- AutoCAD
- Solidworks
- Fusion360
- MS Office  
    """
)


# ----- WORK HISTORY -------
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("**Office Worker | Anadolu University**")
st.write("07/2021 - 10/2021")
st.write(
    """
- Bilgisayara veri girişi yaptım. 
    """
)

 # --- JOB 2
st.write("**Intern Mechanical Engineer | MKS Celik**")
st.write("06/2022 - 08/2022")
st.write(
    """
- Talaşlı ve talaşsız imalat stajlarımı tamamladım. 
    """
)

# --- JOB 3
st.write("**Intern Mechanical Engineer | Peyman AS**")
st.write("08/2021 - 09/2021")
st.write(
    """
- İşletme ve organizasyon stajımı tamamladım. 
    """
)

# ------ EXAMS -------
# ------- SKILLS ------
st.write("#")
st.subheader("Exams")
st.write(
    """
- Yökdil | 90
- YDS | 85     
    """
)