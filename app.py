import os
from string import Template
from flask import Flask, render_template, request
from model import SingleIntegerInput


from collatz import Collatz


app = Flask(__name__, instance_relative_config=True)

SECRET = os.urandom(64)
WTF_SECRET = os.urandom(64)

app.config.update(dict(
    SECRET_KEY=SECRET,
    WTF_CSRF_SECRET_KEY=WTF_SECRET
))


# a simple page that has our form
@app.route('/', methods=['GET', 'POST'])
def hello():
    form = SingleIntegerInput(request.form)
    return render_template("view.html", form=form)


@app.route('/<some_collatz>')
def hello_next_thing(some_collatz):
    thisCollatz = Collatz(some_collatz)
    thisCollatz.collatz()
    intialNumberString = str(thisCollatz.getInitialNumber())
    numNowListString = thisCollatz.getNumberNowList()
    loopCountString = str(thisCollatz.getLoopCount())
    finalNumString = str(thisCollatz.getFinalNumber())
    return render_template("result.html", initialNumber=intialNumberString, numNowListString=numNowListString,
                           loopCountString=loopCountString, finalNumString=finalNumString)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
