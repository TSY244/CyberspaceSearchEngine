from django.shortcuts import render
from django.http import JsonResponse
import tools.UseElasticSearch.UseElasticSearch as ES
import configparser

# Create your views here.

# global variable
config = configparser.ConfigParser()
config.read("config.ini")
es_host = config.get("es", "host")
es_port = config.get("es", "port")
info_index = config.get("es", "info_index")
vuls_index = config.get("es", "vuls_index")


def search_info(request):
    global es_host, es_port, info_index, vuls_index
    if request.method == "GET":
        es = ES.MyElasticSearch(es_host, es_port)
        es.connect()
        query = {}
        for key in request.GET:
            query[key] = request.GET[key]
        if query=={}:
            ret = es.search_data(info_index)
        else:
            ret = es.search_data_by_query(info_index, query)
            
        result = ret["hits"]["hits"]
        for i in range(len(result)):
            result[i] = result[i]["_source"]
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "method not allowed"}, status=405)
