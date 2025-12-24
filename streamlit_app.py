import streamlit as st
import time

# Seitenkonfiguration
st.set_page_config(page_title="Lisas Mama-Auszeit", page_icon="🏔️")

# Styling für ein schönes Design
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Spielzustand initialisieren (damit die App sich merkt, bei welcher Quest Lisa ist)
if 'quest' not in st.session_state:
    st.session_state.quest = 0

def nex_quest():
    st.session_state.quest += 1

# --- GAME LOGIC ---

if st.session_state.quest == 0:
    st.title("🏔️ Mission: Mama-Auszeit")
    st.subheader("Hallo Lisa!")
    st.write(f"Seit 7 Monaten dreht sich deine Welt um den kleinen Elio. Zwischen Windeln, Brei und kurzen Nächten hast du dir eine Pause verdient.")
    st.write("Um dein Ziel zu erreichen, musst du 3 Rätsel lösen. Bist du bereit?")
    if st.button("Abenteuer starten"):
        nex_quest()

elif st.session_state.quest == 1:
    st.header("Level 1: Die Talstation")
    st.write("Das Tor zur Gondel ist verschlossen. Ein Rätsel erscheint:")
    st.info("Ich habe keinen Mund, aber ich antworte jedem, der mich ruft. Ich habe keinen Körper, aber der Wind trägt mich. Was bin ich?")
    
    answer = st.text_input("Deine Antwort:", key="q1").lower().strip()
    if answer:
        if "echo" in answer:
            st.success("Richtig! Die Gondel setzt sich in Bewegung.")
            if st.button("Weiter zum nächsten Level"):
                nex_quest()
        else:
            st.error("Leider falsch. Ein kleiner Tipp: Man hört es in den Bergen.")

elif st.session_state.quest == 2:
    st.header("Level 2: Der Wegweiser")
    st.write("Du bist oben angekommen. Wo geht es zum Resort?")
    st.write("Hinweis: Folge der 'Frucht', die im Namen steckt.")
    
    choice = st.radio("Wähle einen Pfad:", ("Pfad zum Engelberg", "Pfad zur Melchsee-Frutt", "Pfad zum Hasliberg"))
    
    if st.button("Diesen Weg gehen"):
        if "Frutt" in choice:
            st.success("Genau! 'Frutt' klingt fast wie Fruit. Du bist auf dem richtigen Weg.")
            nex_quest()
        else:
            st.warning("Hier wird es zu kalt. Das scheint nicht der richtige Weg zu sein.")

elif st.session_state.quest == 3:
    st.header("Level 3: Das Schloss zur Erholung")
    st.write("Du stehst vor der Lobby. Das Schloss öffnet sich nur bei der richtigen Antwort:")
    st.info("Ich bin das, was du dir wünschst, wenn Elio nachts weint. Sobald du meinen Namen sagst, bin ich gebrochen. Was bin ich?")
    
    answer_3 = st.text_input("Deine Antwort:", key="q3").lower().strip()
    if answer_3:
        if any(word in answer_3 for word in ["stille", "ruhe", "schweigen"]):
            st.success("Das Schloss klickt leise. Willkommen in der Geborgenheit.")
            if st.button("DEIN GESCHENK ÖFFNEN"):
                nex_quest()
        else:
            st.error("Noch nicht ganz. Denk an das, was passiert, wenn Elio endlich tief schläft...")

elif st.session_state.step == 4:
    st.balloons()
    st.title("🎁 DEIN GESCHENK")
    st.markdown("""
    ### 1 Übernachtung im Frutt Mountain Resort
    **Melchsee-Frutt, Schweiz**
    
    Lisa, am 25. Januar 26 ist es so weit, pack die Koffer! Gönn dir eine Pause.
    Elio ist bei Noni in den besten Händen, damit du richtig entspannen kannst.
    """)
    
    if st.button("Spiel neustarten"):
        st.session_state.quest = 0



