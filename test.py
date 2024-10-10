import streamlit as st
import altair as alt
import pandas as pd
import folium
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# 사이트 이름 표시
st.set_page_config('Aivle Streamlit', '🤖')

# 메인 페이지
def main_page():
    st.title('안녕하세요, 에이블러! 🖐️')
    st.text('')

    # 방명록 보기 함수
    messages_df = pd.read_csv('messages.csv')

    # 방명록 내용 가져오기
    words = []
    for index, row in messages_df.iterrows():       
            words.append(row['message'])

    word_counts = Counter(' '.join(words).split())

    # 컨테이너에 표시
    with st.container(height=320, border=False):
        font = 'LG_Smart_UI-Regular.ttf'
        
        wc = WordCloud(font_path=font,\
            background_color="white", \
            width=450, \
            height=200, \
            max_words=100, \
            max_font_size=300)
        
        wc = wc.generate_from_frequencies(word_counts)

        fig = plt.figure()
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        st.pyplot(fig)
    
    # 방명록 저장
    message = st.chat_input('방명록을 남겨주세요! (띄워쓰기X)')
    if message:
        new_df = pd.DataFrame([message], columns=['message'])
        
        messages_df = pd.concat([messages_df, new_df], ignore_index=True)
        messages_df.to_csv('messages.csv', index=False)

        st.experimental_rerun() # 페이지 새로고침


# 미디어 페이지
def media_page():
    st.title('미디어 센터 📻')
    st.subheader('에이블러에게 추천하는 코딩 플레이스트 🎵')
    tab1, tab2, tab3, tab4 = st.tabs(['클래식', 'K-POP', 'Lofi', '노래추천 :pencil:'])


    with tab1:
        tab11, tab12, tab13 = st.tabs(['상쾌하게 아침 코딩!', '차분한 피아노 연주와 함께', '가슴이 웅장해질 차례!'])

        with tab11:
            st.video('https://youtu.be/zABPDtp-4e0?si=NCSBIg7gkX8ykW4I')

        with tab12:
            st.video('https://youtu.be/YmZLR7311O4?si=EwruZnDTRabz25MG')

        with tab13:
            st.video('https://youtu.be/EJC-_j3SnXk?si=P5_5idlr_YzSfeIF')
            

    with tab2:
        tab21, tab22 = st.tabs(['비트에 손을 맡기자!', '텐션업! 여자 아이돌 노래'])

        with tab21:
            st.video('https://youtu.be/n9EeBm5CMVA?si=h2g7Bn6tUGX_LO13')
            st.caption('7반 에이블러 최애 밴드라규~~')

        with tab22:
            st.video('https://youtu.be/3_twbPXQyQE?si=GjBCKKn0AfnZtSQG')


    with tab3:
        tab31, tab32 = st.tabs(['생각이 복잡할 땐, 단순한 음악!', '코딩할 때 듣는 노래 그 잡채..!!'])

        with tab31:
            st.video('https://youtu.be/BTYAsjAVa3I?si=2kUy-VOhoTlMOKe5')
            
        with tab32:
            st.video('https://youtu.be/AnXmn0Tdfzo?si=tJe7I4oJVn3T50E2')

    with tab4:
        st.markdown('#### 여러분의 최애곡을 추천해주세요!')
        
        music_df = pd.read_csv('recommend_music.csv')

        # 노래 추천하기
        col11, col12 = st.columns(2)
        col21, col22 = st.columns(2)
        
        singer = col11.text_input('가수')
        title = col12.text_input('노래 제목')
        alias = col21.text_input('추천 이유')
        link = col22.text_input('유튜브 링크')

        if st.button('추천하기', use_container_width=True, key='music_recommend'):
            new_df = pd.DataFrame([[singer, title, alias, link]], columns=['singer', 'title', 'alias', 'link'])

            music_df = pd.concat([music_df, new_df], ignore_index=True)
            music_df.to_csv('recommend_music.csv', index=False)

            st.success('신청곡이 추가되었습니다! 🎉')
        else:
            st.error('모든 필드를 입력해주세요 😎')
        

        # 추천 리스트 보기
        st.divider()
        st.markdown('#### 에이블러의 추천 리스트 📜')

        music_df = pd.read_csv('recommend_music.csv')
        st.write(music_df)



# 레이아웃 페이지
def layout_page():
    st.title('틱택토 게임 ⭕❌')

    # 버튼 모양
    st.markdown(
    """
    <style>
    .stButton>button {
        width: 150px;
        height: 150px;
        font-size: 50px;  /* 폰트 크기 설정 */
        text-align: center;
        line-height: 100px;
        border-radius: 10px;
        border: 2px solid #111;
        display: inline-block;
        color: #333;
        background-color: #fff;
        border-color: #ccc;
    }
    
    .stButton>button:focus {
        color: #333;
        background-color: #e6e6e6;
        border-color: #8c8c8c;
    }
    .stButton>button:hover {
        color: #333;
        background-color: #e6e6e6;
        border-color: #adadad;
    }
    .stButton>button:active {
        color: #333;
        background-color: #e6e6e6;
        border-color: #adadad;
    }
    
    </style>
    """, unsafe_allow_html=True
    )

    # 게임 상태 초기화
    if 'board' not in st.session_state:
        st.session_state.board = [' ' for _ in range(9)]  # 3x3 보드 초기화
        st.session_state.current_player = '❌'  # 플레이어는 항상 x
        st.session_state.winner = None
        st.session_state.tie = False

    #-------------------------------------------------------------------------------#    
    # 승리 조건 확인 함수
    def check_winner(board):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # 가로
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 세로
                          (0, 4, 8), (2, 4, 6)]  # 대각선
        for a, b, c in win_conditions:
            if board[a] == board[b] == board[c] and board[a] != ' ':
                return board[a]  # 승리한 플레이어 반환
        if ' ' not in board:
            return 'Tie'  # 무승부일 경우 'Tie' 반환
        return None  # 승자가 없을 경우

    # 컴퓨터가 랜덤으로 o 표시
    def computer_move():
        empty_indices = [i for i, value in enumerate(st.session_state.board) if value == ' ']
        if empty_indices:
            comp_choice = random.choice(empty_indices)
            st.session_state.board[comp_choice] = '⭕'
            st.session_state.winner = check_winner(st.session_state.board)

    # 버튼 클릭 시 동작
    def handle_click(index):
        if st.session_state.board[index] == ' ' and st.session_state.winner is None:
            st.session_state.board[index] = st.session_state.current_player
            st.session_state.winner = check_winner(st.session_state.board)
            
            if st.session_state.winner is None:
                computer_move() # 컴퓨터가 다음 선택
                st.session_state.winner = check_winner(st.session_state.board)
            elif st.session_state.winner == 'Tie':
                st.session_state.tie = True

    # 게임 재시작 함수
    def restart_game():
        st.session_state.board = [' ' for _ in range(9)]
        st.session_state.current_player = '❌'
        st.session_state.winner = None
        st.session_state.tie = False    
    #-------------------------------------------------------------------------------#  
    
    # 3x3 버튼으로 게임 보드 그리기
    for i in range(3):
        cols = st.columns(3)  # 한 줄에 3개의 열 생성
        for j in range(3):
            index = i * 3 + j
            button_label = st.session_state.board[index]  # 현재 보드 상태 가져오기
            
            # 버튼 스타일 적용
            if cols[j].button(f"{button_label}", key=f"button_{index}", on_click=handle_click, args=(index,)):
                pass
    
    # 결과 표시
    if st.session_state.winner == 'Tie':
        st.info("무승부입니다 👻")
    elif st.session_state.winner:
        if st.session_state.winner == '❌':
            st.success('축하합니다! 승리했습니다 🎉')
        else:
            st.error('이런! 컴퓨터에게 지셨군요 🤣')
    
    # 게임 재시작 버튼
    if st.button("재시작 🔁"):
        restart_game()
     

# 차트 페이지
def chart_page():
    st.title('차트 차트 🏅')
    st.subheader('차트로 표현하면 좋을 만한 내용을 생각 중입니다 🤔')
    

# 맵 페이지
def map_page():
    st.title('에이블스쿨 위치 🏙️')
    st.markdown('###### 에이블스쿨은 전국 어디서든 수강할 수 있습니다.')

    aivle_loc = [['KT분당교육장', '수도권', 37.35874, 127.11493, '경기도 성남시 분당구 불정로 90'],
                ['KT전농교육장', '수도권', 37.57733, 127.05654, '서울시 동대문구 사가정로 105'],
                ['KT원주연수원', '강원권', 37.33688, 128.00461, '강원도 원주시 행구동 행구덕현길 109'],
                ['에이블스쿨 BDIA 동구캠퍼스', '부산/경남권', 35.11470, 129.03681, '부산 동구 초량중로29 KCA빌딩'],
                ['KT북대구빌딩', '대구/경북권', 35.88162, 28.58188, '대구광역시 북구 고성로 141'],
                ['KT탄방빌딩', '충남/충북권', 36.34536, 127.38412, '대전광역시 서구 문정로 48번길 30'],
                ['KT신안빌딩', '전남/전북권', 35.16441, 126.90555, '광주광역시 북구 신안동 무등로 202번길']]

    aivle_df = pd.DataFrame(aivle_loc, columns=['name', 'region', 'latitude', 'longitude', 'address'])
    
    # 지도 그리기
    aivle_map = folium.Map( location=[36.34, 127.77], zoom_start=7)

    # 지도에 원형 마커와 값 추가
    for index, row in aivle_df.iterrows():       
        folium.CircleMarker(                     
            location=[row['latitude'], row['longitude']],   
            radius=10,             
            color='mediumturquoise',                        
            fill=True,                           
            fill_opacity=0.8                     
        ).add_to(aivle_map)

        html = f'''
        {row['name']}<br>
        {row['region']}<br>
        {row['address']}
        '''

        iframe = folium.IFrame(html,
                       width=200,
                       height=100)
        
        popup = folium.Popup(iframe)
    
        folium.Marker(                          
            location=[row['latitude'], row['longitude']],
            tooltip=html
        ).add_to(aivle_map)                         

    st.components.v1.html(aivle_map._repr_html_(), width=800, height=600)

    # 데이터 프레임 보여주기
    st.markdown('#### 한 눈에 보기 👀')
    st.write(aivle_df, use_container_width=True)

# 사이드바에 페이지 구성
page_names_to_funcs = {'메인 페이지' : main_page, '미디어 센터' : media_page, '틱택토 게임' : layout_page, '에이블스쿨 위치' : map_page}

st.sidebar.header('Sidebar 🦄')

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('페이지 선택', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()

