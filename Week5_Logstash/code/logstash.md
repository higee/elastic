### week5.pdf 실행 스크립트

---
#### input

* stdin
    * p 17 : `$ bin/logstash -f code/input/stdin/stdin.conf`

* file
    * p 22 : `$ bin/logstash -f code/input/file/file.conf`
    * p 26 : `$ bin/logstash -f code/input/file/file-start-position.conf`
    * p 37 : `$ bin/logstash -f code/input/file/file-sincedb-path.conf`
    
* jdbc
    * p 42 : `$ bin/logstash -f code/input/jdbc/jdbc.conf`
    * p 48 : `$ bin/logstash -f code/input/jdbc/jdbc-sql-last-value-1.conf`
    * p 51 : `$ bin/logstash -f code/input/jdbc/jdbc-sql-last-value-2.conf`

* elasticsearch
    * p 59 : `$ bin/logstash -f code/input/elasticsearch/elasticsearch.conf`

---
#### output

* csv
    * p 63 : `$ bin/logstash -f code/output/csv/csv.conf`

* elasticsearch
    * p 67 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch.conf`
    * p 71 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-dynamic-field-name-1.conf`
    * p 75 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-dynamic-field-name-2.conf`
    * p 79 : `$ bin/logstash -f code/output/elasticsearch/elasticsearch-stdout.conf`

#### conditional

* if/else if/else
    * p 83 : `$ bin/logstash -f code/output/conditional.conf`

---
#### filter

* csv
    * p 89 : `$ bin/logstash -f code/filter/csv/separator.conf`
    * p 94 : `$ bin/logstash -f code/filter/csv/autodetect-column-names.conf`
    * p 98 : `$ bin/logstash -f code/filter/csv/convert.conf`

* mutate
    * p 106 : `$ bin/logstash -f code/filter/mutate/split.conf`
    * p 110 : `$ bin/logstash -f code/filter/mutate/add_field.conf`
    * p 114 : `$ bin/logstash -f code/filter/mutate/remove_field.conf`
    
* grok
    * p 123 : `$ bin/logstash -f code/filter/grok/access.conf`
    * p 129 : `$ bin/logstash -f code/filter/grok/apache.conf`

* date
    * p 135 : `$ bin/logstash -f code/filter/date/default.conf`
    * p 135 : `$ bin/logstash -f code/filter/date/date.conf`

* drop
    * p 139 : `$ bin/logstash -f code/filter/drop/drop1.conf`
    * p 143 : `$ bin/logstash -f code/filter/drop/drop2.conf`

* ruby
    * p 151 : `$ bin/logstash -f code/filter/ruby/example1.conf`
    * p 155 : `$ bin/logstash -f code/filter/ruby/example2.conf`
    
* elasticsearch
    * p 160 : `$ bin/logstash -f code/filter/elasticsearch/example1.conf`
    * p 164 : `$ bin/logstash -f code/filter/elasticsearch/example2.conf`
    * p 169 : `$ bin/logstash -f code/filter/elasticsearch/example3.conf`
    * p 174 : `$ bin/logstash -f code/filter/elasticsearch/example4.conf`
