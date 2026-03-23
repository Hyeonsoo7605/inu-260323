import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title='자기소개 페이지',
    page_icon=':wave:',  # 이모지 아이콘
)

# 메인 제목
st.title('안녕하세요! 저는 [이현수]입니다.')

# 간단한 소개
st.write("""
여기에 간단한 자기소개를 작성하세요. 예를 들어, 저는 [직업/전공]을 하는 [나이]살 [이름]입니다.
""")

# 사진 추가 (선택적)
# st.image('path/to/your/photo.jpg', caption='프로필 사진', width=200)

# 섹션: 학력
st.header('학력')
st.write('- [학교 이름], [전공], [졸업 연도]')

# 섹션: 경력
st.header('경력')
st.write('- [직장/역할], [기간]')

# 섹션: 관심사
st.header('관심사')
st.write('- [관심사 1]')
st.write('- [관심사 2]')

# 연락처
st.header('연락처')
st.write('이메일: [your.email@example.com]')
st.write('LinkedIn: [링크]')
