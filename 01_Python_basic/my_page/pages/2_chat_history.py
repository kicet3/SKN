import streamlit as st
import localDB

data = localDB.getData('AI')

st.write(data)