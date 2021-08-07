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
                ("my_role", blocks.CharBlock(required=True, max_length=20)),
                ("email", blocks.EmailBlock(required=True))
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
                ("age", blocks.IntegerBlock(max_value=20)),
            ]
        )
    )
    
    language = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("language", blocks.CharBlock(required=True, max_length=15)),
                ("rating", blocks.IntegerBlock(max_value=100)),
            ]
        )
    )
    
    programming = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("programming_language", blocks.CharBlock(required=True, max_length=20)),
                ("rating", blocks.IntegerBlock(max_value=100)),
            ]
        )
    )
    
    framework = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("my_framework", blocks.CharBlock(required=True, max_length=20)),
                ("rating", blocks.IntegerBlock(max_value=100)),
            ]
        )
    )
    
    additional_skills = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("addtional_skils", blocks.CharBlock(required=True, max_length=20))
            ]
        )
    )
    
    
    # @todo download
    class Meta:
        template = "streams/personal_data.html"
        icon = "user"
        label = "Personal Info"
    
    
class RecordsData(blocks.StructBlock):
    records = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("record", blocks.CharBlock(required=True, max_length=20)),
                ("period", blocks.IntegerBlock(max_value=20)),
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
                ("description", blocks.CharBlock(required = True, max_length=150)),
                ("button_page", blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')),
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
                ("plan_type", blocks.CharBlock(required=True)),
                ("price", blocks.CharBlock(required=True)),
                ("popular", blocks.BooleanBlock(required=False)),
                ("working_rate", blocks.ChoiceBlock(choices=[("h", "h"), ("m", "m"), ("", "")], required=False)),
                ("currency", blocks.ChoiceBlock(choices=[("shs", "shs"), ("$", "$"), ("", "")], required=False)),
                ("sup", blocks.ChoiceBlock(choices=[("*", "*"), ("", "")], required=False)),
                ("free_statement", blocks.CharBlock(required=False)),
                ("plan_items", blocks.ListBlock(
                    blocks.StructBlock(
                        [
                            ("item_name", blocks.CharBlock(required=True)),
                            ("offered", blocks.BooleanBlock(required=False)),
                        ]))),
                ("button_page", blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
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
    title = blocks.CharBlock(required=True, max_length=20)
    
    recommendations = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("Name", blocks.CharBlock(required=True, max_length=45)),
                ("Job_Title", blocks.CharBlock(required=True, max_length=45)),
                ("Photo", ImageChooserBlock(required=True)),
                ("Stament", blocks.CharBlock(required=True, max_length=200)),
                ("star", blocks.IntegerBlock(max_value=5))
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
        
class Experience(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
    
    experience = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("role", blocks.CharBlock(required=True, max_length=60)),
                ("company", blocks.CharBlock(required=True, max_length=70)),
                ("job_description", blocks.CharBlock(required=True, max_length=50)),
                ("year", blocks.CharBlock(required=True, max_length=50)),
                ("location", blocks.CharBlock(required=True, max_length=50)),
            ]
        )
    )
    
    class Meta:
        template = "streams/experience.html"
        icon = "edit"
        label = "Experience"
        
        
class Education(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
    
    education = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("institution", blocks.CharBlock(required=True, max_length=100)),
                ("course", blocks.CharBlock(required=True, max_length=100)),
                ("year", blocks.CharBlock(required=True, max_length=10)),
            ]
        )
    )
    class Meta:
        template = "streams/education.html"
        icon = "edit"
        label = "Education"
        
class LicenseAndCert(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
    
    Lisence_and_Certificate = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("certificate", blocks.CharBlock(required=True, max_length=100)),
                ("certified_by", blocks.CharBlock(required=True, max_length=100)),
                ("issued_on", blocks.DateBlock(required=True)),
                ("Expiry_Date", blocks.DateBlock(required=False)),
                ("No_Expiry", blocks.CharBlock(required=False)),
                ("Credential_Id", blocks.CharBlock(required=True, max_length=100)),
                ("URL", blocks.URLBlock(required=False))
            ]
        )
    )
    
    class Meta:
        template = "streams/licenseandcert.html"
        icon = "edit"
        label = "License and Certificates"
        
        
class Skills(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
     
    skills = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("skills", blocks.CharBlock(required=True, max_length=100)),
                ("level", blocks.CharBlock(required=True, max_length=100)),
            ]
        )
    )
    class Meta:
        template = "streams/skills.html"
        icon = "edit"
        label = "My Skills"


class Accomplishement(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
     
    Accomplishments = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("project", blocks.CharBlock(required=True, max_length=100)),
                ("date", blocks.DateBlock(required=True)),
                ("detail", blocks.CharBlock(required=True, max_length=100))
            ]
        )
    )
    class Meta:
        template = "streams/accomplishment.html"
        icon = "edit"
        label = "Accomplishement"
        
        

class Award(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
     
    award = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("project", blocks.CharBlock(required=True, max_length=100)),
                ("date", blocks.DateBlock(required=True)),
                ("detail", blocks.CharBlock(required=True, max_length=100))
            ]
        )
    )
    class Meta:
        template = "streams/award.html"
        icon = "edit"
        label = "Award"
        

class Interests(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
     
    Interests = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("interes", blocks.CharBlock(required=True, max_length=100)),
                
            ]
        )
    )
    class Meta:
        template = "streams/interest.html"
        icon = "edit"
        label = "Interest"
        
        
