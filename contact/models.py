from django.db import models
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm

from wagtailcaptcha.models import WagtailCaptchaEmailForm, WagtailCaptchaForm

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaForm

# Create your models here.


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )
    

class ContactPage(WagtailCaptchaEmailForm):
    template = "contact/contact_page.html"
    subpage_types = []
    parent_page_types = ['home.HomePage']

    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('from_address', classname="col6"),
                        FieldPanel('to_address', classname="col6"),
                    ]
                ),
                FieldPanel('subject'),
            ], "Email Notification Config"
        ),
    ]
    
    
    def get_form_fields(self):
        return self.form_fields.all()
    
    def get_context(self, request):
        from home.models import HomePage
        from home import models
        context = super(ContactPage, self).get_context(request)
        context['home_menu'] = HomePage.objects.live()
        return context
    