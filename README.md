### Elastic Stack을 활용한 Dashboard 만들기 (1기)
---

#### 안내

* 이 repository는 지속적으로 업데이트가 진행됩니다. (`<>Code`, `Issues`, `Wiki`)
* repository 요소별 안내
    * `Code` : Elastic Stack 흐름에 관한 전반적인 설명
    * `Issues` : 자주 들어온 질문 정리
    * `Wiki` : Elastic Stack 사용법에 초점을 맞춘 간단 사용 설명서

#### 기타

* 내용에 대한 피드백(틀린 내용, 설명의 애매함, version upgrade 등)은 언제든지 편하게 알려주세요.
* `Wiki`에서 기본 환경은 AWS Amazon Linux AMI입니다.
* 데이터는 랜덤으로 생성했으니 참고 바랍니다.

#### Jupyter Notebook을 사용하려면

* Jupyter Notebook (혹은 Python)이 없어도 Elastic Stack을 사용하는데 전혀 문제 없습니다.
* Aggregation이 단계별로 어떻게 진행되는지 공유하기 위해 올린 자료이니 필요하신 분만 다운 받으시면 됩니다.
* 설치
    * 기본적으로 python과 pip가 설치되어 있어야 합니다.
    * 파일을 다운 받을 자기 컴퓨터의 경로로 이동
        * 명령어 : `$ cd {path}`
        * 예시 : `$ cd ~/elasticstack`
    * higee/elastic repository 내려받기 : `$ git clone https://github.com/higee/elastic.git`
    * python package 설치
        * `$ cd elastic`
        * `$ pip install -r requirements.txt`
    * 보고 싶은 파일이 있는 경로고 가서 jupyter notebook 실행
        * 예) Week1의 bucket_aggregation 보고 싶은 경우
        * `$ cd Week1/bucket_aggregation`
        * `$ jupyter notebook`
