def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Błąd: {e}")
            return None
    return wrapper

@safe_function
def divide(x, y):
    return x / y

divide(6,0)