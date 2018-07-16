### week5.pdf 실행 스크립트

---
#### input

* stdin
    * p 18 : `$ bin/logstash -f code/input/stdin/stdin.conf`

* file
    * p 24 : `$ bin/logstash -f code/input/file/file.conf`
    * p 29 : `$ bin/logstash -f code/input/file/file-start-position.conf`
    * p 41 : `$ bin/logstash -f code/input/file/file-sincedb-path.conf`
    
* jdbc
    * p 47 : `$ bin/logstash -f code/input/jdbc/jdbc.conf`
    * p 54 : `$ bin/logstash -f code/input/jdbc/jdbc-sql-last-value-1.conf`
    * p 58 : `$ bin/logstash -f code/input/jdbc/jdbc-sql-last-value-2.conf`

* elasticsearch
    * p 67 : `$ bin/logstash -f code/input/elasticsearch/elasticsearch.conf`

---
#### output

* csv
    * p 73 : `$ bin/logstash -f code/output/csv/csv.conf`

* elasticsearch
    * p 78 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch.conf`
    * p 83 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-dynamic-field-name-1.conf`
    * p 88 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-dynamic-field-name-2.conf`
    * p 93 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-stdout.conf`

#### conditional

* if/else if/else
    * p 96 : `$ bin/logstash -f code/output/conditional.conf`

---
#### filter

* csv
    * p 105 : `$ bin/logstash -f code/filter/csv/separator.conf`
    * p 111 : `$ bin/logstash -f code/filter/csv/autodetect-column-names.conf`
    * p 116 : `$ bin/logstash -f code/filter/csv/convert.conf`

* mutate
    * p 125 : `$ bin/logstash -f code/filter/mutate/split.conf`
    * p 130 : `$ bin/logstash -f code/filter/mutate/add_field.conf`
    * p 135 : `$ bin/logstash -f code/filter/mutate/remove_field.conf`
    
* grok
    * p 145 : `$ bin/logstash -f code/filter/grok/access.conf`
    * p 152 : `$ bin/logstash -f code/filter/grok/apache.conf`

* date
    * p 159 : `$ bin/logstash -f code/filter/date/default.conf`
    * p 159 : `$ bin/logstash -f code/filter/date/date.conf`

* drop
    * p 164 : `$ bin/logstash -f code/filter/drop/drop1.conf`
    * p 169 : `$ bin/logstash -f code/filter/drop/drop2.conf`
