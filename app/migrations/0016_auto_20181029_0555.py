# Generated by Django 2.0.7 on 2018-10-29 05:55

import django.db.models.deletion
from django.db import migrations, models


def add_game_to_missions_and_announcements(apps, schema_editor):
    Game = apps.get_model('app', 'Game')
    MissionPage = apps.get_model('app', 'MissionPage')
    AnnouncementPage = apps.get_model('app', 'AnnouncementPage')

    game = Game.objects.all().order_by('created_at').first()
    for mission in MissionPage.objects.filter(game='908d7ce7-b9b6-4c09-badd-386c3cb13bbd'):
        mission.game = game
        mission.save()

    for announcement in AnnouncementPage.objects.filter(game='908d7ce7-b9b6-4c09-badd-386c3cb13bbd'):
        announcement.game = game
        announcement.save()


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0015_auto_20181027_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcementpage',
            name='game',
            field=models.ForeignKey(default='908d7ce7-b9b6-4c09-badd-386c3cb13bbd',
                                    on_delete=django.db.models.deletion.PROTECT, to='app.Game'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='missionpage',
            name='game',
            field=models.ForeignKey(default='908d7ce7-b9b6-4c09-badd-386c3cb13bbd',
                                    on_delete=django.db.models.deletion.PROTECT, to='app.Game'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplycode',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(
            code=add_game_to_missions_and_announcements,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
