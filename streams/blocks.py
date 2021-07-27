from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock



class RogersBio(blocks.StructBlock):

    first_name = blocks.CharBlock(required=True, help_text = "First Name")
    last_name = blocks.CharBlock(required=True, help_text = "Last Name")
    bio_image = ImageChooserBlock(required=True)
    
    role = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("role", blocks.StructBlock(required=True, max_length=20)),
            ]
        )
    )
    class Meta:
        template = "streams/rogers_bio.html"
        icon = "user"
        label = "Bio Data"
    
    
    
class PersonalData(blocks.StructBlock):
    
    data = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("residence", blocks.CharBlock(required=True, max_length=15)),
                ("city", blocks.CharBlock(required=True, max_length=15)),
                ("age", blocks.CharBlock(required=True, max_length=2)),
            ]
        )
    )
    
    language = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("lang", blocks.CharBlock(required=True, max_length=15)),
            ]
        )
    )
    
    programming = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("programming_language", blocks.CharBlock(required=True, max_length=20)),
            ]
        )
    )
    class Meta:
        template = "streams/personal_data.html"
        icon = ""
        label = "Personal Info"
    
    
class RecordsData(blocks.StructBlock):
    records = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("record", blocks.CharBlock(required=True, max_length=20)),
                ("period", blocks.CharBlock(required=True, max_length=3)),
            ]
        )
    )
    class Meta:
        template = "streams/record_data.html"
        icon = "edit"
        label = "My Records"
        

class MyServices(blocks.StructBlock):
    
    title = blocks.CharBlock(required=True, max_length=20)
    
    my_services = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("service", blocks.CharBlock(required=True, max_length=30)),
                ("descript", blocks.CharBlock(required = True, max_length=150)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta:
        template = "streams/my_service.html"
        icon = "edit"
        label= "My services"
        

class PricePlan(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=15)
    
    plans = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("pan_type", blocks.CharBlock(required=True)),
                ("pan_subtitle", blocks.ListBlock(
                    blocks.StructBlock(
                        [
                            ("item_name", blocks.CharBlock(required=True))
                        ]))),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=True,
                    )
                ),
            ]
        )
    )
    
    class Meta:
        template = "streams/price_plan.html"
        icon = "edit"
        label = "Price Plan"
        

class Recommendations(blocks.StructBlock):
    
    recommendations = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("Name", blocks.CharBlock(required=True, max_length=45)),
                ("Job_Title", blocks.CharBlock(required=True, max_length=45)),
                ("Photo", ImageChooserBlock(required=True)),
                ("Stament", blocks.CharBlock(required=True, max_length=45)),
                ("star", blocks.CharBlock(required=True, max_length=5))
            ]
        )
    )
    class Meta:
        template = "streams/recommendations.html"
        icon = "edit"
        label = "Price Plan"
        
        
class Organisations(blocks.StructBlock):
    
    organisation = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("Photo", ImageChooserBlock(required=True)),
            ]
        )
    )
    class Meta:
        template = "streams/org.html"
        icon = "edit"
        label = "Organisation Logo"