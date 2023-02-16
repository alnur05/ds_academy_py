import random

from django.http import HttpRequest, HttpResponse


def show_weather(request: HttpRequest) -> HttpResponse:
    tempereture = random.randint(-40, 40)
    feel = "OK"
    if tempereture > 20:
        feel  = "Hot"
    if tempereture < 0:
        feel = "cold"
    if tempereture < -10:
        feel = "terribly cold"
    return HttpResponse(f"Today: {tempereture} grad celcius, it is {feel}!")