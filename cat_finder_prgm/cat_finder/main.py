
import requests
import webbrowser
import random

rand = random.randint(1,2)
#Cat API
if rand == 1:
    CAT_API_URL = "https://cataas.com/cat?json=true"
else:
    CAT_API_URL = "https://cataas.com/cat/gif?json=true"

def get_random_cat_url():
    """
    무작위 고양이 이미지의 URL을 가져와 반환합니다.
    """
    try:
        # API 요청
        response = requests.get(CAT_API_URL)
        response.raise_for_status()
        
        data = response.json()
        if data :
            cat_url = data['url']
            return cat_url
        else:
            return "API 응답에서 유효한 URL을 찾을 수 없습니다."

    except requests.exceptions.RequestException as e:
        return f"API 호출 중 오류가 발생했습니다: {e}"

def show_random_cat():
    """
    무작위 고양이 이미지를 사용자의 기본 웹 브라우저로 띄워줍니다.
    """
    cat_url = get_random_cat_url()
    
    if cat_url.startswith("http"):
        print(f"고양이 URL: {cat_url}")
        webbrowser.open(cat_url)
    else:
        print(f"오류: {cat_url}")