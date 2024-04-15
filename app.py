#import flask library along with flask render template, request and requests
from flask import Flask, render_template, request
import requests
#initialize flask
app = Flask(__name__)
#Here __name__ is to definre how you want to run your program. Such
#as presently we want to run our web application using flask.
@app.route("/")
#decorator tells the computer to execute the
#program in an internet browserof the computer.
#Define visitor function to check how many visitor are there
def visitors():

    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    visitors_count = visitors_count + 1

    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()

    # Render HTML with count variable
    return render_template("index.html", count=visitors_count)
    #As you know we need to convert console based output into a GUI based
    #output that will come on the HTML page.
    #To achieve this we will be using flask's render_temlate() method

@app.route('/', methods=['POST'])


# Add route for your webpage

def weather_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    #Get latitude and longitude from the from
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    # Call the weather api 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude and return weather and visitor count while rendering index.html
    api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude

    response = requests.get(api_url)
    weather_data = response.json()
    print(weather_data)
    return render_template("index.html", weather=weather_data, count=visitors_count)
#add code for executing flask
if __name__ == "__main__":
    app.run()
