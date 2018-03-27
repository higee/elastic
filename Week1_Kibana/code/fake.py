import datetime
import socket
import random
import struct

from elasticsearch import Elasticsearch

def fake_data(es, name, n):
    x = ['예약', '일반']
    y = [1, 2, 3, 4, 5]
    prob = [0.1, 0.9]
    probs_sex = [0.45, 0.55]
    probs = [0.3, 0.1, 0.3, 0.2, 0.1]
    probs_memo = [0.3, 0.1, 0.3, 0.12, 0.1, 0.05, 0.03]
    probs_month = [0.2, 0.1, 0.05, 0.05, 0.07, 0.03, 0.02, 0.02, 0.16, 0.05, 0.1, 0.15]
    probs_city = [0.3, 0.08, 0.03, 0.06, 0.07, 0.08, 0.03, 0.09, 0.063, 0.0205, 0.0305, 0.03, 0.05, 0.03, 0.001, 0.03, 0.005]

    for i in range(1, n+1):

        doc = dict()

        # 접수번호
        order = i

        # 접수시간
        year = random.choice(range(2018, 2019))
        if year == 2017:
            month = random.choices(range(1, 13), weights=probs_month, k=1)[0]
            if month in [1, 3, 5, 7, 8, 10, 12]: 
                day = random.choice(range(1, 32))
            elif month in [4, 6, 9, 11]:
                day = random.choice(range(1, 31))
            elif month == 2:
                day = random.choice(range(1, 28))

        else: 
            month = random.choice(range(1, 4))
            if month in [1, 5, 7, 8, 10, 12]: 
                day = random.choice(range(1, 32))
            elif month in [4, 6, 9, 11]:
                day = random.choice(range(1, 31))
            elif month in [2, 3]:
                day = random.choice(range(1, 28))

        hour = random.choice(range(0, 24))
        minute = random.choice(range(0, 60))
        second = random.choice(range(0, 60))

        try:
            date = datetime.datetime(year, month, day, hour, minute, second)
        except ValueError as e:
            print(month, day, e)          

        delta_days = random.choices(range(0, 5), weights=probs, k=1)[0]
        delta_hours = random.choice(range(0, 23))
        delta_minutes = random.choice(range(0, 59))

        delivery_date = date + datetime.timedelta(days=delta_days, hours=delta_hours, minutes=delta_minutes)

        # 예약여부
        reserve = random.choices(x, weights=prob, k=1)[0]

        # 배송메모
        memos = ['부재중', '관리실에 맡김', '상품 이상', '주소 오류', '환불 요청', '무인택배함에 보관', '시간 내에 배송 못함']
        memo = random.choices(memos, weights=probs_memo, k=1)[0]

        # 고객ip
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

        # 고객 성별
        sex = random.choices(['남성','여성'], weights=probs_sex, k=1)[0]

        # 고객 나이
        age = random.choice(range(17, 65))

        # 물건 좌표
        x_ = random.choice(range(35, 37)) + random.random()
        y_ = random.choice(range(126, 129)) + random.random()

        loc = "{}, {}".format(x_, y_)

        cities = ["서울특별시", "경상남도", "경상북도", "전라남도", "전라북도", "충청남도", "충청북도", "세종특별자치시", "강원도", "경기도", "울산광역시", "대전광역시", "광주광역시", "인천광역시", "대구광역시", "부산광역시", "제주특별자치도"]
        city = random.choices(cities, weights=probs_city, k=1)[0]

        # 구매 사이트
        site = random.choices(['11번가', '옥션', 'g마켓', '쿠팡', '위메프', '티몬', 'GS샵'], weights=probs_memo, k=1)[0]

        # 판매자 평점
        rate = random.choices(y, weights=probs, k=1)[0]

        # 상품 분류
        if sex == '남성':
            item = random.choice(['청바지','점퍼','자켓','베스트','팬츠','셔츠', '수트','코트','남방','스웨터','티셔츠','가디건','니트'])
        elif sex == '여성':
            item = random.choice(['청바지', '자켓','팬츠','셔츠','원피스','스커트','코트','스웨터','티셔츠','가디건','니트','블라우스'])

        # 상품 가격
        price = random.choice(range(5000, 30000, 1000))

        # 상품 개수
        quantity = random.choice([1, 7])

        # 결제 카드
        card = random.choices(['우리', '신한', '국민', '하나', '롯데', '시티', '삼성'], weights=probs_memo, k=1)[0]

        doc['접수번호'] = i
        doc['주문시간'] = date
        doc['수령시간'] = delivery_date
        doc['예약여부'] = reserve
        doc['배송메모'] = memo
        doc['고객ip'] = ip
        doc['고객성별'] = sex
        doc['고객나이'] = age
        doc['물건좌표'] = loc
        doc['고객주소_시도'] = city
        doc['구매사이트'] = site
        doc['판매자평점'] = rate
        doc['상품분류'] = item
        doc['상품가격'] = price
        doc['상품개수'] = quantity
        doc['결제카드'] = card

        es.index(index=name, doc_type=name, body=doc)
