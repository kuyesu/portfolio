from django.db import models
from django.db.models.fields.related import ForeignKey

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    PageChooserPanel,
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
    StreamFieldPanel,
    
)
from streams import blocks
# Create your models here.
class AcademicPage(Page):
    
    template = "academic/academic_page.html"
    subpage_types = []
    parent_page_types = ['home.HomePage']

    
    doc_title = models.CharField(max_length=230, blank=False, null=True)
    subtitle = RichTextField(blank=False, null=True)
    
    
   
    academic = StreamField(
       [
           ("mydoc", blocks.RogersDocuments())
       ],
        null = True,
        blank = True,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("doc_title"),
        FieldPanel("subtitle"),
        StreamFieldPanel("academic")
    ]
   
    # title_panel = [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel("doc_title"),
    #             FieldPanel("subtitle"),
                
    #         ],
    #         heading = "Academics",
    #     ),
    # ]
    
    # academic_panel = [
    #     MultiFieldPanel(
    #         [
    #             StreamFieldPanel("academic"),
                
    #         ],
    #         heading = "Docs Info",
    #     ),
    # ]
    
    
    # edit_handler = TabbedInterface (
    #     [
    #         ObjectList(title_panel, heading = "Title Page"),
    #         ObjectList(academic_panel, heading = "Academic docs"),
    #         ObjectList(Page.settings_panels, heading = "Settings"),
    #         ObjectList(Page.promote_panels, heading = "Promotion")
            
    #     ]
    # )
    
    class Meta: #noqa
        verbose_name = "Academic Page"
        verbose_name_plural = "Acaademic Pages"
        
    def get_admin_display_title(self):
        return "Academic Page"
   
   
    def get_context(self, request):
        from home.models import HomePage
        from home import models
        context = super(AcademicPage, self).get_context(request)
        context['home_menu'] = HomePage.objects.live()
        return context