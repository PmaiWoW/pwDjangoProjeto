# Generated by Django 3.2.3 on 2021-06-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210604_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('familyGameDev', models.TextField(choices=[('NINTENDO', 'Nintendo'), ('ROCKSTAR GAMES', 'Rockstar Games'), ('ID SOFTWARE', 'id Software')])),
                ('acDev', models.TextField(choices=[('ROCKSTAR GAMES', 'Rockstar Games'), ('CLOUD IMPERIUM GAMES', 'Cloud Imperium Games'), ('LARIAN STUDIOS', 'Larian Studios'), ('UBISOFT', 'Ubisoft')])),
                ('pokeYellowRelease', models.TextField(choices=[('1965', '1965'), ('1972', '1972'), ('2004', '2004'), ('2017', '2017'), ('1998', '1998')])),
                ('pokeYellowDev', models.TextField(choices=[('NINTENDO', 'Nintendo'), ('SEGA', 'Sega'), ('GAME FREAK', 'Game Freak'), ('BUNGIE', 'Bungie')])),
                ('mostSoldGame', models.TextField(choices=[('GRAND THEFT AUTO V', 'Grand Theft Auto V'), ('MINECRAFT', 'Minecraft'), ('NEED FOR SPEED PAYBACK', 'Need For Speed Payback'), ('DYING LIGHT', 'Dying Light')])),
                ('mostSoldConsole', models.TextField(choices=[('XBOX 360', 'XBox 360'), ('PLAYSTATION 4', 'PlayStation 4'), ('XBOX SERIES X', 'XBox Series X'), ('NINTENDO WII', 'Nintendo Wii'), ('PLAYSTATION 2', 'PlayStation 2'), ('GAME BOY COLOR', 'Game Boy Color')])),
                ('firstCommercialGame', models.TextField(choices=[('MINECRAFT', 'Minecraft'), ('PAC-MAN', 'Pac-Man'), ('PONG', 'Pong'), ('RESIDENT EVIL', 'Resident Evil')])),
                ('ps1MostSoldGame', models.TextField(choices=[('TEKKEN 3', 'Tekken 3'), ('GRAN TURISMO', 'Gran Turismo'), ('TOMB RAIDER', 'Tomb Raider')])),
                ('mostPopArcade', models.TextField(choices=[('PAC-MAN', 'Pac-Man'), ('SPACE INVADERS', 'Space Invaders'), ('DONKEY KONG', 'Donkey Kong')])),
                ('minecraftCharName', models.TextField(choices=[('ALLEN', 'Allen'), ('HORATIO', 'Horatio'), ('STEVE', 'Steve'), ('BARRY', 'Barry')])),
                ('correctAnswers', models.IntegerField(default=0)),
            ],
        ),
    ]