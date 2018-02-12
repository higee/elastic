### shopping index : data 및 Dashboard backup 

---

#### 1. 직접 구축한 elasticsearch에서 index 생성 및 mapping 설정

* Kibana Dev Tools 이동
* `shopping-mapping` format으로 index 및 mapping 생성

#### 2. logstash로 실습 데이터 migration

* Logstash Home Directory 이동
* output elasticsearch hosts에 자신의 서버 ip 입력 
* ip 모를 경우 `my ip`에 있는 명령어를 터미널에 입력 후 출력되는 ip 주소 이용
* `shopping.conf`로 logstash 실행 

#### 3. scripted field 생성

* Kibana Management - Index Patterns - scripted fields 이동
* `scripted_field/` 내에 있는 field 직접 하나하나 생성

#### 4. Visualizations 불러오기

* Kibana Management - Saved Objects - Visualizations 이동
* Import 누르고 `import/visualization.json` 선택
* `New Index Pattern`에 `shopping` 선택

#### 5. Dashboard 불러오기

* Kibana Management - Saved Objects - Dashboards 이동
* Import 누르고 `import/dashboard.json` 선택

#### 6. 완성
