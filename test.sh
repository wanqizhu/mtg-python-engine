if [ "$1" == "-v" ]; then  # verbose
	python3 -m unittest -v -f
elif [ "$1" == "-q" ]; then
  python3 -m unittest -b -f
else
	python3 -m unittest -v -b -f  # silence stdout
fi
# python3 MTG/test/test_mana.py -b
# python3 MTG/test/test_player.py -b
# python3 MTG/test/test_game.py -b