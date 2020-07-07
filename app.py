from flask import Flask, render_template, request

from collatz import Collatz

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def main():
    return render_template('appInitial.html', message=None)


@app.route('/collatzComplete', methods=['POST'])
def collatz_complete():
    if request.method == 'POST':
        num1 = request.form['num1']
        try:
            val = int(num1)
        except ValueError:
            return render_template('appInitial.html', message="Please input an Integer and try again")

        thisCollatz = Collatz(num1)
        thisCollatz.collatz()
        initialNumberString = str(thisCollatz.getInitialNumber())
        numNowListString = thisCollatz.getNumberNowList()
        loopCountString = str(thisCollatz.getLoopCount())
        finalNumString = str(thisCollatz.getFinalNumber())
        return render_template('appComplete.html', collatzNumInitial=initialNumberString, collatzList=numNowListString,
                               collatzLoop=loopCountString, collatzNumFinal=finalNumString)


if __name__ == ' __main__':
    app.debug = True
    app.run()
