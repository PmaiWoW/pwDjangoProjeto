from django.db import models

# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    birth_date = models.DateField()
    phone_number = models.IntegerField()
    email = models.EmailField()

    def emailToString(self):
        return str(self.email)

    def __str__(self):
        id = self.email
        return id.lower()


class Message(models.Model):
    subject = models.CharField(max_length=80, default="No Subject")
    message = models.TextField(max_length=858)
    agentID = models.ForeignKey(Agent,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=False,
                                related_name="AgentID")

    def __str__(self):
        return self.subject


class Quiz(models.Model):
    FAMILY_GAME_DEV = (
        ("NINTENDO", "Nintendo"),
        ("ROCKSTAR GAMES", "Rockstar Games"),
        ("ID SOFTWARE", "id Software"),
        ("UBISOFT", "Ubisoft")
    )

    AC_DEV = (
        ("ROCKSTAR GAMES", "Rockstar Games"),
        ("CLOUD IMPERIUM GAMES", "Cloud Imperium Games"),
        ("LARIAN STUDIOS", "Larian Studios"),
        ("UBISOFT", "Ubisoft")
    )

    POKE_YELLOW_RELEASE = (
        ("1965", "1965"),
        ("1972", "1972"),
        ("2004", "2004"),
        ("2017", "2017"),
        ("1998", "1998")
    )

    POKE_YELLOW_DEV = (
        ("NINTENDO", "Nintendo"),
        ("SEGA", "Sega"),
        ("GAME FREAK", "Game Freak"),
        ("BUNGIE", "Bungie")
    )

    MOST_SOLD_GAME = (
        ("GRAND THEFT AUTO V", "Grand Theft Auto V"),
        ("MINECRAFT", "Minecraft"),
        ("NEED FOR SPEED PAYBACK", "Need For Speed Payback"),
        ("DYING LIGHT", "Dying Light")
    )

    MOST_SOLD_CONSOLE = (
        ("XBOX 360", "XBox 360"),
        ("PLAYSTATION 4", "PlayStation 4"),
        ("XBOX SERIES X", "XBox Series X"),
        ("NINTENDO WII", "Nintendo Wii"),
        ("PLAYSTATION 2", "PlayStation 2"),
        ("GAME BOY COLOR", "Game Boy Color")
    )

    FIRST_COMMERCIAL_GAME = (
        ("MINECRAFT", "Minecraft"),
        ("PAC-MAN", "Pac-Man"),
        ("PONG", "Pong"),
        ("RESIDENT EVIL", "Resident Evil")
    )

    PS1_MOST_SOLD_GAME = (
        ("TEKKEN 3", "Tekken 3"),
        ("GRAN TURISMO", "Gran Turismo"),
        ("TOMB RAIDER", "Tomb Raider")
    )

    MOST_POP_ARCADE = (
        ("PAC-MAN", "Pac-Man"),
        ("SPACE INVADERS", "Space Invaders"),
        ("DONKEY KONG", "Donkey Kong")
    )

    MINECRAFT_CHAR_NAME = (
        ("ALLEN", "Allen"),
        ("HORATIO", "Horatio"),
        ("STEVE", "Steve"),
        ("BARRY", "Barry")
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    most_popular_family_games_developer = models.TextField(choices=FAMILY_GAME_DEV)
    assassins_Creed_franchise_developer = models.TextField(choices=AC_DEV)
    pokemon_Yellow_release_year = models.TextField(choices=POKE_YELLOW_RELEASE)
    pokemon_Yellow_developer = models.TextField(choices=POKE_YELLOW_DEV)
    most_sold_game_of_all_time = models.TextField(choices=MOST_SOLD_GAME)
    most_sold_console_of_all_time = models.TextField(choices=MOST_SOLD_CONSOLE)
    first_commercial_game = models.TextField(choices=FIRST_COMMERCIAL_GAME)
    most_sold_game_on_PlayStation_1 = models.TextField(choices=PS1_MOST_SOLD_GAME)
    most_popular_arcade_game = models.TextField(choices=MOST_POP_ARCADE)
    name_of_the_first_main_character_from_Minecraft = models.TextField(choices=MINECRAFT_CHAR_NAME)

    correctAnswers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    name = models.CharField(max_length=80)
    comment = models.TextField(max_length=600)

    def __str__(self):
        return self.name
