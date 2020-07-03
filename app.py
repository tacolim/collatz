from flask import Flask, render_template, request

from collatz import Collatz

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = request.form['num1']
        thisCollatz = Collatz(num1)
        thisCollatz.collatz()
        initialNumberString = str(thisCollatz.getInitialNumber())
        numNowListString = thisCollatz.getNumberNowList()
        loopCountString = str(thisCollatz.getLoopCount())
        finalNumString = str(thisCollatz.getFinalNumber())
        return render_template('app.html', collatzNumInitial=initialNumberString, collatzList=numNowListString,
                               collatzLoop=loopCountString, collatzNumFinal=finalNumString)

        # num2 = request.form['num2']
        # operation = request.form['operation']
        #
        # if operation == 'add':
        #     sum = float(num1) + float(num2)
        #     return render_template('app.html', sum=sum)
        #
        # elif operation == 'subtract':
        #     sum = float(num1) - float(num2)
        #     return render_template('app.html', sum=sum)
        #
        # elif operation == 'multiply':
        #     sum = float(num1) * float(num2)
        #     return render_template('app.html', sum=sum)
        #
        # elif operation == 'divide':
        #     sum = float(num1) / float(num2)
        #     return render_template('app.html', sum=sum)
        # else:
        #     return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
