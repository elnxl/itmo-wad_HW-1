from flask import redirect, url_for, render_template
from app import app
import requests
from bs4 import BeautifulSoup

@app.route('/', methods=['GET'])
def hello():
    return redirect(url_for('profile'))

@app.route('/profile', methods=['GET'])
def profile():
    username='elnxl'
    github_html = requests.get(f'https://github.com/{username}').text
    soup = BeautifulSoup(github_html, "html.parser")
    fullname = soup.find('span',class_= "p-name vcard-fullname d-block overflow-hidden").text
    nickname = soup.find('span',class_= "p-nickname vcard-username d-block").text
    repos = soup.find('span',class_="Counter").text
    follow = soup.find_all('span',class_="text-bold color-fg-default")

    user= {'username': nickname,
           'fullname': fullname,
           'city': 'Saint-Peterburg',
           'repos': repos,
           'followers': follow[0].text,
           'following': follow[1].text
    }

    return render_template('profile.html', title='Profile', user=user)
