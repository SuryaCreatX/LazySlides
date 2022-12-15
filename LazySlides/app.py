import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
import io
from PIL import Image 
import time
import os
import base64
import requests
from streamlit_lottie import st_lottie

#from text import text2s
#from imagesalone import img2s
#from video2s import v2s
#from audio import audios

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

hidemenu = """
<style>
#MainMenu {
	visibility:hidden;
}
footer{
	visibility:visible;
}
footer:after{
	content:'Copyright © 2022 : GenZerrorZ';
	display:block;
	postion:relative;
	color:DarkGrey;
}
<style>
"""

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 



def main():
	im = Image.open("icon.png")
	st.set_page_config(
        page_title="LazySlides",
        page_icon=im,
        layout="wide",
    )

	st.markdown(hidemenu,unsafe_allow_html=True)

	st.title("LazySlides")
	add_bg_from_local('bgf.jpg')
	


	menu = ["Home","Video","Image","Audio","Document Files","Youtube","About"]
	choice = st.sidebar.selectbox("Browse Options",menu)
	st.sidebar.write("")
	st.sidebar.write("")
	st.sidebar.write("")
		
	ans = st.sidebar.select_slider('How are you feeling today ?',options=['Happy', 'Sad', 'Tired', 'Angry','Surprised','Excited'])
	if ans == 'Happy':
		st.sidebar.write("You are more fun than anyone or anything I know, including bubble wrap")
	if ans == 'Sad':
		st.sidebar.write("I know it's hard to see this right now, but it's only temporary…")
	if ans == 'Tired':
		st.sidebar.write("It's OK to take a break! ...")
	if ans == 'Angry':
		st.sidebar.write("Is it ridiculously cold right now?... I'd better get some coffee")
	if ans == 'Surprised':
		st.sidebar.write("Are you serious? Is this for real? Damn!!! Have a great day.")
	if ans == 'Excited':
		st.sidebar.write("That's wonderful!!! I'm so happy for you!")

	if choice == "Home":
		st.write("Just as simple as drag, drop, upload and convert. Easy to convert and download your file formats in PPT and PDF.")
		st.write("Start converting today!! ")
		st.write("")
		
		with st.container():
			image_column, text_column = st.columns((1, 2))
		with image_column:
			video = Image.open('vid.png')
			st.image(video)
		with text_column:
			st.subheader("VIDEO")
			st.write("Convert your mp4 format videos into PPT")

		with st.container():
			image_column, text_column = st.columns((1, 2))
		with image_column:
			ima = Image.open('img.png')
			st.image(ima)
		with text_column:
			st.subheader("IMAGES")
			st.write("Convert your jpeg, jpg and png format images to PPT")
		
		with st.container():
			image_column, text_column = st.columns((1, 2))
		with image_column:
			audio = Image.open('aud.png')
			st.image(audio)
		with text_column:
			st.subheader("AUDIO")
			st.write("Convert your mp3 format audio files to PPT")

		with st.container():
			image_column, text_column = st.columns((1, 2))
		with image_column:
			text = Image.open('doc.png')
			st.image(text)
		with text_column:
			st.subheader("DOCUMENT FILES")
			st.write("Convert your docx, txt, pdf format document files to PPT")

		with st.container():
			image_column, text_column = st.columns((1, 2))
		with image_column:
			you = Image.open('yt.png')
			st.image(you)
		with text_column:
			st.subheader("YOUTUBE VIDEOS")
			st.write("Convert your youtube video links to PPT")		



	elif choice == "Audio":
		st.subheader("Convert your Audio")
		uploaded_file = st.file_uploader("Upload Audio file ",type=['mp3'],help="Upload image format mp3")
		if st.button("Process"):
			if uploaded_file is not None:
				audio_bytes = uploaded_file.read()
				st.audio(audio_bytes,format='audio/mp3')

				with open(os.path.join("audio",uploaded_file.name),"wb") as f: 
					f.write(uploaded_file.getbuffer())         
				st.success("Saved File")

				#paul here
				audio2s

				with st.spinner('Wait for it...'):
					time.sleep(5)
				my_bar = st.progress(0)
				for percent_complete in range(100):
					time.sleep(0.1)
					my_bar.progress(percent_complete + 1)
				
				col1, col2 = st.columns([1,1])
				with col1:
					if st.button("Download as PPT"):
						st.header("...")
				with col2:
					if st.button("Download as PDF"):
						st.header("...")
    				
		
	
	elif choice == "Video":
		st.subheader("Convert your Video")
		uploaded_file = st.file_uploader("Upload Video file ",type=['mp4'],help="Upload video format mp4")
		if st.button("Process"):
			if uploaded_file is not None:
				video_bytes = uploaded_file.read()
				st.video(video_bytes,format='video/mp4')
				
				with open(os.path.join("video",uploaded_file.name),"wb") as f: 
					f.write(uploaded_file.getbuffer())         
				st.success("Saved File")

				#paul here
				v2s("")
				
				with st.spinner('Wait for it...'):
					time.sleep(5)
				
				my_bar = st.progress(0)
				for percent_complete in range(100):
					time.sleep(0.1)
					my_bar.progress(percent_complete + 1)

				col1, col2 = st.columns([1,1])
				with col1:
					if st.button("Download as PPT"):
						st.header("...")
				with col2:
					if st.button("Download as PDF"):
						st.header("...")
		
			

	elif choice == "Image":
		st.subheader("Convert your Image")
		uploaded_files = st.file_uploader("Upload Image ",type=['jpg','jpeg','png'],help="Upload image format jpg,jpeg,png", accept_multiple_files=True,)
		if st.button("Process"):
			
			for uploaded_file in uploaded_files:
				
				bytes_data = uploaded_file.read()
				image = Image.open(io.BytesIO(bytes_data))
				#st.write("filename:", uploaded_file.name)
				st.image(image)
					
			with open(os.path.join("images",uploaded_file.name),"wb") as f: 
				f.write(uploaded_file.getbuffer())         
			st.success("Saved File")

			#paul here
		
			img2s("")
				
			with st.spinner('Wait for it...'):
				time.sleep(5)
				
			my_bar = st.progress(0)
			for percent_complete in range(100):
				time.sleep(0.1)
				my_bar.progress(percent_complete + 1)

			col1, col2 = st.columns([1,1])
			with col1:
				if st.button("Download as PPT"):
					st.header("...")
			with col2:
				if st.button("Download as PDF"):
					st.header("...")

	
	elif choice == "Document Files":
		st.subheader("Convert your DocumentFiles")
		docx_file = st.file_uploader("Upload File ",type=['txt','docx','pdf'],help="Upload image format jpg,jpeg,png")
		if st.button("Process"):
			if docx_file is not None:
				
				if docx_file.type == "text/plain":
					with open(os.path.join("textfile",docx_file.name),"wb") as f:
						f.write(docx_file.getbuffer())         
					st.success("Saved File")

					text2s("")
					
								
				elif docx_file.type == "application/pdf":
					with open(os.path.join("docf",docx_file.name),"wb") as f:
						f.write(docx_file.getbuffer())         
					st.success("Saved File")
					


				elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
					with open(os.path.join("docf",docx_file.name),"wb") as f:
						f.write(docx_file.getbuffer())         
					st.success("Saved File")
				
			
					
			with st.spinner('Wait for it...'):
				time.sleep(5)
					
			my_bar = st.progress(0)
			for percent_complete in range(100):
				time.sleep(0.01)
				my_bar.progress(percent_complete + 1)

			col1, col2 = st.columns([1,1])
			with col1:
				if st.button("Download as PPT"):
					st.header("...")
			with col2:
				if st.button("Download as PDF"):
					st.header("...")
	

	elif choice == "Youtube":
		st.subheader("Convert your Youtube Video")
		link = st.text_input('Enter your YouTube video link')
		if st.button("Process"):
			st.video(link)
				
			with open(os.path.join("videof",uploaded_file.name),"wb") as f: 
				f.write(uploaded_file.getbuffer())         
			st.success("Saved File")

			#paul here
				
			with st.spinner('Wait for it...'):
				time.sleep(5)
				
			my_bar = st.progress(0)
			for percent_complete in range(100):
				time.sleep(0.1)
				my_bar.progress(percent_complete + 1)

			col1, col2 = st.columns([1,1])
			with col1:
				if st.button("Download as PPT"):
					st.header("...")
			with col2:
				if st.button("Download as PDF"):
					st.header("...")
			
			

	else:
		with st.container():
			text_column, image_column = st.columns((2, 1))
		with text_column:
			st.subheader("About Us :wave:")
			st.info("Team GenZerrorZ")
			st.write("Developers --> Surya · Kalai · Paul · Dharshini")
			st.write("Mentor & Idea --> Navneeth Mahalingam")
			st.write("Developed Using Streamlit @2022")
		with image_column:
			st_lottie(lottie_coding, height=200, key="coding")

				
		local_css("style.css")

		with st.container():
			st.write("---")
			st.header("Get In Touch With Me!")
			st.write("##")

			# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
			contact_form = """
			<form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
				<input type="hidden" name="_captcha" value="false">
				<input type="text" name="name" placeholder="Your name" required>
				<input type="email" name="email" placeholder="Your email" required>
				<textarea name="message" placeholder="Your message here" required></textarea>
				<button type="submit">Send</button>
			</form>
			"""
			left_column, right_column = st.columns(2)
			with left_column:
				st.markdown(contact_form, unsafe_allow_html=True)
			with right_column:
				st.empty()

		


if __name__ == '__main__':
	main()