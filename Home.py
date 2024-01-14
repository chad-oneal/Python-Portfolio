import pandas as pd
import streamlit as st
from PIL import Image
import functions

# Streamlit layout
st.set_page_config(layout='wide')

# Create placeholders for each column
col1, col2 = st.columns([1, 1])

# Content for column 1
with col1:
    circular_image_centered = functions.make_circle_in_column('images/photo.png',
                                                              circle_size=(250, 250),
                                                              canvas_width_multiplier=3)
    st.image(circular_image_centered, use_column_width=True)
    functions.add_space(1)

# Content for column 2
with col2:
    functions.add_space(3)
    st.title('Chad ONeal')
    content = """
    As a dedicated Software Quality Assurance Engineer at RegScale,
    my primary focus is on manual testing and the meticulous development
    of comprehensive test cases. I take pride in my contribution to the
    software testing process, having crafted over 1000 test cases to date,
    all systematically documented in TestRail.

    Beyond manual testing, my role involves a collaborative effort with
    our Principal SDET and Senior SDET, where I am gaining valuable 
    experience in automated testing. Utilizing Python, I assist in the
    testing of both the RegScale web application and its APIs, a task that
    not only bolsters our product reliability but also enables me to
    expand my technical acumen in software testing.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)
st.markdown("""---""")

# Rows 3 & 4
df = pd.read_csv('data.csv', sep=';')

standard_size = (550, 300)  # Define a standard size for all images

col3, _, col4 = st.columns([1.3, 0.3, 1.55])  # Unseen column for spacing

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        functions.add_space(3)

        image_path = 'images/' + row['image']
        img = Image.open(image_path)
        img = img.resize(standard_size)
        img.save("temp_img.png")
        img_base64 = functions.get_image_base64("temp_img.png")

        st.markdown(f'<img src="data:image/png;base64,{img_base64}"'
                    f' style="max-width: 90%; height: auto;">',
                    unsafe_allow_html=True)

        functions.add_space(4)
        st.write(f"[SourceCode]({row['url']})")
        st.markdown("""---""")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        functions.add_space(3)

        image_path = 'images/' + row['image']
        img = Image.open(image_path)
        img = img.resize(standard_size)
        img.save("temp_img.png")
        img_base64 = functions.get_image_base64("temp_img.png")

        # Display the image using Markdown with right alignment
        st.markdown(f'<img src="data:image/png;base64,{img_base64}"'
                    f' style="max-width: 90%; height: auto; margin-left: 10%;">',
                    unsafe_allow_html=True)

        functions.add_space(4)
        st.write(f"[SourceCode]({row['url']})")
        st.markdown("""---""")