import streamlit as st
from recommendation import recommend, get_song_list

st.set_page_config(
    page_title="TuneAI",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 TuneAI")
st.caption("AI-Powered Music Recommendation System")

songs = get_song_list()

selected_song = st.selectbox(
    "🎶 Select a Song",
    songs
)

if st.button("🎧 Recommend"):

    with st.spinner("Finding similar songs..."):

        recommendations = recommend(selected_song)

    if recommendations:

        st.success(f"Found {len(recommendations)} similar songs!")

        st.divider()

        for song in recommendations:

            with st.expander(f"🎵 {song['Song']}"):

                st.write(f"**👤 Artist:** {song['Artist']}")
                st.write(f"**💿 Album Type:** {song['Album']}")
                st.write(f"**⭐ Popularity:** {song['Popularity']}")
                st.write(f"**⏱ Duration:** {song['Duration']}")
                

    else:
        st.warning("No recommendations found.")