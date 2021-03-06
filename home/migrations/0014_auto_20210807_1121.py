# Generated by Django 3.2.6 on 2021-08-07 11:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_homepage_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='price_plan',
            field=wagtail.core.fields.StreamField([('plans', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=15, required=True)), ('plans', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('pan_type', wagtail.core.blocks.CharBlock(required=True)), ('pan_subtitle', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('item_name', wagtail.core.blocks.CharBlock(required=True)), ('offered', wagtail.core.blocks.BooleanBlock(required=True))]))), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=True))])))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='service',
            field=wagtail.core.fields.StreamField([('myservice', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=20, required=True)), ('my_services', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('service', wagtail.core.blocks.CharBlock(max_length=30, required=True)), ('description', wagtail.core.blocks.CharBlock(max_length=150, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))]))], blank=True, null=True),
        ),
    ]
