# Generated by Django 3.2.6 on 2021-08-08 19:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(max_length=230, null=True)),
                ('academic', wagtail.core.fields.StreamField([('mydoc', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=15, required=True)), ('mydoc', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('institution', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('course', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('year', wagtail.core.blocks.DateBlock(max_length=10, required=True)), ('doc', wagtail.documents.blocks.DocumentChooserBlock(required=True))])))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Academic Page',
                'verbose_name_plural': 'Acaademic Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]