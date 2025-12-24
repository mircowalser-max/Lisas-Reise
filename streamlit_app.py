import streamlit as st

# Grundkonfiguration
st.set_page_config(page_title="Lisas Auszeit", page_icon="🏔️")

# Session State initialisieren
if 'step' not in st.session_state:
    st.session_state.step = 0

# --- SPIELLOGIK ---

if st.session_state.step == 0:
    st.title("🏔️ Mission: Mama-Auszeit")
    st.write(f"**Hallo Lisa,**
    
    Erinnerst du dich noch an das Gefühl von absoluter Ruhe? In den letzten 7 Monaten war dein Herz 
    und dein Kopf pausenlos bei dem kleinen Elio. Du hast Windeln gewechselt, Lieder gesungen und 
    Wachposten an seinem Bett gehalten. Du bist eine wunderbare Mama.
    
    Doch heute laden wir dich ein, für einen Moment die Augen zu schließen. Stell dir vor, du stehst 
    am Fuße der Schweizer Alpen. Der Schnee knirscht unter deinen Stiefeln, und die Luft ist so frisch, 
    dass sie in der Nase prickelt. Dein Weg zur Erholung beginnt genau hier. 
    
    Bist du bereit, dem Alltag für einen Moment zu entfliehen?")
    if st.button("Abenteuer starten"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.header("Level 1: Die vergessene Stimme der Berge")
    st.write("""
    Du stehst an der alten Talstation. Die Gondeln schaukeln sanft im Wind, bereit, dich aus dem Tal 
    hinauf in die Wolken zu tragen. Doch der Gondelführer, ein bärtiger Mann mit Lachfalten, hält dich 
    kurz auf. 
    
    'Bevor du die Höhe erreichst, Lisa, musst du das Geplapper des Tals hinter dir lassen', sagt er. 
    'Hör genau hin. In den Felswänden wohnt jemand, der keine eigene Stimme hat, aber jedes deiner 
    Worte kennt.'
    """)
    st.info("Das Rätsel: Ich habe keinen Mund, aber ich antworte jedem, der mich ruft. Ich habe keinen Körper, aber der Wind trägt mich. Was bin ich?")
    
    ans1 = st.text_input("Deine Antwort:").lower().strip()
    if "echo" in ans1:
        st.success("Richtig! Der Gondelführer nickt und die Tür schließt sich sanft.")
        if st.button("Hinaufschweben..."):
            st.session_state.step = 2
            st.rerun()

elif st.session_state.step == 2:
    st.header("Level 2: Der Pfad der Verheißung")
    st.write("""
    Die Gondel öffnet sich und ein gleißendes Weiß empfängt dich. Du befindest dich auf einem Hochplateau. 
    Hier oben scheint die Zeit langsamer zu fließen. Vor dir gabelt sich der Weg im tiefen Pulverschnee. 
    
    Ein alter, hölzerner Wegweiser zeigt in verschiedene Richtungen. Die Inschriften sind alt, aber 
    eine davon leuchtet fast golden in der Wintersonne. Es heißt, man müsse der 'Frucht' folgen, um 
    den Ort der wahren Regeneration zu finden.
    """)
    
    choice = st.radio("Welchem Wegweiser vertraust du?", ["Der Pfad zum Engelberg", "Die Route zur Melchsee-Frutt", "Der Steig zum Hasliberg"])
    if st.button("Dem Wegweiser folgen"):
        if "Frutt" in choice:
            st.success("Goldrichtig! Der Weg führt dich direkt auf den glitzernden See zu.")
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("Der Schnee wird hier zu tief... das ist nicht der richtige Weg. Kehr lieber um!")

elif st.session_state.step == 3:
    st.header("Level 3: Das Tor zur inneren Ruhe")
    st.write("""
    Nach einer kurzen Wanderung erblickst du ein majestätisches Gebäude am Ufer des gefrorenen Sees. 
    Das **Frutt Mountain Resort**. Du trittst an die schwere Holztür. Ein wohliger Duft von Zirbenholz 
    und brennendem Kaminfeuer dringt nach draußen. 
    
    Doch bevor die Klinke nachgibt, erscheint eine letzte Inschrift im Glas der Tür. Es ist die 
    Bedingung für deinen Aufenthalt – ein Versprechen an dich selbst:
    """)
    st.info("Das letzte Rätsel: Ich bin das, wonach du dich sehnst, wenn Elio nachts weint. Man kann mich nicht sehen und nicht anfassen. Aber sobald du meinen Namen aussprichst, bin ich gebrochen. Was bin ich?")
    
    ans3 = st.text_input("Deine Lösung:").lower().strip()
    if any(x in ans3 for x in ["stille", "ruhe", "schweigen"]):
        st.success("Die Tür schwingt lautlos auf. Du bist angekommen.")
        if st.button("DEIN GESCHENK ENTGEGENNEHMEN"):
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.title("🎁 Willkommen im Urlaub, Lisa!")
    st.image("https://storage.kempinski.com/cdn-cgi/image/w=1920,f=auto,fit=scale-down/ki-cms-prod/images/6/8/4/7/717486-1-eng-GB/1ec526639ef3-Exterior_winter_gallery.jpg")
    
    st.markdown("""
    ### Ein Gutschein nur für DICH
    
    **1 Übernachtung im Frutt Mountain Resort** *Melchsee-Frutt, Schweiz*
    
    Lisa, du hast in den letzten Monaten Unglaubliches geleistet. Jetzt ist es Zeit, die Batterien 
    wieder aufzuladen. Genieße das Spa, das fantastische Essen und vor allem: **Die Stille.**
    
    Elio wird in der Zwischenzeit bestens von Noni umsorgt sein.  
    """)
    if st.button("Die Reise noch einmal erleben"):
        st.session_state.step = 0
        st.rerun()




