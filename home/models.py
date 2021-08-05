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

class HomePage(Page):
    """This is the landing page for the portfolio"""
    template = "home/home_page.html"
    
    banner_title = models.CharField(max_length=30, blank=False, null=True)
    banner_title_two = models.CharField(max_length=30, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic", "link"], blank = False, null=True)
    photo = ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null = True,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    banner_image = ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null = True,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    banner_cta = ForeignKey(
        'wagtailcore.Page',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    
    
    bio = StreamField(
        [
            ("bio_data", blocks.RogersBio()),
        ],
        null = True,
        blank = False,
    )
    
    persoanl_data = StreamField(
        [
            ("personal_data_info", blocks.PersonalData()),
        ],
        null=True,
        blank = False,
    )
    
    
    records = StreamField(
        [
            ("record_data", blocks.RecordsData()),
        ],
        null = True,
        blank = True,
    )
    
    service = StreamField(
        [
            ("myservice", blocks.MyServices()),
        ],
        null = True,
        blank = True,
    )
    
    price_plan = StreamField(
        [
            ("plans", blocks.PricePlan()),
        ],
        null = True,
        blank = True,
    )
    
    
    recommend = StreamField(
        [
            ("Recommendations", blocks.Recommendations())
        ],
        null = True,
        blank = True,
    )
    
    organisations_logo = StreamField(
        [
            ("Organisations", blocks.Organisations())
        ],
        null=True,
        blank=True,
    )
    
    """Register fields in field Panels"""
    banner_panel = [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_title_two"),
                ImageChooserPanel("photo"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading = "Home Page Banner",
        ),
    ]
    
    bio_panel  = [
        MultiFieldPanel(
            [
                StreamFieldPanel("bio"),
            ],
            heading = "Rogers Bio-Info",
        ),
    ]
    
    persoanl_data_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("persoanl_data"),
            ],
            heading = "Personal Info",
        ),
    ]
    
    records_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("records"),
            ],
            heading = "Records",
        ),
    ]
    
    service_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("service")
            ],
            heading = "My Services",
        ),
    ]
    
    price_plan_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("price_plan")
            ],
            heading = "Price Plan"
        ),
    ]
    recommend_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("recommend"),
            ],
            heading = "Recommendations"
        ),
    ]
    
    organisations_logo_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("organisations_logo"),
            ],
            heading = "Org Logo",
        ),
    ]
    
    
    """REgister in a TabbedInterface"""
    edit_handler = TabbedInterface (
        [
            ObjectList(banner_panel, heading = "Banner Settings"),
            ObjectList(bio_panel, heading = "Bio"),
            ObjectList(persoanl_data_panel, heading = "Personal Info"),
            ObjectList(records_panel, heading = "Records"),
            ObjectList(service_panel, heading = "Services"),
            ObjectList(price_plan_panel, heading="Price Plans"),
            ObjectList(recommend_panel, heading = "Recommendation"),
            ObjectList(organisations_logo_panel, heading = "Org"),
            ObjectList(Page.settings_panels, heading = "Settings"),
            ObjectList(Page.promote_panels, heading = "Promotion")
        ]
    )
    
    class Meta: #noqa
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
        
    def get_admin_display_title(self):
        return "Kuyeso Rogers Goodman Dashboard"
        
        
