from django.db import models

# Create your models here.
from streams import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    MultiFieldPanel,
    TabbedInterface,
    ObjectList
)

class PortFolioPage(Page):
    
    
    Experinces = StreamField(
        [
            ("experinces", blocks.Experience())
        ],
        blank=False,
        null=True,
    )
    
    Educataion = StreamField(
        [
            ("education", blocks.Education())
        ],
        blank=False,
        null=True
    )
    
    Lincense_And_Certificate = StreamField(
        [
            ("license", blocks.LicenseAndCert())
        ],
        blank=False,
        null=True
    )
    
    Skills = StreamField(
        [
            ("skills", blocks.Skills())
        ],
        blank=False,
        null=True,
    )
    
    Accomplishment = StreamField(
        [
            ("accomplishment", blocks.Accomplishement())
        ],
        blank=False,
        null = True,
    ) 
    
    Award = StreamField(
        [
            ("award", blocks.Award())
        ],
        blank=False,
        null = True,
    )
    
    Interests = StreamField(
        [
            ("Interests", blocks.Interests())
        ]
    )
    
    
    
    
    experince_panels = [
        MultiFieldPanel(
            [
                StreamFieldPanel("Experinces")
            ],
            heading = "Experinces",
        ),
    ]
    
    education_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("Educataion")
            ],
            heading = "Education",
        ),
    ]
    
    linces_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("Lincense_And_Certificate")
            ],
            heading = "License And Certificate",
        ),
    ]
    
    
    skills_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("Skills")
            ],
            heading = "Skills",
        ),
    ]
    
    accom_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("Accomplishment")
            ],
            heading = "Accomplishment",
        ),
    ]
    
    award_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("Award")
            ],
            heading = "Award",
        ),
    ]
    
    interest_panel = [
        MultiFieldPanel(
            [
                StreamFieldPanel("Interests")
            ],
            heading = "Interests",
        ),
    ]
    
    edit_handler = TabbedInterface(
        [
            ObjectList(experince_panels, heading = "Experience"),
            ObjectList(education_panel, heading = "Education"),
            ObjectList(linces_panel, heading = "License"),
            ObjectList(skills_panel, heading = "Skills"),
            ObjectList(accom_panel, heading = "Accomplishemnt"),
            ObjectList(award_panel, heading = "Award"),
            ObjectList(interest_panel, heading = "Interest")
        ]
    )
    
    
    