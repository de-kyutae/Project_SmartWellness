from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('lotto_input.html')


@app.route('/lotto_result', methods=["POST"])
def lotto_result():
    my_lotto = [int(x) for x in request.form.values()]

    lotto_all = [int(i) for i in range(1, 46)]
    lotto_list = random.sample(lotto_all, 6)

    # 집합 연산 할 수있도록 변환
    myset = set(my_lotto)
    lottoset = set(lotto_list)

    compare_lotto = myset.intersection(lottoset)

    return render_template('lotto_result.html', my_lotto=my_lotto, lotto_list=lotto_list)


def lotto_generator():
    lotto = []
    num = random.randint(1, 45)
    while len(lotto) != 6:
        if num not in lotto:
            lotto.append(num)
    print(lotto)


if __name__ == '__main__':
    app.run()