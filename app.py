import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os

# App configuration
st.set_page_config(
    page_title="Multi-Language Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize variables
translated_text = ""

# Sidebar for API configuration
with st.sidebar:
    st.title("🔑 API Configuration")
    
    # Google Gemini configuration
    st.subheader("Google Gemini Settings")
    google_api_key = st.text_input("Google Gemini API Key", type="password", key="google_api_key")
    if google_api_key:
        os.environ["GOOGLE_API_KEY"] = google_api_key
    
    # Model parameters
    st.subheader("Model Parameters")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    model_name = st.selectbox(
        "Model Version",
        ["gemini-1.5-flash"],
        index=0
    )

# Main app interface
st.title("🌍 Multi-Language Translator")
st.caption("Powered by Google Gemini")

# Language selection
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox(
        "Source Language",
        ["Auto Detect", "English", "Spanish", "French", "German", 
         "Italian", "Portuguese", "Russian", "Chinese", "Japanese", "Hindi"],
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        ["English", "Spanish", "French", "German", 
         "Italian", "Portuguese", "Russian", "Chinese", "Japanese", "Hindi"],
        index=0
    )

# Text input area
text_to_translate = st.text_area(
    "Text to Translate",
    height=200,
    placeholder="Enter text here to translate..."
)

# Initialize the model
@st.cache_resource
def load_model(api_key, model_name, temperature):
    try:
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=temperature
        )
    except Exception as e:
        st.error(f"Model initialization failed: {str(e)}")
        return None

# Translation function
def translate_text(model, text, source_lang, target_lang):
    if not text.strip():
        return ""
    
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"You are an expert translator from {source_lang} to {target_lang}"),
            ("human", "{text}")
        ])
        
        chain = prompt | model
        response = chain.invoke({"text": text})
        return response.content
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return ""

# Translate button
if st.button("Translate", type="primary"):
    if not text_to_translate.strip():
        st.warning("Please enter text to translate")
    elif not os.environ.get("GOOGLE_API_KEY"):
        st.error("Please provide a Google Gemini API key in the sidebar")
    else:
        with st.spinner("Translating..."):
            model = load_model(
                api_key=os.environ["GOOGLE_API_KEY"],
                model_name=model_name,
                temperature=temperature
            )
            
            if model:
                translated_text = translate_text(
                    model,
                    text_to_translate,
                    source_lang if source_lang != "Auto Detect" else "English",
                    target_lang
                )
                
                if translated_text:
                    st.subheader("Translation Result")
                    st.text_area(
                        "Translated Text",
                        translated_text,
                        height=200,
                        key="translated_text"
                    )

# History feature
if "history" not in st.session_state:
    st.session_state.history = []

if text_to_translate.strip() and translated_text:
    st.session_state.history.append({
        "source": text_to_translate,
        "translation": translated_text,
        "language_pair": f"{source_lang} → {target_lang}"
    })

if st.session_state.history:
    with st.expander("Translation History"):
        for i, item in enumerate(reversed(st.session_state.history)):
            st.write(f"**{item['language_pair']}**")
            st.caption("Original:")
            st.write(item["source"])
            st.caption("Translation:")
            st.write(item["translation"])
            if i < len(st.session_state.history) - 1:
                st.divider()