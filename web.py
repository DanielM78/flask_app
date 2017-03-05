from flask import Flask, render_template, request 
import os 
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",port=port)


