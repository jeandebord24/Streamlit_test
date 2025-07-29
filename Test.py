import streamlit as st
import time

# -----------------------------
# CONFIGURATION DE LA PHRASE
# -----------------------------
PHRASE_DU_JOUR = "Je ne dois pas parler pendant les cours."
NB_LIGNES_A_ECRIRE = 10

# -----------------------------
# INITIALISATION DES ETATS
# -----------------------------
if "count" not in st.session_state:
    st.session_state.count = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "logs" not in st.session_state:
    st.session_state.logs = []
if "finished" not in st.session_state:
    st.session_state.finished = False

# -----------------------------
# AFFICHAGE DE L'INTERFACE
# -----------------------------
st.title("📘 Phrase du jour")
st.subheader(f"Écris la phrase ci-dessous {NB_LIGNES_A_ECRIRE} fois exactement à l'identique :")
st.code(PHRASE_DU_JOUR)

st.markdown(f"**Progrès** : {st.session_state.count} / {NB_LIGNES_A_ECRIRE}")

# -----------------------------
# FORMULAIRE DE SAISIE
# -----------------------------
with st.form("punition_form", clear_on_submit=True):
    user_input = st.text_input("Ta phrase (exactement) :")
    submitted = st.form_submit_button("Valider")

# -----------------------------
# TRAITEMENT DE LA REPONSE
# -----------------------------
if submitted and not st.session_state.finished:
    if user_input.strip() == PHRASE_DU_JOUR:
        st.session_state.count += 1
        elapsed_time = round(time.time() - st.session_state.start_time, 2)
        st.session_state.logs.append((st.session_state.count, elapsed_time))

        if st.session_state.count >= NB_LIGNES_A_ECRIRE:
            st.session_state.finished = True
            st.success("🎉 Tu as fini les 100 lignes de punition !")
            st.balloons()
        else:
            st.success(f"✅ Ligne {st.session_state.count}/{NB_LIGNES_A_ECRIRE} validée.")
    else:
        st.error("❌ La phrase est incorrecte. Vérifie l'orthographe exacte.")

# -----------------------------
# AFFICHAGE DES TEMPS RECENTS
# -----------------------------
if st.session_state.logs:
    st.write("⏱️ Temps par ligne (5 dernières) :")
    for idx, t in st.session_state.logs[-5:]:
        st.write(f"Ligne {idx} : {t} sec")


