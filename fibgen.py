from flask import Flask, request, render_template, redirect
from Fibinocci import Fibinocci
#import Fibinocci
application = Flask(__name__)


@application.route('/test')
def hello():
	ls = Fibinocci.getFibinocci(10)
	str1 = ', '.join(str(e) for e in ls)
	return str1

@application.route('/', methods=['GET', 'POST'])
def startingPage():
	if request.method == 'POST':
		nterm = int(request.form.get('nterm'))
		print(nterm)
		application.logger.warning(str(nterm))
		ls = Fibinocci.getFibinocci(nterm)
		str1 = ' '.join(str(e) for e in ls)
		return render_template('home.html',output = str1)

	return render_template('home.html')

if __name__ == '__main__':
	application.run(host='0.0.0.0')
