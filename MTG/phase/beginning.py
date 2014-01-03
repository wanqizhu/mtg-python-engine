def run(game):
    """Run through the beginning phase of a turn"""
    
    active_player = game.get_active_player()
    
    active_player.zero_lands_played()

    ## Untap Step

    active_player.untap()

    ## Upkeep Step

    # TODO: Add in abilities that trigger at start of upkeep

    game.gain_priority()

    ## Draw Step

    active_player.draw()

    
    
