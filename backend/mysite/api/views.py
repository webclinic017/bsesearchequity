from rest_framework.decorators import api_view
from rest_framework.response import Response


import redis


redis_host = "localhost"
redis_port = 6379
redis_password = ""

redis_instance = redis.Redis(host=redis_host,port=redis_port)



@api_view(['GET'])
def query_db(request,**kwargs):


    searchinput = request.GET.get("name")

    if searchinput!=None:

        alldatafromdb = redis_instance.keys('*'+searchinput.upper()+'*')

        alloutputs = []
        count = 0
        for every in alldatafromdb:

                dict = {}
                try:
                   output_from_redis = redis_instance.hmget(every,"open","high","low","close")
                except Exception as e :
                    print("Exception"+"-"+str(e))

                dict["keyname"] = every
                dict["open"] = output_from_redis[0]
                dict["high"] = output_from_redis[1]
                dict["low"] = output_from_redis[2]
                dict["close"] = output_from_redis[3]

                count = count+1
                alloutputs.append(dict)



        return Response({ 'outputfromdb' : alloutputs}, status=200)


    return True