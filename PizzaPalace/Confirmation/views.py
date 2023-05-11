from django.shortcuts import render

def main(request):
    """
    Renders the confirmation page.
    """
    return render(request, "Confirmation.html")
