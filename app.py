
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
def main():
    st.set_page_config(page_title="Sentiment_protyush", page_icon= ":computer")
    st.title("Voice based sentiment analysis")
    st.write("by @Protyush :wave:")

    st.header("Record your own voice :studio_microphone:")
    
    if st.button(f"Click to Record"):
        recognizer= sr.Recognizer()
        with sr.Microphone() as source:
            print('Clearing background noise...')
            st.subheader("Clearing background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print('Waiting for your message...')
            st.subheader("Waiting for your message...")
            recordedaudio= recognizer.listen(source)
            print('Done recording...')
            st.subheader("Done recording...")

        try:
            print('Printing the message...')
            text= recognizer.recognize_google(recordedaudio, language='en-US')
            print('Your message:{}'.format(text))
            st.text_area(label="#Printing message...", value=text, height=20)
        except Exception as ex:
            #print(ex)
            st.write("# Please give some input")



        
        Sentence=[str(text)] 
        analyser= SentimentIntensityAnalyzer()
        for i in Sentence:
            v=analyser.polarity_scores(i)
            if v == 0:
                st.write("# Neutral 😐")
            elif v["compound"] < -0.05:
                st.write("# Negative 😔")
            elif v["compound"] >=0.05:
                st.write("# Positive 😄")
            else:
                st.write("# Neutral 😐")




if __name__=='__main__':
    main()