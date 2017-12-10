curl -XGET "http://13.125.21.52:9200/shopping/_search" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "query": {
    "range": {
      "판매자평점": {
        "gte": 2,
        "lte": 4
      }
    }
  },
  "aggs": {
    "avg_item": {
      "avg": {
        "field": "상품개수"
      }
    }
  }
}'
