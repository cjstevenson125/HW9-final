from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mike')
def mike():
    return render_template('mike.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        radius = float(request.form['radius'])
        height = float(request.form['height'])
        pi=3.14
        materialcost=25
        laborcost=15

        toparea=(pi*(radius**2))
        sidearea=2*(pi*(radius*height))
        totalarea=toparea+sidearea
        totalarea=totalarea/144
        totalmaterialcost=totalarea*materialcost
        totallaborcost=totalarea*laborcost
        estimate=totalmaterialcost+totallaborcost

    return render_template('estimate.html', myValue=estimate) 





if __name__ == '__main__':
    app.run(debug=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user = users.find_one({"email": request.form['username']})
        if user and user['password'] == request.form['password']:
            user_obj = User(username=user['email'], role=user['role'], id=user['_id'])
            login_user(user_obj)
            next_page = request.args.get('next')