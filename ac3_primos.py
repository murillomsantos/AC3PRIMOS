# AC3PRIMOS

from flask import Flask

app = Flask(__name__)

@app.route('/')
def primos():
    primos = []
    num = 2
    while len(primos) < 100:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primos.append(num)
        num += 1
    primos_str = ""
    for i in primos:
        primos_str += str(i) + " "
    return primos_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
