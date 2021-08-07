# Generated by Django 3.2.6 on 2021-08-07 12:25

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_homepage_price_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='price_plan',
            field=wagtail.core.fields.StreamField([('plans', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=15, required=True)), ('plans', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('pan_type', wagtail.core.blocks.CharBlock(required=True)), ('price', wagtail.core.blocks.CharBlock(required=True)), ('popular', wagtail.core.blocks.BooleanBlock(required=False)), ('working_rate', wagtail.core.blocks.ChoiceBlock(choices=[('h', 'h'), ('m', 'm'), ('', '')], required=False)), ('currency', wagtail.core.blocks.ChoiceBlock(choices=[('shs', 'shs'), ('$', '$'), ('', '')], required=False)), ('sup', wagtail.core.blocks.ChoiceBlock(choices=[('*', '*'), ('', '')], required=False)), ('pan_subtitle', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('item_name', wagtail.core.blocks.CharBlock(required=True)), ('offered', wagtail.core.blocks.BooleanBlock(required=False))]))), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
