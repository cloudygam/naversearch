import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_naver_web(keyword):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    encoded = urllib.parse.quote(keyword)
    url = f"https://search.naver.com/search.naver?query={encoded}"

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    results = []

    items = soup.select('a.lnk_head')  # 광고성 상단 링크 포함

    for item in items:
        title = item.text.strip()
        link = item['href']
        results.append({
            '제목': title,
            '링크': link,
        })

    return results

# Streamlit 앱
st.title("🔎 네이버 지역검색")

query = st.text_input("검색어를 입력하세요:")

if query:
    with st.spinner("네이버 검색 중..."):
        results = search_naver_web(query)

    if results:
        for r in results:
            st.markdown(f"### [{r['제목']}]({r['링크']})")
            st.markdown("---")
    else:
        st.warning("검색 결과를 찾을 수 없습니다.")
