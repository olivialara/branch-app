import streamlit as st
import pandas as pd
import numpy as np
#plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio


# def make_values(start, end, size, epsilon, sensitivity):
#     true_values = list(np.random.randint(low=start, high = end, size = size, dtype=int))
#     df = pd.DataFrame (true_values, columns = ['true_values'])
#     return(make_laplace(epsilon, sensitivity, df))

def make_laplace(epsilon, sensitivity, df):
    df['laplace_values'] = df['true_values'] + [np.random.laplace(loc=0, scale = sensitivity/epsilon) for idx in range(len(df))]
    df = df.drop(columns=['Unnamed: 0'])
    st.dataframe(df)
    return(graph_distribution(df))

def graph_distribution(df):
    pio.templates.default = 'plotly_dark'
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df['true_values'], histnorm = 'probability', marker_color = '#0000FF', name = 'True Values'))
    fig.add_trace(go.Histogram(x=df['laplace_values'], histnorm = 'probability', marker_color = '#DE3163', name = 'Laplace Noise Added'))

    # overlay both histograms and add titles
    fig.update_layout(barmode='overlay',
                    xaxis_title_text='True Values', # xaxis label
                    yaxis_title_text='Probability',)

    fig.update_layout(title = '<b>True Distribution vs Laplace Distribution with Dist b/w 0 and 1,000</b>', title_x = .45)

    # reduce opacity to see both histograms
    fig.update_traces(opacity=0.5)
    return(fig)

def graph_curves(df):
    hist_data = [df['true_values'], df['laplace_values']]

    group_labels = ['true', 'laplace']
    colors = ['#F7DC6F', '#DE3163']

    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                            bin_size=.2, show_rug=False, show_hist=False)

    # Add title
    fig.update_layout(title_text='Curve Plot with 100 Values', title_x = .5,
                    xaxis_title_text='Number of Apps',
                    yaxis_title_text='Probability')
    return fig