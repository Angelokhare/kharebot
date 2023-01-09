'use strict';

var express = require('express')
var mongoose = require("mongoose")
var dotenv = require('dotenv');
const bcrypt= require("bcrypt")
const cors= require("cors")
var crypto = require("crypto");



class Encrypter {
  constructor(encryptionKey) {
    this.algorithm ="aes-192-cbc";
    this.key = crypto.scryptSync(encryptionKey, "salt", 24);
  }

  encrypt(clearText) {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(this.algorithm, this.key, iv);
    const encrypted = cipher.update(clearText, "utf8", "hex");
    return [
      encrypted + cipher.final("hex"),
      Buffer.from(iv).toString("hex"),
    ].join("|");
  }

  dencrypt(encryptedText) {
    const [encrypted, iv] = encryptedText.split("|");
    if (!iv) throw new Error("IV not found");
    const decipher = crypto.createDecipheriv(
      this.algorithm,
      this.key,
      Buffer.from(iv, "hex")
    );
    return decipher.update(encrypted, "hex", "utf8") + decipher.final("utf8");
  }
}


// Usage

const encrypter = new Encrypter("secret");

// const clearText = "adventure time";
// const encrypted = encrypter.encrypt(clearText);
// const dencrypted = encrypter.dencrypt("a7abe1c87c8c94cc357a1cfeb6d7bd4b|51eaad2d92bb49f50db6f6aa7e6f0fce");

// console.log(dencrypted)



















dotenv.config();

const app = express();
app.use(cors())
app.use(express.json())

mongoose.set('strictQuery', false);

mongoose.connect("mongodb+srv://angelokhare:" + process.env.MONGODB_PASSWORD + "@cluster0.cy072ov.mongodb.net/?retryWrites=true&w=majority")


var newUser = new mongoose.Schema({
  userTelegramId: {
    type: String,
  },
  userName: {
    type: String,
    required: true,
    maxLength: 25,


  },
  email: {
    type: String,
    required: true,


  },
  password: {
    type: String,
    required: true,
    minLength: 8,

  },
  dateJoined: {
    type:   Number,
    required: true,

  },
  linkName: {
    type: String,
    required: true,

  },
  binance: {
    apiKey: { type: String},
    apiSecret: { type: String}

  },
  kucoin: {
    apiKey: { type: String},
    apiSecret: { type: String},
    apiPassphrase: { type: String}
  }
})

var User = new mongoose.model("User", newUser)


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                     Sign up       GET
app.get('/signup', (req, res) => {

  var userNameList = []
  var emailList = []
  var userIdList = []
  User.find({}, function (err, users) {
    for (let x in users) {
      var useremail = users[x].email
      var username = users[x].userName
      var userid = users[x].userId
      emailList.push(useremail)
      userNameList.push(username)
      userIdList.push(userid)

    }
    console.log("op")
    res.send([emailList, userNameList])
  })


  // res.send('Express + TypeScript Server');
});

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk           Sign up          POST
app.post('/signup', (req, res) => {
  const bodyName = req.body
  console.log("yeah2")


  const adduser = new User({
    userName: bodyName.username.toLowerCase(),
    password: bodyName.password,
    email: bodyName.email.toLowerCase(),
    linkName: bodyName.username.toLowerCase(),
    dateJoined: new Date().getTime(),
    userTelegramId: "?",
  binance: {
    apiKey: "?",
    apiSecret: "?"

  },
  kucoin: {
    apiKey: "?",
    apiSecret:"?",
    apiPassphrase: "?"
  }

  })

  adduser.save(function (err) {
    if (err) {
      console.log(err)
    }
    else {
      console.log("done")
    }
  })

})


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                     Login       GET
app.get('/login', (req, res) => {

  var emailList = []
  var passwordList = []

  User.find({}, function (err, users) {
    for (let x in users) {
      var useremail = users[x].email
      var userpassword = users[x].password

      emailList.push(useremail)
      passwordList.push(userpassword)


    }
    console.log([emailList, passwordList])
    res.send([emailList, passwordList])
  })
})

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                     Login       POST
app.get('/login/:test', (req, res) => {

var loginRoute=req.params.test
var emailChecking= loginRoute[0]
var passwordChecking= loginRoute.slice(1, loginRoute.length)



    var emailList=[]
  User.find({}, function(err, users) {
    for (let x in users) {
     var combineemail=users[x].email
     emailList.push(combineemail.toLowerCase())
    }
    console.log("aa")


      console.log("ww")

      User.findOne({email:emailList[parseInt(emailChecking)]}, (err, found)=>{
        console.log("ss")

      bcrypt.compare(passwordChecking, found.password, (err, got)=>{
        console.log("zz")

        if(got){
          res.send(["right"])
          console.log("qq")
        }
        else{
          res.send(["wrong"])
          console.log(["wrong"][0])
        }
      })
  })
  })

console.log("hey")
})


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                     ID       GET
app.get('/id', (req, res) => {

  var idList = []
  var usernameList= []
  
  User.find({}, function (err, users) {
    for (let x in users) {
      var userid = users[x].userTelegramId
      var username = users[x].userName

      idList.push(userid)
      usernameList.push(username)


    }
    console.log([idList, usernameList])
    res.send([idList, usernameList])
  })
})

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                     Libking Account       GET
app.get('/testing', (req, res) => {

  var telegramEmail= req.query.email
  var telegramPassword= req.query.password
  var telegramId= req.query.id

  var emailList = []
  var passwordList = []
  var idList = []


  User.find({}, function (err, users) {
    for (let x in users) {
      var useremail = users[x].email
      var userpassword = users[x].password
      var userid= users[x].userTelegramId
      emailList.push(useremail)
      passwordList.push(userpassword)
      idList.push(userid)


    }
    console.log([emailList, passwordList])
    if(emailList.includes(telegramEmail)){
      bcrypt.compare(telegramPassword, passwordList[emailList.indexOf(telegramEmail)], (err, got)=>{
        console.log("zz")

        if(got){

          if(idList[emailList.indexOf(telegramEmail)]!="?"){
            res.send("Your Account is already linked in another device 👀 \n \nClick on /exitAll to signout globally 🏃‍♂️💨.")
          }

          else{
          var conditions = {email: telegramEmail};
          var update = { userTelegramId: telegramId}
        User.findOneAndUpdate(conditions, update, function (err){
          res.send("Your Account has been linked successufully 🎉🙌 \n \n Click on /myAccount to access your services.")
        })
      }
        }
        else{
          res.send("Wrong credentials" + " \n Click on /linkAccount to try again \n Or \n \n Click on <a href='https://kharetradingbot.netlify.app/signup'>Web</a> to Signup" )
        }
      })
    }
    else{
    res.send("Wrong credentials" + " \n Click on /linkAccount to try again \n Or \n \n Click on <a href='https://kharetradingbot.netlify.app/signup'>Web</a> to Signup" )

    }
    // res.send([emailList, passwordList])
  })
})


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                     Signout       GET
app.get('/signout', (req, res) => {

  var telegramId= req.query.id
  console.log(telegramId)

  var emailList = []
  var idList = []

  User.find({}, function (err, users) {
    for (let x in users) {
      var useremail = users[x].email
      var userid = users[x].userTelegramId

      emailList.push(useremail)
      idList.push(userid)


    }
    if(req.query.globalSignout==undefined){
    var conditions = {email: emailList[idList.indexOf(telegramId)]};
    var update = { userTelegramId: "?"}
  User.findOneAndUpdate(conditions, update, function (err){
    res.send("You have successfully signout out of your account 🏃‍♂️💨 \n \nClick /linkAccount to sign in.")
    console.log("done")
  })
    }
    else{
if(idList[emailList[idList.indexOf(req.query.globalSignout)]]!="?"){
  var conditions = {email: emailList[idList.indexOf(req.body.globalSignout)]};
  var update = { userTelegramId: "?"}
  User.findOneAndUpdate(conditions, update, function (err){
    res.send("Your account have been removed from other devices 🏃‍♂️💨. \n \nClick /linkAccount to sign in.")
    console.log("done")
  })
}
else{
  res.send("none")
}

    }
  })
})


app.get('/binance', (req, res) => {


  var emailList = []
  var idList = []
  var binaceList = []
  var usernameList = []



  User.find({}, function (err, users) {
    for (let x in users) {
      var useremail = users[x].email
      var userid = users[x].userTelegramId
      var userbinace = users[x].binance
      var username = users[x].userName


      emailList.push(useremail)
      idList.push(userid)
      binaceList.push(userbinace)
      usernameList.push(username)

    }
  if(req.query.id==undefined){
    console.log("kkkkk")
    var binanceApiKey= req.query.binanceApiKey
    var binanceApiSecret= req.query.binanceApiSecret




///////////////////////////////////////////////////////////////// Encrypting  binanceApiKey
    var encryptedbinanceApiKey = encrypter.encrypt(binanceApiKey)
console.log(encryptedbinanceApiKey)




///////////////////////////////////////////////////////////////// Encrypting  binanceApiSecret
var encryptedbinanceApiSecret = encrypter.encrypt(binanceApiSecret)
console.log(encryptedbinanceApiSecret)



    var conditions = {userTelegramId: req.query.idTelegram};
    var update = {
      binance: {
        apiKey: encryptedbinanceApiKey,
        apiSecret: encryptedbinanceApiSecret
    
      }
    }
  User.findOneAndUpdate(conditions, update, function (err){
    res.send("Congratulation🥂 \n \nYou have successfully linked your Binance Api to your account💯 \n \nClick /myAccount to see your features.")
    console.log("done")
  })




  }
  else{
    var id= req.query.id
    console.log(id)
    console.log(idList)
    console.log(binaceList)
    console.log(idList.indexOf(id))
    console.log(binaceList[idList.indexOf(id)].apiKey)
    console.log(binaceList[idList.indexOf(id)]["apiSecret"])
    var telegramId= req.query.id
    if( binaceList[idList.indexOf(telegramId)]["apiKey"]=="?"){
 res.send("unaunteticated")
    }
    else{
           if( binaceList[idList.indexOf(telegramId)]["apiSecret"]=="?"){
  res.send("unaunteticated")
    }
    else{
res.send(usernameList[idList.indexOf(id)])
    }
    }
 

    
  }

})
})


// If the filter condition is empty, it means all
// User.remove({}, function ( err ) { 
//   console .log( "success" );
// }); 







app.listen(8080 || process.env.PORT, () => {
  console.log(`⚡️[server]: Server is running at http://localhost:8080`);
});



