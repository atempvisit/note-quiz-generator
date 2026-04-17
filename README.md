# Note & Quiz Generator Application

This is a simple note and quiz generator application built using Streamlit and the Google Gemini API. The application allows users to upload images, generates notes based on the content of the images, transcribes audio from the generated notes, and creates quizzes based on the notes with selectable difficulty levels.

## Installation

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application

To run the project, follow these steps:
1. Clone the repository to your local machine.
2. Create a `.env` file in the root directory of the project and add your Gemini API key in the following format:
```
GEMINI_API_KEY="your_api_key_here"
```
3. Install the required packages using pip.
4. Run the Streamlit application using the command:
```
streamlit run {filename}.py
```