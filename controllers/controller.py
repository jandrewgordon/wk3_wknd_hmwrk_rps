from app import app
from flask import render_template, request
from models.player import Player
from models.game import *

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/game')
def index():
    return render_template("index.html")

@app.route('/game', methods=['POST'])
def display_result():
    player1 = Player("default", request.form['player1_input'])
    print(request.form['player1_input'])
    player2 = Player("default", request.form['player2_input'])
    print(request.form['player2_input'])
    result = decide_result(player1, player2)
    if result == player1:
        return "Player 1 Wins!"
    elif result == player2:
        return "Player 2 Wins!"
    elif result == None:
        return "Draw!"

# @app.route('/<player1_choice>/<player2_choice>')
# def display_result(player1_choice, player2_choice):
#     player1 = Player("default", player1_choice)
#     player2 = Player("default", player2_choice)
#     result = decide_result(player1, player2)
#     if result == player1:
#         return "Player 1 Wins!"
#     elif result == player2:
#         return "Player 2 Wins!"
#     elif result == None:
#         return "Draw!"
