import cProfile
import unittest
import pstats

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('.')

    def runtests():
    	# set verbosity to 2 to see each test
        unittest.TextTestRunner(verbosity=1, buffer=True).run(suite)
    
    cProfile.run(
        'runtests()', filename='test_cprofile_results.log', sort='cumtime')

    p = pstats.Stats('test_cprofile_results.log')
    p.strip_dirs().sort_stats('cumulative').print_stats(30)
