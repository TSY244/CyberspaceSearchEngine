import elasticsearch
url="http://192.168.79.128:9200"
es=elasticsearch.Elasticsearch([url])
ret=es.search(index="info",query={"match":{"site":"192.168.79.128"}})
result=ret["hits"]["hits"]
print(result)
