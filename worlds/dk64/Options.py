import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList


# DK64_TODO: Get Options from DK64R

class Goal(Choice):
    """
    Determines the goal of the seed
    """
    display_name = "Goal"
    option_krool = 0
    default = 0


dk64_options: typing.Dict[str, type(Option)] = {
    "death_link": DeathLink,
    "goal": Goal,
}
