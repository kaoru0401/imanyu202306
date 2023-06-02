import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('streamlit入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!'
expander= st.beta_expander('問い合わせ')
expander.write('問い合わせの回答')
    
# #★２カラム
# st.write('Interractive Widgets')

# left_column, right_column = st.beta_columns(2)
# button= left_column.button('右カラムにボタンを表示')
# if button:
#     right_column.write('ここは右カラム')
# #★エキスパンダー
# expander= st.beta_expander('問い合わせ')
# expander.write('問い合わせの回答')






#★サイドバー
# st.sidebar.write('Interractive Widgets')
# text= st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は', 0, 100, 50)
# 'あなたの趣味：', text, 'です。'
# 'コンデション：', condition

#★インタラクティブなウィジェット４msgbox
# condition = st.slider('あなたの今の調子は', 0, 100, 50)
# 'コンデション：', condition

#★インタラクティブなウィジェット３msgbox
# text= st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text, 'です。'

#★インタラクティブなウィジェット２selectbox
# option= st.selectbox(
#     '好きな数字を教えてください、',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は', option, 'です。'
# img= Image.open('200801140402000.jpg')
# st.image(img, caption= "Audi", use_column_width=True)


# st.table(df.style.highlight_max(axis=0))
# df = pd.DataFrame(
#     np.random.rand(100, 2)/ [50, 50] + [35.69, 139.70],
#     columns= ["lat", "lon"]

# )
# st.map(df)