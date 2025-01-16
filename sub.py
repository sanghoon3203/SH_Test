#!/usr/bin/env python3
"""
push_logs_to_pubsub.py

- VM 내 특정 로그 파일(예: traffic_generator.log)의 각 줄을 읽어서,
- Base64 인코딩 후 Kakao Cloud Pub/Sub가 요구하는 JSON 구조 {"messages": [...]}를 생성,
- POST /publish 로 전송

Usage:
  python3 push_logs_to_pubsub.py

(필요하다면 인자나 환경변수로 파일 경로, Pub/Sub URL, Credential 등을 주입해서 쓰세요.)
"""

import os
import base64
import json
import requests

# ==== (1) 설정: 파일 경로 & Pub/Sub API 정보 ====
LOG_FILE_PATH = "/home/traffic_generator.log"

PUBSUB_URL = (
    "https://pub-sub.kr-central-2.kakaocloud.com"
    "/v1/domains/fa22d0db818f48829cf8b7849e3a0a26/"
    "projects/0aa67b93c3ec48e587a51c9f842ca407/"
    "topics/f7a3b81e-f77d-4ca4-8b67-424fb5579524/publish"
)

CRED_ID = "69ea0f3d1a3e4e67aa7b6b826a9b088b"
CRED_SECRET = "40a19910b1098ac3aa8aeab743443f9e0cb81dabc3773ac35174ea04b30ece407783fc"

# ==== (2) 함수: 로그 라인을 Pub/Sub 메시지로 변환 후 전송 ====
def push_logs_to_pubsub(log_lines):
    """
    log_lines: list of strings (각 줄)

    1) 각 줄을 Base64 인코딩
    2) {"messages":[ {"data": "<base64>", "attributes": {...}}, ... ]} 구조로 JSON 생성
    3) requests.post(...)로 Pub/Sub API 호출
    """
    messages = []

    for line in log_lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue  # 빈 줄이면 스킵

        # 1) Base64 인코딩
        encoded_data = base64.b64encode(line_stripped.encode('utf-8')).decode('utf-8')

        # 2) 메시지 객체 구성
        #    Kakao Pub/Sub는 "data" 필드가 Base64 문자열이어야 함
        message_obj = {
            "data": encoded_data,
            "attributes": {
                # 필요하면 추가 메타데이터를 넣을 수 있습니다.
                "source": "traffic_generator",
                "line_length": str(len(line_stripped))
            }
        }
        messages.append(message_obj)

    # 모든 라인을 하나의 요청으로 보낼 경우 (주의: 너무 많으면 Body가 커질 수 있음)
    body = {"messages": messages}

    # 3) Pub/Sub로 전송
    headers = {
        "Credential-ID": CRED_ID,
        "Credential-Secret": CRED_SECRET,
        "Content-Type": "application/json"
    }

    print(f"Sending {len(messages)} messages to Pub/Sub endpoint...")
    resp = requests.post(PUBSUB_URL, headers=headers, json=body, timeout=10)

    print("Response status:", resp.status_code)
    print("Response body:  ", resp.text)
    # 필요시 resp.raise_for_status() 로 에러 시 예외 처리

# ==== (3) 메인 로직 ====
def main():
    # 1) 파일 읽기
    if not os.path.exists(LOG_FILE_PATH):
        print(f"Log file not found: {LOG_FILE_PATH}")
        return

    with open(LOG_FILE_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print("No logs to send.")
        return

    # 2) 전송
    push_logs_to_pubsub(lines)

if __name__ == "__main__":
    main()