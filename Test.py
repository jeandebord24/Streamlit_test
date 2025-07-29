import streamlit as st
import time
from datetime import datetime


# CONFIGURATION DE LA PHRASE À ÉCRIRE
PHRASE_DU_JOUR = "Je ne dois pas parler pendant les cours."

# Titre
st.title("Phrase du jour")
st.write("Écris la phrase ci-dessous **100 fois** exactement à l'identique.")

# Affiche la phrase cible
st.code(PHRASE_DU_JOUR)

# Initialisation des variables de session
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "count" not in st.session_state:
    st.session_state.count = 0
if "logs" not in st.session_state:
    st.session_state.logs = []
if "finished" not in st.session_state:
    st.session_state.finished = False

# Lancement du chrono au premier input
if st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# Initialisation manuelle de la valeur dans session_state
if "input_phrase" not in st.session_state:
    st.session_state.input_phrase = ""

# Champ de texte contrôlé par la valeur dans session_state
user_input = st.text_input("Ta phrase (exactement) :", value=st.session_state.input_phrase, key="input_phrase_field")
aaa= st.session_state.input_phrase
st.code(aaa)
aaa


def clear_text():
    st.session_state["input_phrase_field"] = ""


# Bouton pour valider
if st.button("Valider") and not st.session_state.finished:
    if user_input.strip() == PHRASE_DU_JOUR:
        st.session_state.count += 1
        elapsed_time = round(time.time() - st.session_state.start_time, 2)
        st.session_state.logs.append((st.session_state.count, elapsed_time))
        clear_text
                # 🔁 Réinitialise la phrase dans le champ
        st.session_state.input_phrase = ""
        
        
        if st.session_state.count >= 100:
            st.session_state.finished = True
            st.success("🎉 Tu as fini les 100 lignes de punition !")
            st.balloons()
        else:
            st.success(f"✅ Ligne {st.session_state.count}/100 validée.")
    else:
        st.error("❌ La phrase est incorrecte. Vérifie l'orthographe exacte.")

# Affichage du temps pour chaque ligne validée
if st.session_state.logs:
    st.write("⏱️ Temps par ligne :")
    for idx, t in st.session_state.logs[-5:]:  # Affiche les 5 dernières
        st.write(f"Ligne {idx} : {t} sec")

# Affichage du nombre restant
if not st.session_state.finished:
    st.info(f"Il te reste {100 - st.session_state.count} lignes.")



