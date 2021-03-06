# Generated by Django 3.2.3 on 2021-06-30 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='acDev',
            new_name='assassins_Creed_franchise_developer',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='firstCommercialGame',
            new_name='first_commercial_game',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='mostPopArcade',
            new_name='most_popular_arcade_game',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='familyGameDev',
            new_name='most_popular_family_games_developer',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='mostSoldConsole',
            new_name='most_sold_console_of_all_time',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='mostSoldGame',
            new_name='most_sold_game_of_all_time',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='ps1MostSoldGame',
            new_name='most_sold_game_on_PlayStation_1',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='minecraftCharName',
            new_name='name_of_the_first_main_character_from_Minecraft',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='pokeYellowDev',
            new_name='pokémon_Yellow_developer',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='pokeYellowRelease',
            new_name='pokémon_Yellow_release_year',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='firstName',
            new_name='primeiro_nome',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='lastName',
            new_name='último_nome',
        ),
    ]
