# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0015_auto_20181025_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('cardinality_hash', models.TextField(db_index=True, null=True)),
                ('first_effective_date', models.DateTimeField(null=True)),
                ('last_effective_date', models.DateTimeField(null=True)),
                ('credential_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credential_sets', to='api_v2.CredentialType')),
            ],
            options={
                'db_table': 'credential_set',
            },
        ),
        migrations.AddField(
            model_name='credential',
            name='latest',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='credential',
            name='revoked_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api_v2.Credential'),
        ),
        migrations.AddField(
            model_name='credential',
            name='revoked_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='credentialset',
            name='latest_credential',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api_v2.Credential'),
        ),
        migrations.AddField(
            model_name='credentialset',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credential_sets', to='api_v2.Topic'),
        ),
        migrations.AddField(
            model_name='credential',
            name='credential_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to='api_v2.CredentialSet'),
        ),
        migrations.AlterUniqueTogether(
            name='credentialset',
            unique_together=set([('topic', 'credential_type', 'cardinality_hash')]),
        ),
    ]
