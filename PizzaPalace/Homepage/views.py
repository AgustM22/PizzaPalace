from django.shortcuts import render

def main(request):
    """
    Displays the homepage.
    """
    return render(request, "Homepage.html")
