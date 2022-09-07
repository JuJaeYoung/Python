# web site 명을 추출하고 콘텐츠 명을 제출

def crawling( url ) :
    if '://' in url:
        words = url.split('/')

        site = words[2]
        content = words[3]
    else :
        print('주소를 정확히 입력해주세요.')
    
    return site, content

url = input('Site 명을 추출할 주소를 입력해주세요. : ')
#url = 'https://sports.news.naver.com/wfootball/vod/index?category=&tab=&listType=total&date=&gameId=&teamCode=&playerId=&keyword=&id=980810&page=1'
crawling(url)

a,b = crawling(url)

print(f'사이트명 : {a}\n콘텐츠 : {b}')



# 강사님 풀이

def crawling( s ) :             # url을 문자열로 받아서 구문분석을 통해 Site 명을 추출하여 반환
    if s.find('://') == -1:     # site 주소인지 확인
        return 'No Site'        # site 가 아니라면 'No Site'반환             
    x = s.split('/')

    return x[2]

s1 = crawing(url)
print(f'URL : {url}')
print(f'Site : {s1}')
