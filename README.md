# Streamlit Github 로 배포하기
🚀 배포 사이트 : https://aivle-app-ql94wa2navxf5ewwax5n8k.streamlit.app/

안녕하세요! 에이블스쿨에서 배운 Streamlit 을 이용해 간단하게 사이트를 만들고 배포하는 연습을 했습니다.

이 중 깃허브와 연동해 배포하는 초간단 방법을 소개하려고 합니다. (git 몰라도 됨)

## 1. 깃허브 계정 만들기
### 1-1
![image](https://github.com/user-attachments/assets/9c277433-b059-4e16-8c10-2aefb143bab8)

- https://github.com/
- 오른쪽 위의 Sign up 버튼을 눌러 만들 수 있습니다
- 구글 계정과 연동 가능합니다

<br>


## 2. Streamlit 계정 만들기
### 2-1
![image](https://github.com/user-attachments/assets/3ca0d82f-e99c-4dce-a8f3-e74276d163ec)

- https://streamlit.io/
- 깃허브와 마찬가지로 오른쪽 위의 Sign up 버튼을 눌러 만들 수 있습니다
- 구글 및 깃허브 계정과 연동 가능합니다

<br>


## 3. 깃허브 레포지토리 생성하기
### 3-1
![image](https://github.com/user-attachments/assets/e9ce3d36-97e1-4235-9cb9-1ad8aeae3745)
### 3-2
![image](https://github.com/user-attachments/assets/31833b57-ede5-499e-bf82-81d89e325da3)


- repository 탭에서 new 버튼을 눌러 새로운 레포지토리를 생성합니다
- 레포지토리 이름(마음대로), public, add readme.md file 로 설정합니다
- 가장 아래의 create repository 버튼을 누르면 새로운 레포지토리가 생성됩니다

<br>


## 4. 레포지토리에 파이썬 파일 저장하기
### 4-1
![image](https://github.com/user-attachments/assets/0cec3d96-f8fb-4089-912d-5fda9b0f654a)
### 4-2
![image](https://github.com/user-attachments/assets/0a2d921a-6ec9-4b98-9522-cdbb77dc6f41)
### 4-3
![image](https://github.com/user-attachments/assets/10cfc181-1986-4bb6-bab0-366a8d997991)


- Add file > Upload files 에 들어갑니다
- 파일 탐색기에서 내가 만든 파이썬 파일을 찾아 드래그 앤 드랍으로 가져옵니다. (제 파일의 이름은 test.py 입니다)
- 만약 파이썬 파일에서 csv 파일을 불러오는 코드가 있다면, 해당 csv 파일도 함께 가져옵니다. (이 때, 파이썬 코드에서 불러오는 방법과 해당 파일의 경로가 동일해야 합니다.)
- 가장 아래의 commit changes 버튼을 눌러 저장합니다.

<br>

## 5. requirements.txt 파일 만들기
### 5-1
![image](https://github.com/user-attachments/assets/a9e2a56a-bf97-40a4-8ca0-2ece294692b0)
### 5-2
![image](https://github.com/user-attachments/assets/405afc60-c1e7-4efd-948f-7b4d2171e34f)


- Add file > New file 에 들어갑니다
- 파일 이름을 requirements.txt 로 설정합니다
- 내용에는 내가 사용한 모듈의 이름을 적습니다 (streamlit, pandas, numpy 등)
- 오른쪽 상단의 commit changes 를 눌러 저장합니다. (팝업 창이 뜨면 동일하게 누릅니다)

<br>

## 6. streamlit 에서 새로운 앱 만들기
### 6-1
![image](https://github.com/user-attachments/assets/500a3a12-1fed-40f4-921d-e6b2fcfd9271)
### 6-2
![image](https://github.com/user-attachments/assets/369e885b-af34-486e-b545-83a5690cb7fa)
### 6-3
![image](https://github.com/user-attachments/assets/82696882-56b2-489b-a02f-66bd8d5ab033)

- https://share.streamlit.io/
- 나의 streamlit 페이지에서 상단의 Create app 을 클릭합니다
- 미리 github 레포지토리를 만들어 두었으므로 I have an app 을 클릭합니다
- 깃허브 계정과 연동합니다 (로그인 요구 시 깃허브 계정 로그인)
- 깃허브와 연동이 된 경우, 자동으로 깃허브 레포지토리 목록이 뜨고, 그 중 배포할 레포지토리를 선택합니다
- Branch 는 main 입니다
- Main file path 는 내가 만든 파이썬 파일 이름입니다
- app url 은 자동으로 생성되므로 건너 뛰어도 됩니다
- Deploy! 를 누릅니다

<br>

## 7. 배포 기다리기
### 7-1
![image](https://github.com/user-attachments/assets/6c43e4dc-9868-4a28-8c87-7447e380990d)

- 배포가 되는 것을 기다립니다 (약 1분 ~ 5분 소요될 수 있습니다)
- 너무 오래 걸린다면 배포 중 에러가 발생했을 가능성이 높습니다.
- 오른쪽 하단의 Manage app 을 누르면 배포 중 어떤 에러가 발생했는 지 확인 할 수 있습니다.
- 배포 환경은 로컬 환경과 매우 다릅니다. requirements.txt 에 모듈 하나를 빼먹었다던가, csv 파일 경로가 틀리다던가 등의 오류가 발생할 수 있습니다.
- 만약 오류가 발견되어 파이썬 파일을 변경했다면, Manage app 에서 Reboot App 을 누르면 빌드가 다시 진행됩니다.

<br>

## 8. 배포 완료
### 8-1
![image](https://github.com/user-attachments/assets/dc35f246-3ce8-4644-88c7-d2991d502aff)

- 빌드가 성공적으로 수행되었다면, 나만의 사이트 배포가 완료됩니다!
- url 을 친구들과 함께 공유하고 즐거운 경험을 나눠보세요😀

<br>

# 감사합니다
혹시 진행 중 오류가 발생되거나 궁금한 사항은 우리반 커뮤니티에 댓글을 달아주시거나, 팀즈로 연락 주세요ㅎㅎ
