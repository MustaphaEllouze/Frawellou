class Test : 
    """Class that runs all tests
    * All new tests must begin with '_test_'
    """

    def run(
        verbose:bool=True,
        ) -> bool:
        """Run all tests
        """
        # Return variable
        everything_ok = True

        # Run each test
        for func in [Test.__dict__[key] for key in Test.__dict__.keys() if '_test_' in key]:
            testing = func()
            if verbose : print(f'Runned {func.__name__} --> {testing*"OK"+(1-testing)*"FAILED"}')
            everything_ok = everything_ok and testing
        
        # Returns False if a test went wrong
        return everything_ok
    
    def _test_00() -> bool :
        return True