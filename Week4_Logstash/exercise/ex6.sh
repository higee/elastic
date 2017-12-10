curl -XGET "http://13.125.21.52:9200/shopping/_search" -H 'Content-Type: application/json' -d'
{
  "size":0,
  "query": {
    "terms": {
      "구매사이트": [
        "11번가",
        "옥션"
      ]
    }
  },
  "aggs": {
    "avg_age": {
      "avg": {
        "field": "고객나이"
      }
    }
  }
}'
