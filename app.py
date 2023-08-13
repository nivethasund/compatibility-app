from flask import Flask, render_template, request
import string
import ephem

app = Flask(__name__)

def get_moon_phase(x):
    moon_phase = round(ephem.Moon(x).moon_phase, 2)
    return moon_phase

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/numerology', methods=['GET', 'POST'])
def numerology():
    if request.method == 'POST':
        your_name = request.form['your_name'].replace(" ", "").lower()
        crush_name = request.form['crush_name'].replace(" ", "").lower()

        alphabets = list(string.ascii_lowercase)
        counter = 0
        dict = {}

        for alphabet in alphabets:
            dict[alphabet] = counter + 1
            counter+=1

        def name_count(name):
    
            i = 0
            for x in list(name):
                y=dict[x]
                i = i+y
    
            return i

        your_count = name_count(your_name)
        their_count = name_count(crush_name)

        diff =round((1-(abs(your_count-their_count)/abs(your_count+their_count)))*100,0)
        return render_template('num_result.html', diff=diff)

    return render_template('num_index.html')

@app.route('/moon_phase', methods=['GET', 'POST'])
def moon_phase():
    if request.method == 'POST':
        your_bday = request.form['your_bday']
        crush_bday = request.form['crush_bday']

        your_phase = get_moon_phase(your_bday)
        crush_phase = get_moon_phase(crush_bday)
        compatibility_score = round((your_phase + crush_phase) * 100, 0)

        if compatibility_score >= 100:
            compatibility_message = "Your Compatibility Score is off the charts!! Perfect match at 100%"
        else:
            compatibility_message = f"Your Compatibility Score is {compatibility_score}%!"

        return render_template('moon_result.html', compatibility_message=compatibility_message)

    return render_template('moon_phase.html')
      
if __name__ == "__main__":
    app.run(debug=True)

