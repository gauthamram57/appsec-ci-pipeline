from django.shortcuts import render

def home(request):

    context = {
        "project_name": "AppSec CI Pipeline",
        "hero_title": "Secure Code Before Deployment",
        "hero_description": "Automated Application Security Pipeline integrating Semgrep, Trivy and OWASP ZAP through GitHub Actions.",
        "sast_tool": "Semgrep",
        "sca_tool": "Trivy",
        "dast_tool": "OWASP ZAP",
    }

    return render(request, "home.html", context)

def search(request):

    query = request.GET.get("q", "")

    return render(
        request,
        "search.html",
        {"query": query}
    )
from .models import Comment


def comments(request):

    if request.method == "POST":

        username = request.POST.get("username")

        message = request.POST.get("message")

        Comment.objects.create(
            username=username,
            message=message
        )

    all_comments = Comment.objects.all().order_by("-created_at")

    return render(
        request,
        "comments.html",
        {
            "comments": all_comments
        }
    )