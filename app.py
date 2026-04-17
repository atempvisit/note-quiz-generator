import streamlit as st
from api_calling import audio_transcription, note_generator, quiz_generator
from PIL import Image


st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Notes Summary and Quizzes")
st.divider()


with st.sidebar:

    #image

    images =st.file_uploader(
        "Upload your note photos here",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    pil_images = [Image.open(image) for image in images]


    if images:
        if len(images) > 3:
            st.warning("Please upload a maximum of 3 images.")
        else:
            st.subheader("Uploaded Images")

            col = st.columns(len(images))

            for i, image in enumerate(images):
                with col[i]:
                    st.image(image, caption=f"Image {i+1}")
    
    # difficulty
    selected_difficulty = st.selectbox(
        "Select Quiz Difficulty",
        ("Easy", "Medium", "Hard"),
        index=None
    )

    button = st.button("Generate", type="primary")

if button:
    if not images:
        st.error("Please upload at least one image to generate the summary and quiz.")
    if not selected_difficulty:
        st.error("Please select a quiz difficulty level.")
    
    if images and selected_difficulty:

        # note summary

        with st.container(border=True):
            st.subheader("Notes Summary")

            with st.spinner("Generating notes summary..."):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)
            
        # audio transcript
        with st.container(border=True):
            st.subheader("Audio Transcript")

            with st.spinner("Generating audio transcript..."):
                generated_audio = audio_transcription(generated_notes) 
                st.audio(generated_audio, format="audio/mp3")


        # quiz generator
        with st.container(border=True):
            st.subheader(f"Quiz Difficulty: {selected_difficulty}")

            with st.spinner("Generating quizzes..."):
                generated_quiz = quiz_generator(pil_images, selected_difficulty)
                st.markdown(generated_quiz)