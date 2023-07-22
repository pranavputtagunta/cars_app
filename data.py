import streamlit as st
import numpy as np
import pandas as pd

def app(car_df):
	st.header("View Data")
	st.table(car_df)	
