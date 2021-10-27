from wagtail.core import hooks
from django.shortcuts import redirect
from django.http import HttpResponse
from wagtail.core import hooks



from django.shortcuts import redirect

# @hooks.register('before_serve_document')
# def serve_document(document, request):
#     # eg. use document.file_extension, document.url, document.filename
#     if document.file_extension == 'pdf':
#         google_view_pdf_base = 'https://docs.google.com/viewer?url='
#         # document.url is a relative URL so more work needed here
#         # also URL should probably be URL encoded
#         redirect_url = google_view_pdf_base + document.url
#         # must return an instance of HTTPResponse
#         return redirect(redirect_url)
#     # no return means the normal page serve will operate

@hooks.register('before_serve_document')
def serve_document(document, request):
    if document.file_extension != 'pdf':
        return  # Empty return results in the existing response
    response = HttpResponse(document.file.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'filename="' + document.file.name.split('/')[-1] + '"'
    if request.GET.get('download', False) in [True, 'True', 'true']:
        response['Content-Disposition'] = 'attachment; ' + response['Content-Disposition']
    return response
