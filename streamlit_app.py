import os
import streamlit as st
from PIL import Image

# Configurazione della pagina
st.set_page_config(
    page_title="@misty_highlander_99 • Instagram", page_icon="📸", layout="centered"
)

# Stile CSS personalizzato per simulare l'interfaccia di Instagram
st.markdown(
    """
    <style>
    .ig-container {
        max-width: 600px;
        margin: 0 auto;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #262626;
    }
    .highlight-item {
        text-align: center;
        font-size: 12px;
        color: #8e8e8e;
    }
    .highlight-circle {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        border: 1px solid #dbdbdb;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        background-color: #fafafa;
        margin-bottom: 4px;
    }
    .post-card {
        background-color: white;
        border: 1px solid #dbdbdb;
        border-radius: 8px;
        padding: 0px;
        margin-bottom: 20px;
    }
    .post-header {
        padding: 12px;
        font-weight: bold;
        font-size: 14px;
        border-bottom: 1px solid #efefef;
    }
    .post-footer {
        padding: 12px;
        font-size: 14px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

with st.container():
    # Intestazione Instagram
    col_avatar, col_info = st.columns([1, 2.5])

    with col_avatar:
        # Carica automaticamente 'profile.jpg' se presente nel repository
        if os.path.exists("profile.jpg"):
            st.image("profile.jpg", width=110)
        else:
            st.image(
                "https://images.unsplash.com/photo-1509114397022-ed747cca3f65?w=300&auto=format&fit=crop&q=80",
                width=110,
            )

    with col_info:
        st.markdown("#### **misty_highlander_99** &nbsp; ✅")
        st.markdown(
            "**2** post &nbsp;&nbsp;&nbsp;&nbsp; **1,789** followers &nbsp;&nbsp;&nbsp;&nbsp; **312** following"
        )

    # Bio del profilo con indizi linguistici
    st.markdown(
        """
        <b>A. M. MacMhìcheil</b><br>
        🌧️ Living where the mist never clears.<br>
        💬 Non ho un verbo 'avere', ho solo cose che stanno 'presso' di me. ⛰️<br>
        ⚙️ Il mio tè è sempre caldo e la mia grammatica inizia sempre col verbo.<br>
        🔗 <i>linktr.ee/uisge_beatha</i>
    """,
        unsafe_allow_html=True,
    )

    # Storie in evidenza (Highlights)
    st.markdown("<br>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🥃</div>Pub</div>",
            unsafe_allow_html=True,
        )
    with h2:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>⛰️</div>Mist</div>",
            unsafe_allow_html=True,
        )
    with h3:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🪧</div>Road</div>",
            unsafe_allow_html=True,
        )
    with h4:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🌧️</div>Rain</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center; font-weight: bold; font-size: 14px; letter-spacing: 1px; margin-bottom: 15px;'>⊞ POSTS</div>",
        unsafe_allow_html=True,
    )

    # --- POST 1: Personaggio che sorseggia whisky al pub ---
    st.markdown(
        """
    <div class="post-card">
        <div class="post-header">📍 The local pub, Highlands</div>
    """,
        unsafe_allow_html=True,
    )

    # Carica automaticamente 'post1.jpg' se presente nel repository
    if os.path.exists("post1.jpg"):
        st.image("post1.jpg", use_container_width=True)
    else:
        st.image(
            "https://images.unsplash.com/photo-1544717305-2782549b5136?w=600&auto=format&fit=crop&q=80",
            use_container_width=True,
        )

    st.markdown(
        """
        <div class="post-footer">
            <strong>misty_highlander_99</strong> <em>Uisge beatha</em> per l'anima, sorseggiando lentamente al pub. 🥃<br>
            A volte mi guardo intorno e penso: "C'è un bicchiere di whisky <em>a me</em>" (letteralmente!). Strano modo di possedere le cose, vero? Misteri della mia struttura sintattica profonda...<br><br>
            <small style="color: #8e8e8e;">❤️ 342 likes &nbsp;&nbsp;&nbsp; 💬 45 comments</small>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- POST 2: Cartello stradale bilingue remoto ---
    st.markdown(
        """
    <div class="post-card">
        <div class="post-header">📍 Ancoiste Magna (Remote Area)</div>
    """,
        unsafe_allow_html=True,
    )

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=600&auto=format&fit=crop&q=80",
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="post-footer">
            <strong>misty_highlander_99</strong> Cartello stradale bilingue in un luogo remoto: la parte superiore è sbiadita dalla pioggia battente, mentre quella inferiore mostra una dicitura ricca di vocali larghe e consonanti aspirate incomprensibile ai non addetti! 🪧<br>
            Quando provo a presentarmi qui, i verbi saltano sempre <strong>all'inizio della frase</strong> prima ancora del soggetto (VSO). Nessuna eccezione.<br><br>
            <small style="color: #8e8e8e;">❤️ 512 likes &nbsp;&nbsp;&nbsp; 💬 89 comments</small>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    with st.expander("🔍 [CLICCA QUI] Soluzione e Indizi per la Classe"):
        st.markdown(
            """
        * **Regole rispettate:** Nessun nome di lingua esplicito e nessuna bandiera nazionale[cite: 2].
        * **Indizio 1 (Il verbo avere):** L'uso della costruzione possessiva con "presso di me".
        * **Indizio 2 (Sintassi VSO):** I verbi che precedono sempre il soggetto e l'oggetto.
        * **Indizio 3 (*Uisge beatha*):** L'origine etimologica del termine whisky e i suoni aspirati/gutturali.
        """
        )        align-items: center;
        justify-content: center;
        font-size: 24px;
        background-color: #fafafa;
        margin-bottom: 4px;
    }
    .post-card {
        background-color: white;
        border: 1px solid #dbdbdb;
        border-radius: 8px;
        padding: 0px;
        margin-bottom: 20px;
    }
    .post-header {
        padding: 12px;
        font-weight: bold;
        font-size: 14px;
        border-bottom: 1px solid #efefef;
    }
    .post-footer {
        padding: 12px;
        font-size: 14px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

with st.container():
    # Intestazione in stile Instagram
    col_avatar, col_info = st.columns([1, 2.5])

    with col_avatar:
        # Foto profilo
        st.image(
            "https://images.unsplash.com/photo-1509114397022-ed747cca3f65?w=300&auto=format&fit=crop&q=80",
            width=90,
        )

    with col_info:
        st.markdown("#### **misty_highlander_99** &nbsp; ✅")
        st.markdown(
            "**2** post &nbsp;&nbsp;&nbsp;&nbsp; **1,789** followers &nbsp;&nbsp;&nbsp;&nbsp; **312** following"
        )

    # Bio del profilo con gli indizi linguistici
    st.markdown(
        """
        <b>A. M. MacMhìcheil</b><br>
        🌧️ Living where the mist never clears.<br>
        💬 Non ho un verbo 'avere', ho solo cose che stanno 'presso' di me. ⛰️<br>
        ⚙️ Il mio tè è sempre caldo e la mia grammatica inizia sempre col verbo.<br>
        🔗 <i>linktr.ee/uisge_beatha</i>
    """,
        unsafe_allow_html=True,
    )

    # Storie in evidenza (Highlights)
    st.markdown("<br>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🥃</div>Pub</div>",
            unsafe_allow_html=True,
        )
    with h2:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>⛰️</div>Mist</div>",
            unsafe_allow_html=True,
        )
    with h3:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🪧</div>Road</div>",
            unsafe_allow_html=True,
        )
    with h4:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🌧️</div>Rain</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center; font-weight: bold; font-size: 14px; letter-spacing: 1px; margin-bottom: 15px;'>⊞ POSTS</div>",
        unsafe_allow_html=True,
    )

    # --- POST 1: Il personaggio che sorseggia whisky al pub ---
    st.markdown(
        """
    <div class="post-card">
        <div class="post-header">📍 The local pub, Highlands</div>
    """,
        unsafe_allow_html=True,
    )

    st.image(
        "https://images.unsplash.com/photo-1544717305-2782549b5136?w=600&auto=format&fit=crop&q=80",
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="post-footer">
            <strong>misty_highlander_99</strong> <em>Uisge beatha</em> per l'anima, sorseggiando lentamente al pub. 🥃<br>
            A volte mi guardo intorno e penso: "C'è un bicchiere di whisky <em>a me</em>" (letteralmente!). Strano modo di possedere le cose, vero? Misteri della mia struttura sintattica profonda...<br><br>
            <small style="color: #8e8e8e;">❤️ 342 likes &nbsp;&nbsp;&nbsp; 💬 45 comments</small>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- POST 2: Il cartello stradale bilingue remoto ---
    st.markdown(
        """
    <div class="post-card">
        <div class="post-header">📍 Ancoiste Magna (Remote Area)</div>
    """,
        unsafe_allow_html=True,
    )

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=600&auto=format&fit=crop&q=80",
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="post-footer">
            <strong>misty_highlander_99</strong> Cartello stradale bilingue in un luogo remoto: la parte superiore è sbiadita dalla pioggia battente, mentre quella inferiore mostra una dicitura ricca di vocali larghe e consonanti aspirate incomprensibile ai non addetti! 🪧<br>
            Quando provo a presentarmi qui, i verbi saltano sempre <strong>all'inizio della frase</strong> prima ancora del soggetto (VSO). Nessuna eccezione.<br><br>
            <small style="color: #8e8e8e;">❤️ 512 likes &nbsp;&nbsp;&nbsp; 💬 89 comments</small>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    with st.expander("🔍 [CLICCA QUI] Soluzione e Indizi per la Classe"):
        st.markdown(
            """
        * **Regole rispettate:** Nessun nome di lingua esplicito e nessuna bandiera nazionale[cite: 2].
        * **Indizio 1 (Il verbo avere):** L'uso della costruzione possessiva con "presso di me".
        * **Indizio 2 (Sintassi VSO):** I verbi che precedono sempre il soggetto e l'oggetto.
        * **Indizio 3 (*Uisge beatha*):** L'origine etimologica del termine whisky e i suoni aspirati/gutturali.
        """
        )
