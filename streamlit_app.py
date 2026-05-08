import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_a = pd.read_json('heart_failure_a.json')
df_b = pd.read_json('heart_failure_b.json')
df = pd.merge(df_a, df_b, on='person_id', how='inner')


# #1 그대로 streamlit으로 구현

# g = sns.jointplot(
#     data=df,
#     x='ejection_fraction',
#     y='age',
#     hue='DEATH_EVENT'
# )

# st.pyplot(g.fig)

# #2 스모킹 여부를 한꺼번에 표시하지 말고 라디오로 선택하여 다른 그래프를 볼 수 있도록 구현


# smoking_option = st.radio(
#     "Smoking 여부 선택",
#     ["전체", "흡연자", "비흡연자"]
# )


# if smoking_option == "흡연자":
#     filtered_df = df[df["smoking"] == 1]
# elif smoking_option == "비흡연자":
#     filtered_df = df[df["smoking"] == 0]
# else:
#     filtered_df = df

# fig, ax = plt.subplots()

# sns.violinplot(
#     data=filtered_df,
#     x="DEATH_EVENT",
#     y="platelets",
#     hue="smoking",
#     split=True,
#     ax=ax
# )

# st.pyplot(fig)

# #3. 심박출(ejection_fraction)로 범위를 한정하여 그래프 구현
# #   심박출의 범위는 slider로 선택

# ef_min, ef_max = st.slider(
#     "Ejection Fraction 범위 선택",
#     0, 80, (20, 60)
# )


# filtered_df = df[
#     (df["ejection_fraction"] >= ef_min) &
#     (df["ejection_fraction"] <= ef_max)
# ]

# fig, ax = plt.subplots()

# sns.histplot(
#     data=filtered_df,
#     x="time",
#     bins=20,
#     hue="DEATH_EVENT",
#     ax=ax
# )

# st.pyplot(fig)