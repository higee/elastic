### week5.pdf 실행 스크립트

---
#### input

* stdin
    * p 17 : `$ bin/logstash -f code/input/stdin/stdin.conf`
    * p 21 : `$ bin/logstash -f code/input/stdin/stdin-rubydebug.conf`

* file
    * p 25 : `$ bin/logstash -f code/input/file/file.conf`
    * p 28 : `$ bin/logstash -f code/input/file/file-start-position.conf`
    * p 38 : `$ bin/logstash -f code/input/file/file-sincedb-path.conf`
    
* jdbc
    * p 42 : `$ bin/logstash -f code/input/jdbc/jdbc.conf`
    * p 47 : `$ bin/logstash -f code/input/jdbc/jdbc-sql-last-value-1.conf`
    * p 49 : `$ bin/logstash -f code/input/jdbc/jdbc-sql-last-value-2.conf`
    * p 52 : `$ bin/logstash -f code/input/jdbc/jdbc-schedule.conf`

* elasticsearch
    * p 56 : `$ bin/logstash -f code/input/elasticsearch/elasticsearch.conf`

---
#### output

* csv
    * p 58 : `$ bin/logstash -f code/output/csv/csv.conf`
    * p 61 : `$ cat data/week5.csv`

* elasticsearch
    * p 63 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch.conf`
    * p 69 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-dynamic-field-name-1.conf`
    * p 71 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-dynamic-field-name-2.conf`
    * p 74 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-stdout.conf`
    * p 77 : `$ bin/logstash -f code/output/conditional.conf`

---
#### filter

* csv
    * p 82 : `$ bin/logstash -f code/filter/csv/separator.conf`
    * p 84 : `$ bin/logstash -f code/filter/csv/autodetect-column-names.conf`
    * p 87 : `$ bin/logstash -f code/filter/csv/convert.conf `

* mutate
    * p 92 : `$ bin/logstash -f code/filter/mutate/split.conf`
    * p 95 : `$ bin/logstash -f code/filter/mutate/add_field.conf`
    * p 97 : `$ bin/logstash -f code/filter/mutate/remove_field.conf`
    
* grok
    * p 105 : `$ bin/logstash -f code/filter/grok/access.conf`
    * p 107 : `$ bin/logstash -f code/filter/grok/access2.conf`
    * p 110 : `$ bin/logstash -f code/filter/grok/apache.conf`

* date
    * p 114 : `$ bin/logstash -f code/filter/date/default.conf`
    * p 116 : `$ bin/logstash -f code/filter/date/date.conf`

* drop
    * p 119 : `$ bin/logstash -f code/filter/drop/drop1.conf`
    * p 120 : `$ bin/logstash -f code/filter/drop/drop2.conf`
