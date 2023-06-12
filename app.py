import streamlit as st
from pytube import YouTube
import os
from pathlib import Path

st.set_page_config(
    page_title="My App",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply CSS styling
background_color = "#03002e"
text_color = "white"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {text_color};
        color: {background_color};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("You Tube Videos Downloader App")
st.subheader("ABOUT ME :")
st.write(" Hi guys my name is Ayoub and this is my Website were you can download youtube videos for free  ")

# Create a text 
name = st.text_input("Enter the URL", value="", help="Enter the URL")
Video_URL = name

# Create a button 
button_clicked = st.checkbox("Download")
if button_clicked:
        
    try:
        # Extract the video ID from the URL
        video_id = YouTube(Video_URL).video_id
        video = YouTube(Video_URL)

        # Generate the YouTube Embed HTML code
        embed_code = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'

        # Display the embedded YouTube video
        st.markdown(embed_code, unsafe_allow_html=True)
        # Get the available video qualities
        available_qualities = [stream.resolution for stream in video.streams.filter(progressive=True).order_by("resolution")]
        
        # Create a dropdown menu for quality selection
        selected_quality = st.selectbox("Select video quality", available_qualities)
        # Function to download the video
        def download_video():

            video = YouTube(Video_URL)

            stream = video.streams.filter(progressive=True, resolution=selected_quality).first()

            # Set the download path to the Downloads folder on Windows
            path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

            # Download the video to the specified path
            stream.download(output_path=path_to_download_folder)
            

            # Display success message
            st.success("Video downloaded successfully!")

        # Create a button to trigger the download
        if st.button("Download Video"):
            download_video()
       
        
       
    except:
        st.write("Invalid YouTube video URL")


