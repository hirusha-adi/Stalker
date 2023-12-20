
class PhoneinfogaNotFoundError(Exception):
    """
    Exception raised when the Phoneinfoga executable is not found.

    This exception is raised when attempting to execute Phoneinfoga, but the required executable
    (phoneinfoga.exe) cannot be found in the specified location.
    """
    pass

