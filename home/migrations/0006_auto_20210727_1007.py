# Generated by Django 3.2.5 on 2021-07-27 10:07

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210727_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='organi',
            field=wagtail.core.fields.StreamField([('Organisations', wagtail.core.blocks.StructBlock([('org', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=True))])))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='recommend',
            field=wagtail.core.fields.StreamField([('Recommendations', wagtail.core.blocks.StructBlock([('recommendations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('Name', wagtail.core.blocks.CharBlock(max_length=45, required=True)), ('Job_Title', wagtail.core.blocks.CharBlock(max_length=45, required=True)), ('Photo', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Stament', wagtail.core.blocks.CharBlock(max_length=45, required=True)), ('star', wagtail.core.blocks.CharBlock(max_length=5, required=True))])))]))], blank=True, null=True),
        ),
    ]
