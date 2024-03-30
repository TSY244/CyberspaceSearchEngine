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

info_parameters=["site","port","area","tide","vuls"]
vuls_parameters=["site","prt_name","vul_type","vul_numb"]

def search_info(request):
    global es_host, es_port, info_index, vuls_index
    if request.method == "GET":
        es = ES.MyElasticSearch(es_host, es_port)
        es.connect()
        body = {
            "query": {
                "bool": {
                "should": [
                ],
                "minimum_should_match": 1
                }
            }
        }

        get_request = request.GET
        if "site" in get_request:
            body["query"]["bool"]["should"].append({"term": {"site": get_request["site"]}})
        if "ports" in get_request:
            for port in get_request["ports"].split(","):
                body["query"]["bool"]["should"].append({"term": {"ports": int(port)}})
        if "area" in get_request:
            for area in get_request["area"].split(","):
                body["query"]["bool"]["should"].append({"term": {"area": area}})
        if "tide" in get_request:
            for tide in get_request["tide"].split(","):
                body["query"]["bool"]["should"].append({"term": {"tide": tide}})
        if "vuls" in get_request:
            for vul in get_request["vuls"].split(","):
                body["query"]["bool"]["should"].append({"term": {"vuls": vul}})

        ret=es.search_data_by_body(info_index, body=body)
        result = ret["hits"]["hits"]
        for i in range(len(result)):
            result[i] = result[i]["_source"]
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "method not allowed"}, status=405)

def search_vuls(request):
    if request.method == "GET":
        es = ES.MyElasticSearch(es_host, es_port)
        es.connect()
        body = {
            "query": {
                "bool": {
                "should": [
                ],
                "minimum_should_match": 1
                }
            }
        }

        get_request = request.GET
        if "site" in get_request:
            body["query"]["bool"]["should"].append({"term": {"site": get_request["site"]}})
        if "prt_name" in get_request:
            prt_name = get_request["prt_name"][1:-1]
            body["query"]["bool"]["should"].append({"term": {"prt_name.keyword": prt_name}})
        if "vul_type" in get_request:
            vul_type = get_request["vul_type"][1:-1]
            body["query"]["bool"]["should"].append({"term": {"vul_type.keyword": vul_type}})
        if "vul_numb" in get_request:
            vul_numb = get_request["vul_numb"][1:-1]
            body["query"]["bool"]["should"].append({"term": {"vul_numb.keyword": vul_numb}})

        ret=es.search_data_by_body(vuls_index, body=body)
        result = ret["hits"]["hits"]
        for i in range(len(result)):
            result[i] = result[i]["_source"]
        return JsonResponse(result, safe=False)