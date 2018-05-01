### Elastic Stack을 활용한 Dashboard 만들기
---

#### 안내

* 이 repository는 지속적으로 업데이트가 진행됩니다. (`<>Code`, `Issues`, `Wiki`)
* repository 요소별 안내
    * `Code` : Elastic Stack 흐름에 관한 전반적인 설명
    * `Issues` : 자주 들어온 질문 정리
    * `Wiki` : Elastic Stack 사용법에 초점을 맞춘 간단 사용 설명서

#### 설치

* AWS EC2에 접속 하는 경우를 제외하고는 Windows 및 Mac OS 공통
* 아래 내용의 동영상이며 영상 속 코드를 복사할 수도 있다. 

[![elastic stack install guide](https://asciinema.org/a/176392.png)](https://asciinema.org/a/176392)

----

#### 0. AWS EC2 설정
* AMI : `Amazon Linux 2 LTS Candidate 2 AMI (HVM), SSD Volume Type - ami-96b916f8`
* Security Group
   
    | Type        | Protocol           | Port Range  | Source | Description
    | :------------- |:-------------:| :-----:| :----: | :---|
    | SSH      | TCP | 22 | Custom 0.0.0.0/0 | ssh
    | Custom TCP      | TCP | 9200 | Custom 0.0.0.0/0 | elasticsearch REST
    | Custom TCP      | TCP | 9300 | Custom 0.0.0.0/0 | elasticsearch node communication
    | Custom TCP      | TCP | 5601 | Custom 0.0.0.0/0 | kibana

#### 1. AWS EC2 접속

* Mac OS
    * elastic_camp.pem를 Home directory에 다운 받고 Home으로 이동
    * 예를 들어 ip 주소가 12.345.678.123인 경우
    ```
    $ cd ~
    $ chmod 400 elastic_camp.pem
    $ ssh -i "elastic_camp.pem" ec2-user@ec2-12-345-678-123.ap-northeast-2.compute.amazonaws.com
    ```
* Windows : [클릭](https://github.com/higee/elastic/wiki/AWS-EC2-Instance-%EC%83%9D%EC%84%B1-%EB%B0%8F-%EC%A0%91%EC%86%8D#connect-windows)

#### 2. virtual memory areas 늘리기
* 설명
    * Elasticsearch는 mmapfs 디렉토리에 index를 저장한다 (default 설정)
    * mmap counts에 대한 운영체제의 limit이 default로는 낮게 되어 있어서 높혀주지 않으면 out of memory 발생    
* 방법
    * `$ sudo vim /etc/sysctl.conf`
    * 가장 아래 라인으로 이동 : `shift + g` 입력
    * 새로운 라인으로 편집 모드 : `o` 입력
    * 다음과 같이 입력 `vm.max_map_count=262144`
    * 저장 : `ESC` 누르고 `:wq` 입력 후 `Enter`
    * 재시작 : `$ sudo reboot`

#### 3. docker 설치
* 약 1분 후에 [AWS EC2 접속](#ec2)와 같은 방법으로 재접속한다
* docker 설치 및 현재 유저로도 실행할 수 있도록 설정
```
$ sudo yum install docker -y
$ sudo usermod -aG docker $USER
$ exit
```
* [AWS EC2 접속](#ec2)와 같은 방법으로 재접속
* docker 구동

```$ sudo service docker start```

#### 4. docker-compse 설치 및 실행 가능하게 설정
```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

<a name='git'></a>
#### 5. git 설치 및 repo clone
* git을 설치하고 본 repository를 clone 받는다
* elastic stack 설치에 필요한 스크립트 및 자료를 미리 올려두었다

```
$ sudo yum install git -y
$ git clone -b class3 https://github.com/higee/elastic.git
$ cd elastic/Week4_Elasticsearch/code/install
```

#### 6. elastic stack 실행
* 다운 받은 docker-compose.yml에 설치 및 실행에 필요한 모든 정보가 들어있다.
* 수업 후에 환경에 맞게 customize하고 우선은 default 상태로 실행하자

```
$ docker-compose up 
```

* 혹은 detach mode로 실행
```
$ docker-compose up -d
```

#### 7. logstash 실행
* logstash container를 root로 실행 : `$ docker exec -u 0 -it logstash bash`
* logstash 실행 (편의상 configuraiton 파일도 모두 volume 형태로 mount 해두었다)
* 실행하고 싶은 scenario를 [여기](https://github.com/higee/elastic/blob/class3/Week5_Logstash/code/logstash.md)에서 찾아서 실행하자
* 예를 들어 아래와 같이 하면 파일 데이터를 수집하는 logstash를 실행한다 
```
$ bin/logstash -f code/input/file/file-sincedb-path.conf
```

#### 8. Kibana 접속
* 예를 들어 ip 주소가 12.345.678.123인 경우 : `http://12.345.678.123:5601`
* docker-compose에서 port를 변경해주면 `80번` 혹은 `443번` 포트 등을 사용할 수 있다

#### 9. 혹시 x-pack enabled해서 사용할 경우 default username 및 password는 아래와 같다
```
id : elastic
pwd : changeme
```
---

#### 기타

* 내용에 대한 피드백(틀린 내용, 설명의 애매함, version upgrade 등)은 언제든지 편하게 알려주세요.
* 데이터는 랜덤으로 생성했으니 참고 바랍니다.
