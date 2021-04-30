import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

path1 = "Data/pheno_WS.csv"
df1 = pd.read_csv(path1)
columns = df1.columns

def main():
    st.title("タイトル")

    st.subheader("サブヘッダー")
    st.write("String")

    df1 = pd.DataFrame({"a1": np.zeros(10), "a2": np.random.random(10)})
    st.dataframe(data=df1)

    st.button("ラベル")
    st.checkbox("ラベル", value=False)
    st.selectbox("ラベル", ("あお", "あか", "しろ"))

    # スライダー
    st.slider("label", 20, 50, 20, 3, "%f")

    # テキスト入力
    st.text_input("label_hoge", "ちちんぷいぷい")

    # 数値入力
    st.number_input("put number", 20, 50, 23)
    x_axis = st.sidebar.selectbox('x軸項目', columns)

    # ファイルアップロード
    uploaded_file = st.file_uploader("ラベル", type="")
    st.header("file loading")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        st.header("showing graph")

        fig=px.scatter(data_frame=df, x=x_axis, y="YLD")
        st.plotly_chart(fig)


if __name__ == '__main__':
    main()