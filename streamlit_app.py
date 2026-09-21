import os
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="@misty_highlander_99 • Instagram", page_icon="📸", layout="centered"
)

# Custom CSS styling
css_style = """
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
"""
st.markdown(css_style, unsafe_allow_html=True)

with st.container():
    # Instagram Header
    col_avatar, col_info = st.columns([1, 2.5])

    with col_avatar:
        # Load 'profile.jpg' if present in the repository, otherwise load fallback
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
            "**2** posts &nbsp;&nbsp;&nbsp;&nbsp; **1,789** followers &nbsp;&nbsp;&nbsp;&nbsp; **312** following"
        )

    # Bio section with English & Gaelic phrases
    st.markdown(
        "<b>A. M. MacMhìcheil</b><br>"
        "🌧️ <i>Mìneachadh:</i> Living where the mist never clears.<br>"
        "💬 <i>'Tha cupa tì agam'</i>? No! I don't have a verb 'to have', I only have things that are <b>'at me'</b>! ⛰️<br>"
        "⚙️ My tea is always hot and my grammar strictly starts with the verb.<br>"
        "<i>Còas a tha thu? Slàinte mhath!</i> 🥃<br>"
        "🔗 <i>linktr.ee/uisge_beatha</i>",
        unsafe_allow_html=True,
    )

    # Highlights
    st.markdown("<br>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🥃</div>Tigh-òsta</div>",
            unsafe_allow_html=True,
        )
    with h2:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>⛰️</div>Ceò</div>",
            unsafe_allow_html=True,
        )
    with h3:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🪧</div>Rathad</div>",
            unsafe_allow_html=True,
        )
    with h4:
        st.markdown(
            "<div class='highlight-item'><div class='highlight-circle'>🌧️</div>Uisge</div>",
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center; font-weight: bold; font-size: 14px; letter-spacing: 1px; margin-bottom: 15px;'>⊞ POSTS</div>",
        unsafe_allow_html=True,
    )

    # --- POST 1 ---
    st.markdown(
        "<div class='post-card'><div class='post-header'>📍 An Tigh-òsta (The local pub), Highlands</div>",
        unsafe_allow_html=True,
    )

    if os.path.exists("post1.jpg"):
        st.image("post1.jpg", use_container_width=True)
    else:
        st.image(
            "https://images.unsplash.com/photo-1544717305-2782549b5136?w=600&auto=format&fit=crop&q=80",
            use_container_width=True,
        )

    st.markdown(
        "<div class='post-footer'>"
        "<strong>misty_highlander_99</strong> <em>Slàinte mhath!</em> 🥃 Sorseggiando un po' di <em>Uisge beatha</em> for the soul.<br>"
        '<i>Tha glainne whisky agam</i> = "There is a glass of whisky <em>at me</em>" (literally!). '
        "Quite a unique way to possess things, right? Deep syntax mysteries... <i>Oidhche mhath!</i><br><br>"
        '<small style="color: #8e8e8e;">❤️ 342 likes &nbsp;&nbsp;&nbsp; 💬 45 comments</small>'
        "</div></div>",
        unsafe_allow_html=True,
    )

    # --- POST 2 ---
    st.markdown(
        "<div class='post-card'><div class='post-header'>📍 Ancoiste Magna (Remote Area)</div>",
        unsafe_allow_html=True,
    )

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=600&auto=format&fit=crop&q=80",
        use_container_width=True,
    )

    st.markdown(
        "<div class='post-footer'>"
        "<strong>misty_highlander_99</strong> <i>Fàilte gu àite iomallach!</i> (Welcome to a remote place!) 🪧<br>"
        "Bilingual road sign out here: the top part is faded by heavy rain, while the bottom section displays broad vowels, slender consonants, and aspirated sounds puzzling to outsiders!<br>"
        "Whenever I speak, verbs always jump <strong>straight to the beginning of the sentence</strong> (<i>Sgrìobh mi...</i> = Wrote I...). VSO word order always.<br><br>"
        '<small style="color: #8e8e8e;">❤️ 512 likes &nbsp;&nbsp;&nbsp; 💬 89 comments</small>'
        "</div></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")
    with st.expander("🔍 [CLASSIFIED] Detective Debriefing & Clues"):
        st.markdown(
            """
        * **Rules Followed:** No language name explicitly mentioned and no national flags displayed[cite: 2].
        * **Gaelic Expressions Embedded:** 
            - *Slàinte mhath!* (Good health! / Toast)
            - *Uisge beatha* (Water of life = Whisky)
            - *Fàilte* (Welcome)
            - *Tha... agam* (Structure for possession: "Is... at me")
            - *Tigh-òsta* (Pub/Inn), *Ceò* (Mist), *Rathad* (Road), *Uisge* (Rain/Water)
        * **Clue 1 (No verb 'to have'):** Uses the prepositional structure *"at me"* (*agam*).
        * **Clue 2 (VSO Word Order):** Verb-Subject-Object structure (*Sgrìobh mi*).
        * **Clue 3 (Phonetics):** Mentions broad/slender vowels and aspirated consonants.
        """
        )
