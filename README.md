# SH_Test
 Test용 파일들 저장소
<div align="center">

<!-- logo -->
<img src="https://user-images.githubusercontent.com/80824750/208554611-f8277015-12e8-48d2-b2cc-d09d67f03c02.png" width="400"/>

### Back-end Git Reamd.me Template ✅

[<img src="https://img.shields.io/badge/-readme.md-important?style=flat&logo=google-chrome&logoColor=white" />]() [<img src="https://img.shields.io/badge/-tech blog-blue?style=flat&logo=google-chrome&logoColor=white" />]() [<img src="https://img.shields.io/badge/release-v0.0.0-yellow?style=flat&logo=google-chrome&logoColor=white" />]() 
<br/> [<img src="https://img.shields.io/badge/프로젝트 기간-2022.12.10~2022.12.19-green?style=flat&logo=&logoColor=white" />]()

</div> 

## 📝 소개
백엔드 깃 레파지토리의 README.md를 빠르게 작성하기 위해 만든 템플릿입니다.

다음과 같은 내용을 작성할 수 있습니다.
- 프로젝트 소개
- 프로젝트 화면 구성 또는 프로토 타입
- 프로젝트 API 설계
- 사용한 기술 스택
- 프로젝트 아키텍쳐
- 기술적 이슈와 해결 과정
- 프로젝트 팀원

  
## PUB/SUB TOPIC 콘솔에서 생성
- 콘솔에서 생성
  </br>
<img src="https://user-images.githubusercontent.com/80824750/208456048-acbf44a8-cd71-4132-b35a-500047adbe1c.gif" width="400"/>
</br>

## Test용 topic, Data Catalog 실습용 topic 생성

- **이름**: `TestTopic`
- **기본서브스크립션**: `생성 안함`
- **토픽 메세지 보존 기간**: `0일 0시 10분`
- **인스턴스유형**: `m2a.xlarge`
- **설명**: `없음`
--------------------------------------------------
- **이름**: `DataCatalogTopic`
- **기본서브스크립션**: `생성 안함`
- **토픽 메세지 보존 기간**: `0일 0시 10분`
- **인스턴스유형**: `m2a.xlarge`
- **설명**: `없음`

## Test용 topic Subscription 생성

- **이름**: `TestTopic-pull`
- **토픽선택**: `TestTopic`
- **유형**: `PULL`
- **서브스크립션 메세지 보존 기간**: `0일 0시 10분`
- **응답 대기 시간**: `20초`
------------------------------------------------------
- **이름**: `TestTopic-push`
- **토픽선택**: `TestTopic`
- **유형**: `PUSH`
- **프로토콜**:`http://`
- **엔드포인트URL**:{API서버1 URL}
- **서브스크립션 메세지 보존 기간**: `0일 0시 10분`
- **응답 대기 시간**: `20초`




# Traffic Generator VM 1,2를 이용해 PUB/SUB 통신하기

이 가이드는 VM1과 VM2를 사용하여 PUB/SUB 통신을 설정하는 방법을 설명합니다.

## 1. VM1: PUB 메시지 전송

- **스크립트 실행**  
  터미널에서 다음 명령어를 입력하여 `pub_sub_send.py` 스크립트를 실행합니다.

  ```
  python3 pub_sub_send.py
  ```
- **정상 실행 시 출력 메시지**
  스크립트가 정상적으로 실행되면 아래와 같은 메시지가 출력됩니다.
  ```
  "CLI 입력 -> Kakao Pub/Sub 전송 프로그램입니다."
  "아래에 전송하고 싶은 문자열을 입력하세요."
  "빈 줄, Ctrl+D, 혹은 'quit' 입력 시 전송을 마칩니다."
  ```

## 2. VM2: SUB 메시지 수신
- **스크립트 실행**
  터미널에서 다음 명령어를 입력하여 restapi_sub.py 스크립트를 실행합니다.

  ```
  python3 restapi_sub.py
  ```
  **정상 실행 시 동작**
  스크립트가 정상적으로 실행되면 VM2에서 지속적으로 메시지를 받아옵니다.


# Traffic Generator VM 2를 이용해 PUB/SUB 토픽, 서브스크립션 생성

  ## 1. VM2: PUB/SUB 토픽생성 

- **스크립트 실행**  
  터미널에서 다음 명령어를 입력하여 `CreateTopic.py` 스크립트를 실행합니다.

```
python3 CreateTopic.py
```

**실행후 카카오 클라우드 콘솔에서 확인**

## 2. VM2: PUB/SUB 서브스크립션 생성 

- **스크립트 실행**  
  터미널에서 다음 명령어를 입력하여 `CreateSubscription.py` 스크립트를 실행합니다.

```
python3 CreateSubscription.py
```


# GO 실습
- publisher.go 실습
```
cd /home/ubuntu/gosdk/cmd
go build -o publisher config.go publisher.go
./publisher
```

- subscriber.go 실습
```
cd /home/ubuntu/gosdk/cmd
go build -o subscriber config.go subscriber.go
./subscriber
```
### 프로토타입
<img src="https://user-images.githubusercontent.com/80824750/208454673-0449e49c-57c6-4a6b-86cf-66c5b1e623dc.png">

<br />

## 🗂️ APIs
작성한 API는 아래에서 확인할 수 있습니다.

👉🏻 [API 바로보기](/backend/APIs.md)


<br />

## ⚙ 기술 스택
> skills 폴더에 있는 아이콘을 이용할 수 있습니다.
### Back-end
<div>
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/Java.png?raw=true" width="80">
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/SpringBoot.png?raw=true" width="80">
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/SpringSecurity.png?raw=true" width="80">
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/SpringDataJPA.png?raw=true" width="80">
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/Mysql.png?raw=true" width="80">
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/Ajax.png?raw=true" width="80">
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/Thymeleaf.png?raw=true" width="80">
</div>

### Infra
<div>
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/AWSEC2.png?raw=true" width="80">
</div>

### Tools
<div>
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/Github.png?raw=true" width="80">
<img src="https://github.com/yewon-Noh/readme-template/blob/main/skills/Notion.png?raw=true" width="80">
</div>

<br />

## 🛠️ 프로젝트 아키텍쳐
![no-image](https://user-images.githubusercontent.com/80824750/208294567-738dd273-e137-4bbf-8307-aff64258fe03.png)



<br />

## 🤔 기술적 이슈와 해결 과정
- Stream 써야할까?
    - [Stream API에 대하여](https://velog.io/@yewo2nn16/Java-Stream-API)
- Gmail STMP 이용하여 이메일 전송하기
    - [gmail 보내기](https://velog.io/@yewo2nn16/Email-이메일-전송하기with-첨부파일)
- AWS EC2에 배포하기
    - [서버 배포하기-1](https://velog.io/@yewo2nn16/SpringBoot-서버-배포)
    - [서버 배포하기-2](https://velog.io/@yewo2nn16/SpringBoot-서버-배포-인텔리제이에서-jar-파일-빌드해서-배포하기)


<br />

## 💁‍♂️ 프로젝트 팀원
|Backend|Frontend|
|:---:|:---:|
| ![](https://github.com/yewon-Noh.png?size=120) | ![](https://github.com/SeongHo-C.png?size=120) |
|[노예원](https://github.com/yewon-Noh)|[이성호](https://github.com/SeongHo-C)|
