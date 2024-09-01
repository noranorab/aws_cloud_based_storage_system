from django.shortcuts import HttpResponse, render
from django.http import JsonResponse

import boto3

access_key_id=''
secret_access_key=''
s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

def home(request):
    if request.method == "POST":

        myfile = request.FILES['myfile']
        print(myfile.name)
        response = s3.put_object(
            Body=myfile,
            Bucket='mystorage-01-09-2024',
            Key=myfile.name,
        )

        return HttpResponse("upload successful")


    return render(request, 'home.html')

def getFiles(request):

    response = s3.list_objects(
        Bucket='mystorage-01-09-2024'
    )

    return JsonResponse(response["contents"], safe=False)

