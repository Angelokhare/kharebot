
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from binance.client import Client
from binance.exceptions import BinanceAPIException # here
from datetime import datetime
# import requests
# from requests.adapters import HTTPAdapter
# import random



app=Flask(__name__)



# @app.route('/')
# def front():
#     return render_template("index.html", today=toon, year=big)

@app.route('/balance', methods=('GET', 'POST'))
def balance():
    global dataBack
    binanceApiKey = request.args.get('binanceApiKey')
    binanceApiSecret = request.args.get('binanceApiSecret')
    balanceRequest = request.args.get('balanceRequest')

    client=Client(binanceApiKey,binanceApiSecret)
    try:
      if balanceRequest=="all":
        # print(client.get_account()["balances"])     

        totalBalance=[]
        finalBalance=[]
        for x in client.get_account()["balances"]:
          totalBalance.append(x["free"])
        for a in totalBalance:
          if a== "0.00000000":
            pass
          else:
            finalBalance.append(client.get_account()["balances"][totalBalance.index(a)]["asset"] +": "+ a )

        print(str(finalBalance).replace(",", "\n")) 
        dataBack= str(finalBalance).replace(",", "\n")

    

      elif balanceRequest=="futures":
        # print(client.futures_account_balance())
        dataBack = [float(client.futures_account_balance()[6]['balance'])]
        print([dataBack])

      elif balanceRequest=="spot":
        print(client.spot_account_balance())   

      elif balanceRequest=="margin":
        print(client.get_margin_account()) 
    except BinanceAPIException as e:
     print (e.status_code)
     print (e.message)
     if e.message=="API-key format invalid.":
       dataBack= str(e.status_code) + "Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨."
     else: 
       dataBack= str(e.status_code) + "\n" + e.message     

    return jsonify(dataBack)


@app.route('/price', methods=('GET', 'POST'))
def price():
  try:
    binanceApiKey = request.args.get('binanceApiKey')
    binanceApiSecret = request.args.get('binanceApiSecret')
    cryptoRequest = request.args.get('cryptoRequest').upper()

    client=Client(binanceApiKey,binanceApiSecret)
    pairPrice = client.get_symbol_ticker(symbol=cryptoRequest)["price"]
    print(pairPrice)
    return jsonify([pairPrice, 200])
  # except:
  #   pairPrice="Invalid Trading Pair \n \n click /getPrice to try again."

  except BinanceAPIException as e:
    print (e.status_code)
    print (e.message)
    pairPrice= str(e.status_code) + "\n" + e.message  + "\n \nClick /getPrice to try again."  
    if e.message=="API-key format invalid.":
      pairPrice= str(e.status_code) + " Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨."
      return jsonify([pairPrice, 404 ])
    else:
      pairPrice= str(e.status_code) + "\n" + e.message  + "\n \nClick /getPrice to try again."     
      return jsonify([pairPrice, 404])  





@app.route('/futures_trade', methods=('GET', 'POST'))
def futures_trade():
  print("ttt")
  global tradeResult
  global futureBalance
  try:
    binanceApiKey = request.args.get('binanceApiKey')
    binanceApiSecret = request.args.get('binanceApiSecret')
    tradingPair = request.args.get('tradingPair').upper()
    type = request.args.get('type').upper()
    quantity = request.args.get('quantity')
    takeProfit = request.args.get('takeProfit')
    stopLoss = request.args.get('stopLoss')
    entry = request.args.get('entry')
    leverage = request.args.get('leverage').strip()
    margin = request.args.get('margin')
    market = request.args.get('market').upper()





    

    client=Client(binanceApiKey,binanceApiSecret)
    print(client.futures_get_position_mode())


 
    if market=="BUY":
      refMarket="SELL"
    else:
      refMarket="BUY"                    

    if margin == "Cross":
       marginTest= 'FALSE'
    else:
      marginTest='TRUE'   

              
    if entry=="Market price":
      tradeEntry=""
      tradeTitle="MARKET"
      limit_order_long = client.futures_create_order(
    symbol=tradingPair,
    side=market,
    type=tradeTitle,
    Position__side= type,
    quantity=quantity,
)
      print(limit_order_long)


      if takeProfit != "None":

        sell_gain_market_long = client.futures_create_order(
    symbol=tradingPair,
    side=refMarket,
    type='LIMIT',
    quantity=quantity,
    price= takeProfit
    # stopPrice=takeProfit,
    # closePosition=True,
    # reduceOnly= True
)
        print(sell_gain_market_long)  

      if stopLoss != "None":
        sell_stop_market_short = client.futures_create_order(
      symbol=tradingPair,
    side=refMarket,
    type='LIMIT',
    quantity=quantity,
    # stopPrice=stopLoss,
    price=stopLoss
    # closePosition= True,
    # ReduceOnly= True
)
      print(sell_stop_market_short)

    else:
      tradeTitle='LIMIT'
      tradeEntry=entry
      limit_order_long = client.futures_create_order(
    symbol=tradingPair,
    side=market,
    type=tradeTitle,
    Position__side= type,
    quantity=quantity,
    isIsolated=marginTest,
    timeInForce='GTC',
    price=tradeEntry,
)
      print(limit_order_long)



      if takeProfit != "None":

        sell_gain_market_long = client.futures_create_order(
    symbol=tradingPair,
    side=refMarket,
    type='TAKE_PROFIT_MARKET',
    quantity=quantity,
    stopPrice=takeProfit,
    closePosition=True,
    reduceOnly= True
)
        print(sell_gain_market_long)  

      if stopLoss != "None":
        sell_stop_market_short = client.futures_create_order(
      symbol=tradingPair,
    side=refMarket,
    type='STOP_MARKET',
    quantity=quantity,
    stopPrice=stopLoss,
    closePosition= True,
    ReduceOnly= True
)
      print(sell_stop_market_short)


    global futureBalance
    print(leverage.strip()[0:-1])
    result = client.futures_change_leverage(symbol=tradingPair, leverage=float(leverage.strip()[0:-1])) 




    global futureBalance
    print(leverage.strip()[0:-1])
    result = client.futures_change_leverage(symbol=tradingPair, leverage=float(leverage.strip()[0:-1]))     
    tradeResult="Your trade was entered successfully 🏃‍♂️💨."
    print(tradeResult)
    return jsonify(tradeResult)
  except BinanceAPIException as e:
    print (e.status_code)
    print (e.message)
    if e.message=="API-key format invalid.":
      tradeResult= str(e.status_code) + " Error‼ \nYou used an invalid API key during registration 🤔. \nClick on /deleteApiKey to remove and add a new API key 🏃‍♂️💨."
      return jsonify(tradeResult)

    elif e.message=="Margin is insufficient.": 
      if "usdt" in tradingPair.lower(): 
        futureBalance = float(client.futures_account_balance()[6]['balance'])
      elif "busd" in tradingPair.lower(): 
        futureBalance = float(client.futures_account_balance()[8]['balance'] )
      cryptoPrice = client.get_symbol_ticker(symbol=tradingPair)["price"]

      print((futureBalance * 20)/float(cryptoPrice)) 
      print(leverage.strip()[0:-1])
      tradeResult= "You have insufficient Margin balance to complete this trade \nThe quantity of " + tradingPair + " required to complete this trade is " + str((futureBalance* float(leverage.strip()[0:-1]))/float(cryptoPrice) )
      print(tradeResult)  
      return jsonify(tradeResult)

    elif e.message=="Invalid symbol.": 
      tradeResult= tradingPair + " is an Invalid symbol"
      return jsonify(tradeResult)    
    elif e.message=="Quantity greater than max quantity.": 
      tradeResult= "The quantity entered is greater than max quantity required to enter this trade 😨."
      return jsonify(tradeResult) 

    else:
      return jsonify(e.message) 
               


@app.route('/alert', methods=('GET', 'POST'))
def alert():
  try:
    binanceApiKey = request.args.get('binanceApiKey')
    binanceApiSecret = request.args.get('binanceApiSecret')

    client=Client(binanceApiKey,binanceApiSecret)
    pairPrice = client.get_all_tickers()
    cryptoList=[]
    for x in pairPrice:
      cryptoList.append(x["symbol"] + ":-%20" + str(x["price"]))
      # print(x["symbol"] + ":- " + x["price"])
    print(str(cryptoList).replace(", ", "\n")[1: -1].replace("'", ""))  
    return jsonify(str(cryptoList).replace(", ", "%0A")[1: -1].replace("'", ""))

  # except:
  #   pairPrice="Invalid Trading Pair \n \n click /getPrice to try again."

  except BinanceAPIException as e:
    print (e.status_code)
    print (e.message)
    pairPrice= str(e.status_code) + "\n" + e.message  + "\n \nClick /getPrice to try again."  
    return jsonify(pairPrice)

  


    # pairPrice= str(e.status_code) + "\n" + e.message  + "\n \nClick /getPrice to try again."  





#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     return render_template("index.html", today=toon, year=big)

# # @app.route('/blog')
# # def blog():
# #     fem=t
# #     return render_template("blog.html",fem=fem)

# @app.route('/signup', methods=('GET', 'POST'))
# def signup():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data.lower())
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This Email has exited before!")
#               return redirect(url_for("invalide"))

#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))
#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data.lower(), email=form.email.data.lower(), country=form.country.data.lower(), password=new_password, phone_number=form.phone.data, firstname=form.firstname.data.lower(), lastname=form.lastname.data.lower(), gender=form.gender.data.lower(), birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     return render_template("signup.html", form=form, year=big, today=toon)


# @app.route('/invalid-password', methods=('GET', 'POST'))
# def invalidp():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data)
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This Email has exited before!")
#               return redirect(url_for("invalide"))

#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))
#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data, email=form.email.data, country=form.country.data, password=new_password, phone_number=form.phone.data, firstname=form.firstname.data, lastname=form.lastname.data, gender=form.gender.data, birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     fan="Password entered does not Match!"
#     dot="*"
#     return render_template("signup.html", form=form, year=big, today=toon, mess=fan, x=dot)


# @app.route('/invalid-email', methods=('GET', 'POST'))
# def invalide():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data)
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This account has exited before!")
#               return redirect(url_for("invalide"))

            
#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))

#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data, email=form.email.data, country=form.country.data, password=new_password, phone_number=form.phone.data, firstname=form.firstname.data, lastname=form.lastname.data, gender=form.gender.data, birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     fan="EMAIL already exist!"
#     dot="*"
#     return render_template("signup.html", form=form, year=big, today=toon, mess=fan, y=dot)



# @app.route('/invalid-username', methods=('GET', 'POST'))
# def invalidu():
#     big=datetime.now().strftime("%Y")
#     toon=datetime.now().strftime("%d-%m")
#     form = Signup()
#     if form.validate_on_submit():
#         print(form.username.data)
#         print(form.birthdate.data)
#         if form.password.data== form.confpassword.data:
#             if User.query.filter_by(email=form.email.data).first():
#               flash("This Email has exited before!")
#               return redirect(url_for("invalide"))

#             elif User.query.filter_by(username=form.username.data).first():  
#                 flash("This username has exited before!")
#                 return redirect(url_for("invalidu"))
#             else:
#                 new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
#                 person= User(username=form.username.data, email=form.email.data, country=form.country.data, password=new_password, phone_number=form.phone.data, firstname=form.firstname.data, lastname=form.lastname.data, gender=form.gender.data, birthday=form.birthdate.data)
#                 print(form.username.data)
#                 db.session.add(person)
#                 db.session.commit()
#             return ("New user has been created!")
#         else:
#             flash(message="incorrect password")
#             return redirect(url_for("invalidp"))
#     fan="Username already exist!"
#     dot="*"
#     return render_template("signup.html", form=form, year=big, today=toon, mess=fan, z=dot)    



# @app.route('/login', methods=("POST", "GET"))
# def login():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     if request.method=="POST":
#         name = request.form['username'].lower()
#         password = request.form['password']
#         print(name)
#         print(password)
#         us= User.query.filter_by(email=name).first() 
#         using= User.query.filter_by(username=name).first()
#         if us :
#             flash("This account has exited before!")
#             if check_password_hash(us.password, request.form['password']):
#                 login_user(us)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida")) 
#         elif using:
#             flash("This account has exited before!")
#             if check_password_hash(using.password, request.form['password']):
#                 login_user(using)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))        

#         else:
#             return redirect(url_for("invalidl"))   
#     return render_template("login.html", year=big, today=toon)

# @app.route('/invalid-login-user', methods=("POST", "GET"))
# def invalidl():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     if request.method=="POST":
#         name = request.form['username'].lower()
#         password = request.form['password']
#         print(name)
#         print(password)
#         us= User.query.filter_by(email=name).first() 
#         using= User.query.filter_by(username=name).first()
#         if us:
#             flash("This account has exited before!")
#             if check_password_hash(us.password, request.form['password']):
#                 login_user(us)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))  
#         elif using:
#             flash("This account has exited before!")
#             if check_password_hash(using.password, request.form['password']):
#                 login_user(using)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))         

#         else:
#             return redirect(url_for("invalidl"))  
#     use="This account does not exit!"         
#     return render_template("login.html", year=big, today=toon, note=use)   


# @app.route('/invalid-login-password', methods=("POST", "GET"))
# def invalida():
#     toon=datetime.now().strftime("%d-%m")
#     big=datetime.now().strftime("%Y")
#     if request.method=="POST":
#         name = request.form['username'].lower()
#         password = request.form['password']
#         print(name)
#         print(password)
#         us= User.query.filter_by(email=name).first() 
#         using= User.query.filter_by(username=name).first()
#         if us:
#             flash("This account has exited before!")
#             if check_password_hash(us.password, request.form['password']):
#                 login_user(us)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))  

#         elif using:
#             flash("This account has exited before!")
#             if check_password_hash(using.password, request.form['password']):
#                 login_user(using)
#                 return redirect(url_for("user"))
#             else:
#                 return redirect(url_for("invalida"))         

#         else:
#             return redirect(url_for("invalidl"))  
#     use="This password entered is incorrect!"         
#     return render_template("login.html", year=big, today=toon, note=use) 


# @app.route("/welcome")
# @login_required
# def user():
#     return render_template("user.html", name=current_user.username)


# # @app.route("/welcome")
# # def viv():
# #     return redirect("login") 

# @app.route("/logout-user")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("login"))   


# @app.route('/users-movie', methods=("POST", "GET"))  
# @login_required
# def movie():
#     if request.method=="POST":
#         toon=datetime.now().strftime("%d-%m")
#         viv=datetime.today().strftime('%A').lower()
#         name = request.form['name'].lower()   
#         if name==[]:
#             return render_template("movie.html", dis=viv, today=toon)
#         else:    
#              md="1affd879f3e8aac72ebe06eb3db99dc1"
#              ma="a7f423ca02d4c7d3280f566396d8e180"
#              mc="6a4570c97e3acf8ac318f2bca3ed09cd"
#              mf="8e49fca814ae244c2b6949e2ede67661"
#              letters=[md, ma, mc, mf]
#              hh=random.randint(0,len(letters)-1)
#              vv=letters[hh]
#              print(letters[hh]) 
#              print(name)
#              response = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key": letters[hh], "query": name})
#              data = response.json()["results"]
#              print(vv)
#              if data==[]:
#                 fame = request.form['name']
#                 dam= f"{fame} not found!"
#                 return render_template("movie.html", dam=dam, dis=viv, today=toon)
#              else:
#                 #  print(data)
#                 print(vv)
#                 return render_template("movieshow.html", feg=data)
#     toon=datetime.now().strftime("%d-%m")
#     viv=datetime.today().strftime('%A').lower()
#     return render_template("movie.html", dis=viv, today=toon)   
# viv=datetime.today().strftime('%A').lower()
# print(viv)


# # @app.route('/showcase-movie', methods=("POST", "GET"))
# # @login_required
# # def showcase():
# #     viv=datetime.today().strftime('%A').lower()
# #     if request.method=="POST":
# #         name = request.form['name'].lower()
# #         print(name)
# #         response = requests.get("https://api.themoviedb.org/4/search/movie", params={"api_key": "a7f423ca02d4c7d3280f566396d8e180", "query": name})
# #         data = response.json()["results"]
# #         print(data)
# #         return render_template(("movieshow.html"), feg=data)
# #     return render_template("movieshow.html", dis=viv)
# # 

if __name__=='__main__':
    app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)





















































































# # from flask import Flask, flash, render_template, request, url_for, redirect
# # from datetime import datetime
# # from flask_wtf import FlaskForm
# # from werkzeug.security import check_password_hash, generate_password_hash
# # from wtforms import StringField, PasswordField, SelectField, SubmitField, IntegerField
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_login import login_user, logout_user, LoginManager, UserMixin, login_required, current_user
# # from wtforms.validators import DataRequired, Email, Length, number_range

# # app=Flask(__name__)
# # app.config["SQLALCHEMY_DATABASE_URL"]="sqlite///game.db"
# # app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
# # db=SQLAlchemy(app)

# # login_manage=LoginManager
# # login_manage.init_app(app)

# # class Signup(FlaskForm):
# #     email=StringField(label="Username", validators=[DataRequired(), Email()])
#     # password=PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
# #     username=StringField(label="Name", validators=DataRequired("Pls enter your name!"))
# #     phone_number=IntegerField(label="Phone number", validators=[DataRequired(), number_range()])
# #     submit=SubmitField(label="Submit")

# # class Storage(db.Model, UserMixin):
# #     username= db.Column(db.String(300), nullable=False, unique=True)
# #     id=db.Column(db.Integer, primary_key=True)
# #     password=db.Column(db.String(200), nullable=False)
# #     phone_number=db.Column(db.Integer, nullable=False)
# #     email=db.Column(db.String(200), nullable=False, unique=True)
# # db.create_all()

# # date=datetime.now().strftime("%Y")
# # @app.route('/')
# # def home():
# #     return render_template("index.html")

# # @app.route('/register')
# # def register():
# #     form= Signup()
# #     if form.validate_on_submit():
# #         if Storage.query.filter_by(email=form.email.data).first() or Storage.query.filter_by(username=form.username.data).first():
# #             flash("This account has exited before!")
# #             redirect(url_for("register"))
# #         else:
# #             new_password = generate_password_hash(password=form.password.data, salt_length=8, method='pbkdf2:sha256')
# #             new_person=Storage(password=new_password, username=form.username.data, email=form.email.data)
# #             db.session.add(new_person)
# #             db.session.commit()
# #             redirect(url_for("welcome"))

# #     return render_template("register.html")

# # @app.route('/login')
# # def login():
# #     form=Signup()
# #     email=form.email.data
# #     password=form.password.data
# #     user = Storage.query.filter_by(email=email).first()
# #     if form.validate_on_submit():
# #         if not user:
# #           flash("Email not recognised!")
# #           redirect(url_for("login"))
# #         elif check_password_hash(user.password, password):
# #             flash("Incorrect Password!")
# #             redirect(url_for("login"))
# #         else:
# #             user= Storage.query.filter_by(email=email).first()
# #             check_password_hash(user.password, password)
# #             login_user(user)
# #             redirect("welcome.html")
# #     return render_template("login.html")


# # @app.route('/welcome')
# # @login_required
# # def welcome():
# #     current_user.username
# #     return render_template("welcome.html")




# # if __name__=='__main__':
# #     app.run(debug=True)


