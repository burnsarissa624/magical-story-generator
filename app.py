import streamlit as st
import random
import os
import uuid
import time

# Core NLP
import spacy
from spacy import displacy
from textblob import TextBlob
import streamlit.components.v1 as components


# Streamlit components
import streamlit.components.v1 as components

st.set_page_config(page_title="Magical Story Generator", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #f8e1f4, #d0f0f6, #fff0f5, #e0f7fa);
        background-size: 600% 600%;
        animation: gradientFlow 20s ease infinite;
        padding: 2rem;
        border-radius: 20px;
    }

    @keyframes gradientFlow {
        0% {background-position: 0% 50%;}
        25% {background-position: 50% 50%;}
        50% {background-position: 100% 50%;}
        75% {background-position: 50% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stButton>button {
        background-color: #ff85c1;
        color: white;
        border-radius: 15px;
        padding: 0.6em 1.4em;
        font-size: 16px;
        font-weight: bold;
        border: none;
        box-shadow: 2px 2px 10px #f3b0c3;
        transition: all 0.3s ease-in-out;
        z-index: 1;
    }

    .stButton>button:hover {
        background-color: #ffb6d9;
        color: #6a1b9a;
        transform: scale(1.05);
        box-shadow: 0 0 15px #ff85c1;
    }
            
    </style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
div.stForm button {
    background-color: #ff85c1;
    color: white;
    border-radius: 15px;
    padding: 0.6em 1.4em;
    font-size: 16px;
    font-weight: bold;
    border: none;
    box-shadow: 2px 2px 10px #f3b0c3;
    transition: all 0.3s ease-in-out;
}

div.stForm button:hover {
    background-color: #ffb6d9;
    color: #6a1b9a;
    transform: scale(1.05);
    box-shadow: 0 0 15px #ff85c1;
}
</style>
""", unsafe_allow_html=True)



#  STORY GENERATOR
def generate_story(character, setting, object_, level):
    if level == "Early Reader (Ages 4–6)":
        story_templates = [
            f"The {character} was in the {setting}. They saw a {object_}. It sparkled! Then they danced and laughed. What a fun day!",
            f"One day, a {character} found a {object_} in the {setting}. It glowed bright! The {character} smiled big. The end!"
        ]
    elif level == "Growing Reader (Ages 7–9)":
        story_templates = [
            f"In a magical {setting}, a brave {character} found a glowing {object_}. When they touched it, the {object_} made the trees sing. The {character} ran to explore what else it could do.",
            f"The {character} was playing in the {setting} when they saw something shiny. It was a {object_}! They picked it up and suddenly they could fly!"
        ]
    else:  # Confident Reader (Ages 10+)
        story_templates = [
            f"Once upon a time, a curious {character} lived in a peaceful {setting}. One morning, they discovered a glowing {object_} hidden behind a tree. As they picked it up, the ground rumbled, and a secret door appeared beneath their feet. With courage in their heart, the {character} stepped through and found a world full of music, laughter, and dancing clouds. That adventure taught them that the bravest hearts find magic where no one else thinks to look.",
            f"In the heart of the {setting}, a brave little {character} stumbled upon a dusty old {object_} lying near a sparkling stream. The {object_} shimmered with a soft light, and as soon as they touched it, a map appeared in the sky made of stars. Following the glowing trail, the {character} met talking animals, rainbow bridges, and even a giggling cloud. By the end of the journey, they realized the real treasure was the friends they made along the way.",
            f"The {character} had always dreamed of going beyond the {setting}, but they never had a reason—until they found a mysterious {object_} that whispered secrets in the wind. As they held it close, a hot air balloon floated down from the sky, waiting just for them. They climbed aboard and soared through golden skies, discovering candy mountains and islands that bounced. Every place they visited taught them something new about kindness, joy, and courage. And when they returned home, the {character} knew they'd never be the same.",
            f"One quiet afternoon in the {setting}, the {character} heard a tiny voice calling their name. Following the sound, they found a tiny creature trapped inside a glowing {object_}. With gentle hands, the {character} set them free, and in return, the creature granted them one wish. Instead of wishing for riches, the {character} wished for a world where everyone could be happy and kind. That wish spread through the {setting} like sunshine, making it the happiest place on Earth.",
            f"Every {character} in the {setting} had heard stories about the magical {object_}, but no one had ever seen it—until now. When the {character} found it buried beneath the oldest tree, they felt a warm glow in their chest. That night, stars danced above them and spelled out a secret message: 'Your heart holds the key.' From that moment on, the {character} used the magic to help others, turning the {setting} into a place of hope and wonder. And whenever someone new came along, they shared their story, reminding everyone that magic is real when you believe in yourself."
        ]

    return random.choice(story_templates)

# MAIN APP 
st.markdown("<h1 style='color:#ff69b4; font-size: 42px;'> Magical Story Generator for Kids! </h1>", unsafe_allow_html=True)
st.markdown("Create your own magical adventure with a character, setting, and magical object!")

feeling = st.text_input("How are you feeling today?")
reading_level = st.selectbox("Choose your reading level:", ["Early Reader (Ages 4–6)", "Growing Reader (Ages 7–9)", "Confident Reader (Ages 10+)"])
character = st.selectbox("Pick a character:", ["unicorn", "robot", "dragon", "kitten"])
setting = st.selectbox("Pick a setting:", ["forest", "beach", "space"])
object_ = st.selectbox("Pick a magical object:", ["magic wand", "treasure map", "glowing rock", "crystal star"])

#MOOD DETECTION 
def get_mood_response(feeling_text):
    analysis = TextBlob(feeling_text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.3:
        return "You're feeling great! Let's add a joyful twist to your adventure! "
    elif polarity < -0.3:
        return "Oh no! Let’s make this story extra magical to cheer you up "
    else:
        return "A peaceful vibe today... sounds like a calm journey awaits "


    if feeling:
        mood_response = get_mood_response(feeling)
        st.markdown(f"**Mood Match:** {mood_response}")

    st.markdown(f"###  Your Story:\n{story}")

    image_path = f"images/{setting}.png"
    st.image(image_path, caption="...", use_container_width=True)

if st.button(" Generate Whimsical Story!"):
    story = generate_story(character, setting, object_, reading_level)


    if feeling:
        mood_response = get_mood_response(feeling)
        st.markdown(f"**Mood Match:** {mood_response}**")

    st.markdown(f"### Your Whimsical Story:\n{story}")

    image_path = f"images/{setting}.png"
    st.image(image_path, caption=f"A scene from the {setting}", use_container_width=True)





#  MAD LIBS 
def generate_mad_lib(adjective, animal, object_, place):
    return f"The {adjective} {animal} danced with a {object_} under the {place}, and everyone clapped with joy! "

#  CONTINUE MY STORY 
def continue_story(starting_line):
    endings = [
        "Suddenly, a glittering light appeared in the sky, and everything changed.",
        "Just then, a friendly dragon flew by and dropped a sparkling envelope.",
        "They turned the corner and found a portal made of music and mist.",
        "A talking mushroom appeared, offering advice and magical tea.",
        "Little did they know, that was just the beginning of their greatest adventure."
    ]
    return starting_line + " " + random.choice(endings) 

#  NAMED ENTITY HIGHLIGHTER 
# --- Magical Keyword Highlighter ---
st.markdown("---")
st.markdown("<h2 style='color:#6a1b9a;'>Magical Entity Highlighter!</h2>", unsafe_allow_html=True)


ner_text = st.text_area("Paste or type a story to highlight magical terms:")

def highlight_magical_keywords(text):
    magical_keywords = [
        "dragon", "unicorn", "kitten", "robot",
        "glowing rock", "magic wand", "treasure map", "crystal star",
        "rainbow", "forest", "beach", "space",
        "cloud", "candy", "hot air balloon", "creature"
    ]
    for word in magical_keywords:
        text = text.replace(
            word, f"<mark style='background-color:#fff3cd; padding:2px; border-radius:4px;'>{word}</mark>"
        )
    return text

if st.button("Highlight Magical Terms"):
    if ner_text.strip():
        highlighted_text = highlight_magical_keywords(ner_text)
        st.markdown(highlighted_text, unsafe_allow_html=True)
    else:
        st.warning("Please enter a story first!")




#  MAD LIBS MODE 
st.markdown("---")
st.markdown("<h2 style='color:#00bcd4;'> Mad Libs Story Mode!</h2>", unsafe_allow_html=True)


with st.form("mad_libs_form"):
    adj = st.text_input("Enter an adjective:", "fancy")
    animal = st.text_input("Enter an animal:", "panda")
    obj = st.text_input("Enter an object:", "balloon")
    place = st.text_input("Enter a place:", "moon")
    submit_libs = st.form_submit_button("Generate Mad Libs Story")

if submit_libs:
    mad_libs_story = generate_mad_lib(adj, animal, obj, place)
    st.markdown(f"### Mad Libs Story:\n{mad_libs_story}")

# CONTINUE MY STORY MODE 
st.markdown("---")
st.markdown("<h2 style='color:#ff85c1;'> Continue my Story!</h2>", unsafe_allow_html=True)


user_start = st.text_input("Write the first sentence of your story:")

if st.button(" Continue It!"):
    if user_start.strip():
        continuation = continue_story(user_start)
        st.markdown(f"### Your Continued Story:\n{continuation}")
    else:
        st.warning("Please type a sentence first!")

# EDUCATIONAL QUESTION GENERATOR

st.markdown("---")
st.markdown("<h2 style='color:#6a1b9a;'>Educational Question Generator!</h2>", unsafe_allow_html=True)


edu_story = st.text_area("Paste your story to generate questions:")

def extract_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    characters = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    places = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
    return characters, places


def generate_questions(text, character, setting, object_):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    questions = [
        f"Why do you think the {character} was in the {setting}?",
        f"What do you think made the {object_} magical?",
        f"What adventure did the {character} go on after finding the {object_}?",
        f"How did the {setting} change throughout the story?",
        f"What kind of friends did the {character} meet? Were they helpful or silly?",
        f"What lesson did the {character} learn by the end of their journey?",
        f"If you had the {object_}, what would *you* do with it?"
    ]

    # Add sentiment-based moral question
    if sentiment > 0.3:
        questions.append("What made this story joyful or exciting?")
    elif sentiment < -0.3:
        questions.append("Was there a sad or tricky part? How could the characters fix it?")
    else:
        questions.append("What peaceful or calming parts stood out to you?")

    return questions

if st.button(" Generate Educational Questions"):
    if edu_story.strip():
        questions = generate_questions(edu_story, character, setting, object_)
        st.subheader("Here are your magical questions!:")
        for q in questions:
            st.markdown(f"- {q}")
    else:
        st.warning("Please paste your story first!")




