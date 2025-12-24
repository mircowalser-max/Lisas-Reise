import streamlit as st

# Grundkonfiguration
st.set_page_config(page_title="Lisas Auszeit", page_icon="🏔️")

# Session State initialisieren
if 'step' not in st.session_state:
    st.session_state.step = 0

# Titelbild (Direkt vom Hotel-Server)
st.image("https://www.fruttmountainresort.com/fileadmin/_processed_/7/0/csm_FMR_Aussenansicht_Winter_3_f6b39d10c0.jpg")

# --- SPIELLOGIK ---

if st.session_state.step == 0:
    st.title("🏔️ Mission: Mama-Auszeit")
    st.write(f"Hallo Lisa, seit 7 Monaten dreht sich deine Welt um den kleinen Elio. Zwischen Windeln, Brei und kurzen Nächten hast du dir eine Pause verdient.")
    if st.button("Abenteuer starten"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.header("Level 1: Das Echo")
    st.info("Ich antworte jedem, habe aber keinen Mund. Was bin ich?")
    ans1 = st.text_input("Deine Antwort:").lower().strip()
    if "echo" in ans1:
        st.success("Richtig!")
        if st.button("Weiter"):
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.header("Level 2: Der Weg")
    st.write("Folge der 'Frucht' im Namen:")
    choice = st.radio("Wohin?", ["Engelberg", "Melchsee-Frutt", "Hasliberg"])
    if st.button("Weg wählen"):
        if "Frutt" in choice:
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("Falscher Weg!")

elif st.session_state.step == 3:
    st.header("Level 3: Das Schloss")
    st.info("Wenn du meinen Namen sagst, bin ich gebrochen. Was bin ich?")
    ans3 = st.text_input("Lösung:").lower().strip()
    if any(x in ans3 for x in ["stille", "ruhe"]):
        st.success("GEWONNEN!")
        if st.button("GUTSCHEIN ANZEIGEN"):
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.title("🎁 DEIN GESCHENK")
    st.markdown("""
    ### 1 Übernachtung im Frutt Mountain Resort
    **Melchsee-Frutt, Schweiz**
    
    Lisa, am 25. Januar 26 ist es so weit, pack die Koffer! WGönn dir eine Pause.
    Damit du voll entspannen kannst, ist Elio bei Noni gut versorgt. 
    """)
    if st.button("Neustart"):
        st.session_state.step = 0
        st.rerun()

