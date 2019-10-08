# Decorator cru

def vai():
    print('vai ', end='')

def gerar_grito_da_torcida(fn):
    def wrapper(*args, **kwargs):
        print('vai ', end='')
        return fn(*args, **kwargs)
    return wrapper

@gerar_grito_da_torcida
def corinthians():
    print('corinthians')

@gerar_grito_da_torcida
def palmeiras():
    print('palmeiras')

@gerar_grito_da_torcida
def santos():
    print('santos')

@gerar_grito_da_torcida
def sao_paulo():
    print('sao paulo')

corinthians()
palmeiras()
santos()
sao_paulo()

def cache(fn):
    fn._cache = {}
    def wrapper(*args, **kwargs):
        if args not in fn._cache:
            fn._cache[args] = fn(*args)
        return fn._cache[args]
    return wrapper

@cache
def fib(n):
    if n < 1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(100):
    print(fib(i))


class App:

    def __init__(self, mensagem):
        self.mensagem = mensagem

    def decorar(self, fn):
        def wrapper(*args, **kwargs):
            print(self.mensagem)
            return fn(*args, **kwargs)
        return wrapper


app = App('Python nem é daora')

@app.decorar
def foo():
    print('foo')

foo()
