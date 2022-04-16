
default isRaining = False
## This, when False, indicates Sunny weather, the default.
## This, when True, indicates Rainy weather.

default rainTime = 100
## This is the length of the weather.
## Can be made longer or shorter by default, but can be extended at any point by adding to it.

default sinceRain = 0
## This tells us if Rain has occured recently.
## Usually, it can be a boolean (True/False), however I find it easier to use integers (Whole Numbers).

default isSnowing = False
## If False, it is not snowing.
## If True, it is snowing.

default areaIsCold = False
## If False, the area is not Cold, which doesn't allow snow.
## If True, the area is Cold, which allowes snow.
## This is not strictly necessary, but it helps with the Weather GUI + Weather Forecast.

default snowTime = 100
## This is the length of the weather.
## Can be made longer or shorter by default, but can be extended at any point by adding to it.

default sinceSnow = 0
## This tells us if Snow has occured recently.

#######################################################################

label start:

    show screen weatherGUI

    menu:
        "Travel":
            jump travelWeather
        "Travel Cold Area":
            jump travelCold
        "Check the weather":
            jump weatherForecast

    return

## This is a placeholder for interactivity on a map or environment.
## Say, you travel to a city on a map from somewhere.
## It does not have to be a menu.

#######################################################################

label travelWeather:

    $ areaIsCold = False

## This labels this area as warm, since the Boolean is set to False. This is mainly for the Weather GUI and
## nothing in-game.

#######################################################################

    if isRaining:

        $ rainTime -= 10

        "You arrived safely, but it seems to be raining."
        "Movement and Agility have been decreased slightly."

        if rainTime == 0:

            $ sinceRain += 1
            $ isRaining = False
            $ rainTime = 100

            "However, just as soon as you arrived, it stopped raining."

## [if isRaining:] checks to see if the Boolean isRaining is True. If it is, it continues down the same code block.
## If it isn't is passes through to the [else:] statement below it.
## [$ rainTime -= 10] removes 10 'seconds' from the rainTime timer. It only removes 'seconds' when the variable is called.
## The text is mostly redundant, it just tells the player what the weather is and any side effects.
## [if rainTime == 0:] checks to see if the rainTime timer has reached 0. If not, it passes.
## However, if it has, it does the following.
## [$ sinceRain += 1] adds 1 to the sinceRain int, telling us that yes, it has just finished raining.*
## [$ isRaining = False] this updates the isRaining boolean to tell us that no, it is no longer raining.
## [$ rainTime = 100] is reset to the default 100 'seconds'.
## The text then indicates to the player that, it was raining, however it no longer is.

## * [sinceRain] can be changed to a boolean. It should still work completely fine.

#######################################################################

    else:

        if not isRaining and sinceRain == 0:

            $ rainChance = renpy.random.randint(1,25)

            if rainChance == 13 or 12 or 11 or 10 and sinceRain == 0:

                $ isRaining = True
                $ rainTime = 100

                "Just as you arrived, it began to rain."
                "You should've seen the oncoming weather clouds, but hey."
                "Movement and Agility have been decreased slightly."

## [if not isRaining and sinceRain == 0:] checks to see if isRaining is False, saying it is no longer raining,
## and if sinceRain is 0, saying that rain is allowed to come.
## If both conditions are met, it continues.
## [$ rainChance = renpy.random.randint(1,25)] is a temporary value. rainChance does not need to be defined by
## a default as it is only used here. It then uses Ren'Py's random integer and finds a random int between 1 & 25.
## This can be adjusted to whatever chance you want rain to have.
## [if rainChance == 13 and sinceRain == 0:] sees if the random number is exactly 13 and checks if rain is allowed.
## If either conditions are not met, it passes. If both are met, it continues.
## [$ isRaining = True] tells us that it is raining.
## [$ rainTime = 100] makes sure that the rainTime timer is 100 'seconds'. This can be removed/changed.
## The dialouge indicates that, it was sunny before, but it is now raining.

#######################################################################

            elif sinceRain == 0:

                "You arrived. The weather seems nice. There do seem to be some oncoming clouds, however."
                "It doesn't look like it should rain anytime soon."

## [elif sinceRain == 0:] makes sure that it is possible for rain to occur, but is only possible if the check
## for the random integer in the last code block was not equal to 13.
## The dialouge tells us that it is still sunny, but there are some clouds, indicating rain is possible.

#######################################################################

            else:
                "The weather seems to be great! No oncoming clouds."

## However, if sinceRain is equal to 1, indicating that rain cannot occur, the dialouge tells us that there is
## no chance for rain at all.

#######################################################################

        else:
            if sinceRain == 1:

                $ allowRain = renpy.random.randint(1,10)

                if allowRain == 9:

                    $ sinceRain = 0

                    "You arrived. The weather seems nice. There do seem to be some clouds rolling in, however."

## This [else] statement comes off of the [if not isRaining and sinceRain == 0:] and is usually triggered if
## sinceRain is equal to 1, or rain is not possible.
## The [if] block checks to see if sinceRain is possible or not. If it is, it passes. If it isn't, it continues.
## [$ allowRain = renpy.random.randint(1,10)] is another temporary value. This allows us to give an opportunity
## to the area to allow rain or not. You can increase/decrease the chance of allowing rain again in said area.
## [if allowRain == 9:] this checks to see if the random integer is equal to exactly 9. If it isn't, it passes.
## If it is, it continues.
## [$ sinceRain = 0] updates the sinceRain counter to allow the chance of rain.
## The dialouge tells the player that, while it is Sunny, there is now chances for rain.

#######################################################################

                else:
                    "The weather seems to be great! No oncoming clouds."

## This check comes off of the [if allowRain == 9:] check. If it fails and the random int is anything but 9,
## it passes to this dialouge, which tells us that the weather is Sunny with no chance of rain.

#######################################################################

            else:
                "You arrived. The weather is Sunny but it is Raining, which is impossible."
    jump start #return

## This can only occur if it is Raining and there is no chance of rain, indicating Sunny weather.
## This is impossible to occur. However, if you do somehow see it, something has gone horribly wrong.
## [return] just sends you back to the main menu. This can be a [jump] clause, or anything else.
## This just indicates the end of the weather forecast.

#######################################################################
###########################  WEATHER: SNOW  ###########################
#######################################################################

## Here is a full code block for a weather pattern to help you grasp it easier, as it may be confusing too see the
## comments + code within the rain pattern. There will be no more comments in this section. However,
## [$ areaIsCold = True] only helps with the Weather GUI at the bottom of the page. This whole code block is the same
## as the rain block, just not broken up and added one value.

label travelCold:

    $ areaIsCold = True

    if isSnowing:

        $ snowTime -= 10

        "You arrived safely, but it seems to be snowing."
        "Movement and Agility have been decreased heavily."

        if snowTime == 0:

            $ sinceSnow += 1
            $ isSnowing = False
            $ snowTime = 100

            "However, just as soon as you arrived, it stopped snowing."
            "Movement and Agility no longer impacted."

    else:

        if not isSnowing and sinceSnow == 0:

            $ snowChance = renpy.random.randint(1,25)

            if snowChance == 13 or 12 or 11 or 10 and sinceSnow == 0:

                $ isSnowing = True
                $ snowTime = 100

                "Just as you arrived, it began to snow."
                "You should've felt the oncoming cold, but hey."
                "Movement and Agility have been decreased heavily."

            elif sinceSnow == 0:

                "You arrived. The weather seems nice, but cold. There do seem to be some oncoming clouds, however."
                "It doesn't look like it should snow anytime soon."

            else:
                "The weather seems to be great! No oncoming clouds."
        
        else:
            if sinceSnow == 1:

                $ allowSnow = renpy.random.randint(1,10)

                if allowSnow == 9:

                    $ sinceSnow = 0

                    "You arrived. The weather seems nice. There do seem to be some clouds rolling in, however."

                else:
                    "The weather seems to be great! No oncoming clouds."
            
            else:
                "You arrived. The weather is XXX but it is XXX, which is impossible."

jump start

#######################################################################
#############################  FORECAST  ##############################
#######################################################################

## This forecast only works for Rain, not Snow, however you can always adapt it to work with Snow, I just haven't done
## that as the Weather GUI does a better job at this anyway. This is just mainly a cute thing you could add to a T.V.
## in your game, or something.

label weatherForecast:

    if isRaining == 1:
        "It is raining."
        if rainTime >= 50:
            "It doesn't look like it'll be stopping any time soon."
        else:
            "But, it should stop soon."
    elif sinceRain == 0:
        "There may be rain today."
    else:
        "It seems sunny, with no clouds today!"

jump start

#######################################################################
###########################  WEATHER: GUI  ############################
#######################################################################

## This works with screens. If you don't already know the basics of them, I highly recommend you touch up on them using
## the screens tutorial on https://www.lezcave.com , which is made by one of our dearest moderators over on the RenPy
## Discord server, where you can also get help from there, too. This will have significantly less comments, as it is
## easier to grasp than what has been done previously.

screen weatherGUI():

    frame:

        vbox:
            xalign 0.0
            yalign 0.0
            spacing 10
            ## Appears in top left corner.

            label _("Current Weather:"):
                xalign 0.5

            if isRaining == 1 and isSnowing == 1: ## A certain case if it is snowing and raining, does not show heavy
                text _("Raining | Snowing") ## or light rain/snow.
            elif isRaining == 1: ## Checks for rain. Priority weather.
                if rainTime >= 50: ## More than 50 rainTime left.
                    text _("Heavy Rain")
                else:
                    text _("Light Rain")
            elif isSnowing and areaIsCold: ## If it is cold and is snowing.
                if snowTime >= 50: ## More than 50 snowTime left.
                    text _("Blizzard + Cold")
                else:
                    text _("Light Snow + Cold")
            elif areaIsCold and sinceSnow == 0: ## If it is cold and can snow.
                text _("Cloudy + Cold")
            elif areaIsCold and sinceSnow == 1: ## If it is cold and can not snow.
                text _("Sunny + Cold")
            elif sinceRain == 0: ## If it is not cold and can rain.
                text _("Cloudy")
            else: ## If it is not cold and can not rain.
                text _("Sunny")
            ## Dynamically changing, can be mainly used for debug if you don't want this in your game. It changes between
            ## regions, too, so if it is sunny in one region and a blizzard in another, it stores that state and displays
            ## the correct one when in that region.

            # text "[isRaining] [sinceRain] [rainTime] | [areaIsCold] | [isSnowing] [sinceSnow] [snowTime]"
            ## For Debug, shows Values. Updates with the Values. [allowRain] and [allowSnow] can be added, you must travel
            ## to each region first before adding them, as if not it crashes the game.