def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Key error. The contact not found."
        except IndexError:
            return "Index error. Try again."
    return inner

def birthday_error(func):
    def inner(*args,**kwargs):
           try:
                return func(*args,**kwargs)
           except ValueError:
                return "Give me name and birthday please."
           except KeyError:
                return "Key error. The contact not found."
           except IndexError:
                return "Index error. Try again."
    return inner

def show_error(func):
    def inner(*args,**kwargs):
           try:
                return func(*args,**kwargs)
           except ValueError:
                return "Give me name, please."
           except KeyError:
                return "Key error. The contact not found."
           except IndexError:
                return "Index error. Try again."
    return inner