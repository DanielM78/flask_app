from flask import Flask, render_template, request 
<<<<<<< HEAD
import weather 
# import yelp_page 
app = Flask(__name__)




@app.route("/")
def index():
	forecast = None 

	address = "Philadelphia, PA"
	if address:
		forecast = weather.get_weather(address)
	
	return render_template('index.html', forecast=forecast)
 

if __name__ == "__main__":

    app.run()
=======
import weather


app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    forecast = None
    if address:
        forecast = weather.get_weather(address)

    return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()

>>>>>>> 7da1378c68252e91871dbd6f3c82217ceb4a8953
