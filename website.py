import streamlit as st
import players

st.title('NFL Qbs')
st.subheader('Hurts')
st.table(players.get_hurts_passing_stats())