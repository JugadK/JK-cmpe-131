import time
def calculate_time(func):
    """
    calculates the time it takes for the following function to happen by using decorators

    The function will calculate time by using a wrapper function which will measure the time at two points but it will run another function in between those two measurments, allowing us to measure the total time it takes for that function to run

    Parameters
    ----------
    func()
        function that will be used between the two variables measuring the current time
    
    Returns
    floats
        difference between the two time measurments
    Examples
    --------
    @calculate_time
    def get_time():
        time.sleep(4)
    4.00003456
    """
    def wrapper():
        """
        Wrapper function for calculate time 

        Wrapper function inside calculate_time, this function will measure the current time twice, but will run the function defined in calculate_time in between it
        Returns
        -------
        Str
            Total time 'X', X being the difference between the two time measurments i.e the time it took for that function to run
        """
        time1 = time.time()
        
        value = func(*args,**kwargs)
        time2 = time.time()
        return 'Total time ' + str((time2-time1))
        return value
    return wrapper


