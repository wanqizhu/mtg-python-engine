def run(game):
    """Run through the combat step of a turn"""
    active_player = game.get_active_player()

    ## Beginning of Combat Step

    # TODO: Add beginning of combat triggers

    game.gain_priority()

    ## Declare Attackers Step

    # TODO: Add support for multiple defending players
    attackers = active_player.declare_attackers()

    # TODO: Add attacking triggers

    game.gain_priority()

    if attackers:
        ## Declare Blockers Step
        block_dict = {}
        for opponent in game.get_opponents(active_player):
            block_dict.update(opponent.declare_blockers(attackers))
            
        # TODO: active player damage assignment order

        # TODO: defending players damage assignment order

        # TODO: Add support for blocking triggers

        game.gain_priority()

        # TODO: Add first strike damage step

        ## Combat Damage Step

        # TODO: Assign combat damage

        # TODO: Deal combat damage

        # TODO: Combat damage triggers

        game.gain_priority()

    ## End of Combat Step

    # TODO: End of combat triggers

    game.gain_priority()

    # TODO: Remove creatures from combat, if necessary
