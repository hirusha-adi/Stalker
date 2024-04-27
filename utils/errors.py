def handle_errors(func):
    """
    A decorator to handle errors gracefully in functions.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    Raises:
        None

    Example:
        @handle_errors
        def my_function():
            try:
                # code that might raise an exception
            except Exception as e:
                # handle the exception gracefully
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")

    return wrapper
