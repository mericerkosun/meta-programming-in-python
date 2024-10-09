def divide(a, b):
    return a / b

try:
    result = divide(40,0)
except ZeroDivisionError as e: # Spesifik error türünü yakalar.
    print(e, "you can't divide 0.")
except Exception as e:
    print(e.__class__) # Error türünün class'ını yazdırır.
except:
    print("Something went wrong.") # Tüm errorları yakalar.

# Some error types: IndexError | FileNotFoundError
