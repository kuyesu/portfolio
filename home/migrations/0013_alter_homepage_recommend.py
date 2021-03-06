# Generated by Django 3.2.6 on 2021-08-06 10:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_records_homepage_my_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='recommend',
            field=wagtail.core.fields.StreamField([('Recommendations', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=20, required=True)), ('recommendations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('Name', wagtail.core.blocks.CharBlock(max_length=45, required=True)), ('Job_Title', wagtail.core.blocks.CharBlock(max_length=45, required=True)), ('Photo', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Stament', wagtail.core.blocks.CharBlock(max_length=45, required=True)), ('star', wagtail.core.blocks.IntegerBlock(max_value=5))])))]))], blank=True, null=True),
        ),
    ]
