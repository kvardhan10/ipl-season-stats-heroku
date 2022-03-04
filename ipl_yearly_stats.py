import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.markdown("""
# IPL PLAYER STATS BY SEASON
- Data from [IPLT20.com](https://www.iplt20.com/)
""")

feat = ['POS','Player']
st.sidebar.header('Pick year and category')
player_type = st.sidebar.selectbox('Player Type:', ['Batsman','Bowler'])
year = st.sidebar.selectbox('Year:', [x for x in range(2008, 2022)])

if player_type is 'Bowler':
    selected_feat = []
    selected_feat = st.sidebar.multiselect('Player Features:', ['Inns', 'Ov', 'Runs','Wkts', 'BBI', 'Econ', 'SR', '4w', '5w'])
    url = 'https://www.iplt20.com/stats/' + str(year) + '/mostWkts?stats_type=bowling'
    index = 1

if player_type is 'Batsman':
    selected_feat = []
    selected_feat = st.sidebar.multiselect('Player Features:', ['Inns',	'NO', 'Runs', 'HS', 'Avg', 'BF', 'SR', '100', '50', '4s', '6s'])
    url = 'https://www.iplt20.com/stats/' + str(year) + '/mostRuns?stats_type=batting'
    index = 0

num = st.sidebar.slider('How many players?', 1, 30, 10)

if st.button('GET STATS'):
    def download():
        html = pd.read_html(url.strip(), header = 0)
        df = html[index]
        return df

    df = download()
    feat.extend(selected_feat)
    st.write('Showing results for ' + str(df[feat].loc[:num].shape[0] - 1) + ' players with ' + str(df[feat].loc[:num].shape[1] - 2) + ' features')
    st.write(df[feat].loc[:num-1].set_index('POS'))
