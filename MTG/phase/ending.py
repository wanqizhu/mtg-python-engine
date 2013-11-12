def run(game):
    """Run through the ending phase of a turn"""

    ## End step

    # TODO: Beginning of end step triggers

    game.gain_priority()

    ## Cleanup step

    game.get_active_player().discard_to_max_hand()

    # TODO: Clean up damage and this turn effects

    # TODO: Possible remaining triggers

    if game.stack:
        game.gain_priority()
