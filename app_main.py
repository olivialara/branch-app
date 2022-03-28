import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from app_functions import *

st.title('Laplace Distribution')
  
st.image("laplace-formula.png")


# range_number = st.number_input('Select a size for the dataset', min_value=0, max_value=10_000, value=100)
# st.write('Current size:', range_number)

# values = st.slider('Select a range of values', 0, 10_000, (0, 1000))
# st.write('Values:', values)

# df = pd.DataFrame(
#     np.random.randint(low=values[0], high = values[1], size = range_number, dtype=int),
#     columns=['true_values'])
# st.write(df)
# st.write( df.to_csv('specified_values.csv'))
df = pd.read_csv('specified_values.csv')

# def make_values(start, end, size, epsilon, sensitivity):
#     true_values = list(np.random.randint(low=start, high = end, size = size, dtype=int))
#     df = pd.DataFrame (true_values, columns = ['true_values'])
#     return(make_laplace(epsilon, sensitivity, df))

epsilon = st.number_input("Epsilon Value", min_value=0.0, max_value=5.0, value=0.5, step=0.1)
sensitivity = st.number_input("Sensitivity Value", min_value=0, max_value=10_000, value=1, step=1)
st.write(make_laplace(epsilon, sensitivity, df))

# def make_laplace(epsilon, sensitivity, df):
#     df['laplace_values'] = df['true_values'] + [np.random.laplace(loc=0, scale = sensitivity/epsilon) for idx in range(len(df))]
#     st.dataframe(df)
#     return(graph_distribution(df))

# st.write (make_values(values[0],values[1], range_number, epsilon, sensitivity))

#st.write (make_laplace(epsilon, sensitivity, trues))



# st.write("Which would you like to alter?") 
# menu_set_averages = st.radio("", ("Epsilon(ε)", "Sensitivity(∆f)"),)

# maybe just have an already loaded model and then beside it have inputs
# can change distribution size and other two parameters? 

# def create_small_dist():
#     range_of_dist = [np.random.uniform(low=0, high = 10, size = 1_000)]

# def create_medium_dist():
#     range_of_dist = [np.random.uniform(low=0, high = 1_000, size = 1_000)]

# def create_large_dist():
#     range_of_dist = [np.random.uniform(low=0, high = 10_000, size = 1_000)]