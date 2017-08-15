if [ "$1" == "-v" ]; then  # verbose
	python3 -m unittest -v
else
	python3 -m unittest -v -b  # silence stdout
fi
# python3 MTG/test/test_mana.py -b
# python3 MTG/test/test_player.py -b
# python3 MTG/test/test_game.py -b