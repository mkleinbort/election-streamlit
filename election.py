import streamlit as st

st.set_page_config(layout='wide')

FOX = 'https://www.youtube.com/watch?v=_nF0c4mbURE&ab_channel=NewsNOWfromFOX'
NBC = 'https://www.youtube.com/watch?v=iwRA-dtub7Y&ab_channel=NBCNews'

#ABC = 'https://www.youtube.com/watch?v=w_Ma8oQLmSM&ab_channel=ABCNews'
TELE = 'https://www.youtube.com/watch?v=MqHm48qskRE&ab_channel=TheTelegraph'

b,c = st.beta_columns((1,1))

with b:
    st.title('NBC News')
    st.video(NBC)

with c:
    st.title('The Telegraph')
    st.video(TELE)
