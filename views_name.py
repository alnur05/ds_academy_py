from django.http import HttpRequest, HttpResponse

def name(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name = request.POST.get("name", "")
        age = request.POST.get("age", "0")
        return HttpResponse(f"""
        Thank  u, {name}!<br>
        You are {age} years old
        """)
    return  HttpResponse("""
    <form  method="POST">
    <label for="name">What is your name</label>
    <input id="name" name="name" value="Alnur"><br>
    <label for="age" >How old are u?</label>
    <input id="age" name="age" type="number" value="18" style="margin-left:23px;margin-top:15px"><br>
    <button type="submit" style="margin-top:20px; margin-left:24%; background-color: #228B22">Complete</button>
    </form>
    """)

