from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
# Create your views here.
def say_hello(request):
    x = 1
    y = 2
    user_name = chr(np.random.randint(65,90)) + "".join([chr(np.random.randint(97,122)) for i in range(np.random.randint(5,9))])
    return render(request, "hello.html", {"name": str(user_name)})
