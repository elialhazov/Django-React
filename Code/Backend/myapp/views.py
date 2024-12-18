from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import json
from .models import Color, Calculation
from .serializers import ColorSerializer

@csrf_exempt
def add_numbers(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            num1 = int(data.get("num1", 0))
            num2 = int(data.get("num2", 0))
            result = num1 + num2

            calculation = Calculation.objects.create(num1=num1, num2=num2, result=result)

            return JsonResponse({
                "num1": num1,
                "num2": num2,
                "result": result,
                "id": calculation.id,
            })
        except (ValueError, KeyError, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid data"}, status=400)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)


class GenerateNewColor(APIView):
    def get(self, request):

        color_name = f"Color {random.randint(1000, 9999)}"
        hex_value = f"#{random.randint(0, 0xFFFFFF):06x}"
        color = Color.objects.create(name=color_name, hex_value=hex_value)
        serializer = ColorSerializer(color)
        return Response(serializer.data)


def home_view(request):
    return HttpResponse(
        "<h1>Welcome to the API Server</h1>"
        "<p>Navigate to:</p>"
        "<ul>"
        "<li><a href='/colors/generate-new-color'>Color Generator</a></li>"
        "<li><a href='/add-numbers/'>Add Numbers API (POST only)</a></li>"
        "</ul>"
    )
