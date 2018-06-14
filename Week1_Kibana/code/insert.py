import os
import sys
import socket
import struct
import random
import datetime

from elasticsearch import Elasticsearch

from fake import fake_data
from es_conf import properties

def main():

    '''
    sys.argv[1] : 데이터 개수
    sys.argv[2] : index postfix
    '''

    # 1. es driver/client 연결
    host = os.environ['fastcampus']
    es = Elasticsearch(host)

    # 2. 수강생 데이터 읽어서 이름 생성
    with open('./email.txt', 'r') as f:
        mails = [s.strip() for s in f.readlines()]
    try:
        postfix = sys.argv[2]
        mail_list = [x.split('@')[0] + '_{}'.format(postfix) for x in mails]
    except IndexError:
        mail_list = [x.split('@')[0] for x in mails]

    for idx, name in enumerate(mail_list):

        # 3. mapping 생성
        if not es.indices.exists(name):
            es.indices.create(name)
            mapping =  {name : properties}
            es.indices.put_mapping(
              index=name,
              doc_type=name,
              body=mapping
            )

        # 4. 데이터 삽입
        n = int(sys.argv[1])
        fake_data(es, name, n)
        print('수강생 {}님의 데이터 {}개가 인덱스 {}에 정상적으로 입력되었습니다.'.format(
            mails[idx].split('@')[0],
            n,
            mail_list[idx]
          )
        )
    
    print('-'*70)
    print('총 {} 명의 데이터가 입력되었습니다.'.format(len(mail_list)))
    print('-'*70)

if __name__ == "__main__":
    main()
