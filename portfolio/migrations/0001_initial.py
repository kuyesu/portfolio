# Generated by Django 3.2.6 on 2021-08-02 14:07

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortFolio',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('Experinces', wagtail.core.fields.StreamField([('experinces', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('experience', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('role', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('company', wagtail.core.blocks.CharBlock(max_length=70, required=True)), ('job_description', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('year', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('location', wagtail.core.blocks.CharBlock(max_length=50, required=True))])))]))], null=True)),
                ('Educataion', wagtail.core.fields.StreamField([('education', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('education', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('institution', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('course', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('year', wagtail.core.blocks.CharBlock(max_length=10, required=True))])))]))], null=True)),
                ('Lincense_And_Certificate', wagtail.core.fields.StreamField([('license', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('lisenceandcert', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('certificate', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('certified_by', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('issued_on', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('Expiry_Date', wagtail.core.blocks.DateBlock(required=False)), ('No_Expiry', wagtail.core.blocks.CharBlock(required=False)), ('Credential_Id', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('URL', wagtail.core.blocks.URLBlock(required=False))])))]))], null=True)),
                ('Skills', wagtail.core.fields.StreamField([('skills', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('skills', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('skills', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('level', wagtail.core.blocks.CharBlock(max_length=100, required=True))])))]))], null=True)),
                ('Accomplishment', wagtail.core.fields.StreamField([('accomplishment', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('Accomplishments', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('project', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('date', wagtail.core.blocks.DateBlock(required=True)), ('detail', wagtail.core.blocks.CharBlock(max_length=100, required=True))])))]))], null=True)),
                ('Award', wagtail.core.fields.StreamField([('award', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('award', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('project', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('date', wagtail.core.blocks.DateBlock(required=True)), ('detail', wagtail.core.blocks.CharBlock(max_length=100, required=True))])))]))], null=True)),
                ('Interests', wagtail.core.fields.StreamField([('Interests', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('Interests', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('interes', wagtail.core.blocks.CharBlock(max_length=100, required=True))])))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
