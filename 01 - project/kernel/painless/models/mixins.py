from django.db import models
from django.http import JsonResponse

class TimeStampedMixin(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class OrganizedMixin(TimeStampedMixin):
    title = models.CharField(max_length= 128, unique = True)
    slug = models.CharField(max_length = 128, unique = True)

    class Meta:
        abstract = True


class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

        def form_valid(self, form):
            response = super(AjaxFormMixin, self).form_valid(form)
            if self.request.is_ajax():
                print(form.cleaned_data)
                data = {
                    'message': "Successfully submit form data."
                }
                return JsonResponse(data)
            else:
                return response
