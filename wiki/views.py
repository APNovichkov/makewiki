from django.shortcuts import render, get_object_or_404
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    """Class Based view that extends from ListView and returns a list of all pages."""

    model = Page
    template_name = "wiki/page_list.html"
    context_object_name = "all_pages_list"

    # def get_queryset(self):
    #     return Page.objects.all()

class PageDetailView(DetailView):
    """
    Show page.html template on GET given a slug.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """

    model = Page
    template_name = "wiki/page.html"
    context_object_name = "page"

    def post(self, request, slug):
        pass
