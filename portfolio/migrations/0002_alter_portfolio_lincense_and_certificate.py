# Generated by Django 3.2.6 on 2021-08-05 09:54

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='Lincense_And_Certificate',
            field=wagtail.core.fields.StreamField([('license', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('Lisence_and_Certificate', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('certificate', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('certified_by', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('issued_on', wagtail.core.blocks.DateBlock(required=True)), ('Expiry_Date', wagtail.core.blocks.DateBlock(required=False)), ('No_Expiry', wagtail.core.blocks.CharBlock(required=False)), ('Credential_Id', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('URL', wagtail.core.blocks.URLBlock(required=False))])))]))], null=True),
        ),
    ]