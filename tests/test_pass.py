""" run with

nosetests -v --nocapture

or

nosetests -v

"""

class Test_pass:

    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_dummy(self):
        HEADING()
        assert True
