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
## api 서버
**프로젝트 설치 및 설정 가이드**
이 문서는 클라우드 VM에 프로젝트를 설치하고 설정하는 과정을 단계별로 안내합니다.

**1. 클라우드 VM에 SSH로 연결 후 스크립트 다운로드**

먼저, 클라우드 VM에 SSH로 접속한 후 필요한 스크립트를 다운로드합니다.

```bash
복사
ssh your_username@your_vm_ip_address
wget https://raw.githubusercontent.com/KOlizer/syu-DataAnalyze/refs/heads/main/ApiServer/api_dev.sh
```
**2. 환경 변수 설정**
다운로드한 api_dev.sh 파일을 열어 환경 변수를 설정합니다. vim 편집기를 사용하여 파일을 수정합니다.

```
vim api_dev.sh
```

파일 내에서 다음 변수들을 설정합니다:

```
MYSQL_HOST="{DB 엔드포인트}"
DOMAIN_ID="{조직 ID}"
PROJECT_ID="{프로젝트 ID}"
TOPIC_NAME_PUBSUB="{PUB/SUB Topic 이름}(로그 적재용, API로 생성할 이름)"
TOPIC_NAME_KAFKA="{Kafka Topic 이름}"
CREDENTIAL_ID="{액세스 키 ID}"
CREDENTIAL_SECRET="{보안 액세스 키}"

LOGSTASH_ENV_FILE="/etc/default/logstash"
LOGSTASH_KAFKA_ENDPOINT="{카프카 엔드포인트}"
주의: 각 {} 안에 해당하는 실제 값을 입력해 주세요.
```

**3. 스크립트 실행 권한 부여 및 실행**
환경 변수를 설정한 후, 스크립트에 실행 권한을 부여하고 실행합니다.

```
chmod +x api_dev.sh
sudo ./api_dev.sh
```


**4. 환경 변수 적용 및 추가 스크립트 실행**
모든 설정이 완료된 후, 환경 변수를 적용하고 추가적인 설정 스크립트를 실행합니다.

```
source /home/ubuntu/.bashrc
sudo -E ./setup_db.sh
sudo -E ./main_script.sh
```


설명:

source /home/ubuntu/.bashrc: .bashrc 파일에 설정된 환경 변수를 현재 세션에 적용합니다.
sudo -E ./setup_db.sh: 환경 변수를 유지한 상태로 데이터베이스 설정 스크립트를 실행합니다.
sudo -E ./main_script.sh: 환경 변수를 유지한 상태로 메인 스크립트를 실행합니다.


필요한 기술 스택에 대한 logo는 [skills 폴더](/skills/)에서 다운로드 받을 수 있습니다.

<br />

> 화면 구성과 프로토 타입 중 원하는 것을 사용해주세요.

### 화면 구성
|Screen #1|Screen #2|
|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/80824750/208456048-acbf44a8-cd71-4132-b35a-500047adbe1c.gif" width="400"/>|<img src="https://user-images.githubusercontent.com/80824750/208456234-fb5fe434-aa65-4d7a-b955-89098d5bbe0b.gif" width="400"/>|

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
