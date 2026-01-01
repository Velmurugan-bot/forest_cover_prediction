import streamlit as st
import pandas as pd
import joblib

model = joblib.load(model.pkl(1)')

st.title("🌲 Forest Cover Type Prediction")

#Input fields - numeric features
elevation = st.number_input("Elevation", min_value=0)
aspect = st.number_input("Aspect", min_value=0)
slope = st.number_input("Slope", min_value=0)
horizontal_distance_to_hydrology = st.number_input("Horizontal Distance to Hydrology")
vertical_distance_to_hydrology = st.number_input("Vertical Distance to Hydrology")
horizontal_distance_to_roadways = st.number_input("Horizontal Distance to Roadways")
hillshade_9am = st.number_input("Hillshade 9am")
hillshade_noon = st.number_input("Hillshade Noon")
hillshade_3pm = st.number_input("Hillshade 3pm")
horizontal_distance_to_fire_points = st.number_input("Horizontal Distance to Fire Points")


st.subheader("Wilderness Area")
wilderness_area = st.selectbox("Select Area", ["Rawah", "Neota", "Comanche Peak", "Cache la Poudre"])
wilderness_encoded = [0, 0, 0, 0]
