from django.http import HttpResponse,JsonResponse
import json
def check_response(req):
    print(req.META)
    print(req.body)
    data=json.loads(req.body)
    print(data)
    return JsonResponse(
        {
            
        }
    )