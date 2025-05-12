from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey! Welcome Here.'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

# METHOD - 01
# to run this project we can use in terminal : 
# uv run --with '<package-name>' --with '<package-name-02>' file_name

# e.g. uv run --with 'flask' .\importing_package_In_Scripts.py

# And Yes we need to write separately all the packages in above style

# METHOD - 02
# use : uv add --script <filename.py> '<package-01>' '<package-02>' 
# then use : uv run <filename.py>

# it will automatically brings the dependencies from the top of your file