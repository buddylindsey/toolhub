# Generated by Django 2.1.1 on 2018-10-17 00:59

from django.db import migrations, models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20181012_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertool',
            name='clearance',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Available to all'), (1, 'Owner cleared users only'), (2, 'Cleared users can approve anyone')], default=0, help_text='Who is allowed to use this tool', verbose_name='Clearance'),
        ),
        migrations.AlterField(
            model_name='usertool',
            name='state',
            field=models.CharField(choices=[('none', 'None'), ('available', 'Available'), ('in_use', 'In Use'), ('disabled', 'Disabled')], default='none', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='usertool',
            name='taxonomies',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=False, help_text='Enter a comma-separated tag string', related_name='tools', space_delimiter=False, to='tools.ToolTaxonomy', tree=True),
        ),
        migrations.AlterField(
            model_name='usertool',
            name='visibility',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Private'), (1, 'Cleared Users'), (2, 'Public')], default=2, help_text='The level of user visibility for this tool', verbose_name='Visibility'),
        ),
    ]
