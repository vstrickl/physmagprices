"""This module renders UI view for app."""
# pylint: disable=no-member
from django.shortcuts import render

from .models import UploadFile

# Create your views here.=
def prices(request):
    """This function renders the Offers Document to the home page."""
    header = "PhysMag Prices"

    # Fetch all uploaded files
    uploaded_files = UploadFile.objects.all()

    context = {
        'header':header,
        'uploaded_files': uploaded_files,
    }

    return render(request, 'prices.html', context)
