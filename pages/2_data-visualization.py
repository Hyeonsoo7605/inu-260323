import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# 페이지 제목
st.title('데이터 시각화 예제')

# 한글 폰트 설정
font_path = Path(__file__).parent.parent / 'fonts' / 'NanumGothic-Bold.ttf'
if font_path.exists():
    font_prop = fm.FontProperties(fname=str(font_path))
    plt.rcParams['font.family'] = font_prop.get_name()
else:
    plt.rcParams['font.family'] = 'DejaVu Sans'  # 기본 폰트

# 샘플 데이터 생성 또는 기존 데이터 사용
# 기존 GDP 데이터를 사용
DATA_FILENAME = Path(__file__).parent.parent / 'data' / 'gdp_data.csv'
if DATA_FILENAME.exists():
    raw_gdp_df = pd.read_csv(DATA_FILENAME)
    # 간단히 처리: 몇 개 국가만 선택
    countries = ['USA', 'CHN', 'JPN', 'DEU', 'FRA']
    gdp_df = raw_gdp_df[raw_gdp_df['Country Code'].isin(countries)].melt(
        ['Country Code'],
        [str(x) for x in range(2010, 2023)],
        'Year',
        'GDP',
    )
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])
    gdp_df = gdp_df.dropna()
else:
    # 샘플 데이터 생성
    data = {
        '년도': [2020, 2021, 2022],
        '판매량': [100, 150, 200],
        '수익': [50, 75, 100]
    }
    gdp_df = pd.DataFrame(data)

# 섹션 1: Matplotlib 막대 그래프
st.header('Matplotlib 막대 그래프 예제')

fig, ax = plt.subplots()
if 'Country Code' in gdp_df.columns:
    # GDP 데이터로 막대 그래프
    for country in countries:
        country_data = gdp_df[gdp_df['Country Code'] == country]
        ax.bar(country_data['Year'], country_data['GDP'] / 1e9, label=country)
else:
    ax.bar(gdp_df['년도'], gdp_df['판매량'], label='판매량')

ax.set_xlabel('년도')
ax.set_ylabel('GDP (십억 달러)' if 'Country Code' in gdp_df.columns else '판매량')
ax.set_title('국가별 GDP 추이' if 'Country Code' in gdp_df.columns else '연도별 판매량')
ax.legend()
st.pyplot(fig)

# 섹션 2: Plotly 선 그래프
st.header('Plotly 선 그래프 예제')

if 'Country Code' in gdp_df.columns:
    fig = px.line(gdp_df, x='Year', y='GDP', color='Country Code', title='국가별 GDP 선 그래프')
    fig.update_layout(
        xaxis_title='년도',
        yaxis_title='GDP',
        font=dict(family='Arial', size=12)
    )
else:
    fig = px.line(gdp_df, x='년도', y='판매량', title='연도별 판매량 선 그래프')
    fig.update_layout(
        xaxis_title='년도',
        yaxis_title='판매량'
    )
st.plotly_chart(fig)

# 섹션 3: Plotly 산점도
st.header('Plotly 산점도 예제')

if 'Country Code' in gdp_df.columns:
    fig = px.scatter(gdp_df, x='Year', y='GDP', color='Country Code', title='국가별 GDP 산점도')
    fig.update_layout(
        xaxis_title='년도',
        yaxis_title='GDP'
    )
else:
    fig = px.scatter(gdp_df, x='년도', y='수익', title='연도별 수익 산점도')
    fig.update_layout(
        xaxis_title='년도',
        yaxis_title='수익'
    )
st.plotly_chart(fig)
