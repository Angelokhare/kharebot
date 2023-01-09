import React, { useState, useEffect } from "react";
import { Link, Routes, Route, useNavigate, redirect, useLocation } from 'react-router-dom'
import Axios from "axios"
import bcrypt from "bcryptjs";
import backend_Api from "../services/config"
import '../fonts/HelveticaHigh/HelveticaHigh.ttf'
import '../fonts/HelveticaLow/HelveticaLow.ttf'
import "../style.scss"


// href="/login
// declare global {
//     interface Window { MyNamespace: any; }
// }

// window.MyNamespace = window.MyNamespace || {};

// (window as any).MyNamespace = "nnn"


export default function SignupPage() {

    const navigate = useNavigate();
    const location = useLocation();
    console.log(location.pathname);


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk        Setting Query Messages
    localStorage.setItem('emailValidText', "");
    localStorage.setItem('passwordValidText', "");
    if(localStorage.getItem('passwordValidText')==null){
        localStorage.setItem('passwordValidText', "")
    }
    if(localStorage.getItem('emailValidText')==null){
        localStorage.setItem('emailValidText', "")
    }
    if(localStorage.getItem('usernameText')==null){
        localStorage.setItem('usernameText', "")
    }
    if(localStorage.getItem('emailText')==null){
        localStorage.setItem('emailText', "")
    }
    if(localStorage.getItem('passwordText')==null){
        localStorage.setItem('passwordText', "")
    }


    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk           Backend Data
      const [data, setData]= useState("")
    useEffect(()=> {
        fetch(backend_Api + "/signup")
        .then(res => res.json())
        .then(data => setData(data))
    }, [])
    console.log(data)



    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                Button Transformation
    const [SignupButtonDisplay, setSignupButtonDisplay] = useState("block")
    const [LoadingButtonDisplay, setLoadingButtonDisplay] = useState("none")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                               Input Value

    const [EmailValue, setEmailValue] = useState("")



    const [UsernameValue, setUsernameValue] = useState("")
    const [PasswordValue, setPasswordValue] = useState("")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Button Color
    const [ButtonColor, setButtonColor] = useState("#545f81")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Button Submittion


    const ButtonTypes = [
        "button",
        "submit",
        "reset",
        // undefined
    ]
    // const [ButtonSubmittion, setButtonSubmittion]= useState("")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Password Length Answer
    const [PasswordLength, setPasswordLength] = useState("")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Username Special Characteers
    const [UsernameKey, setUsernameKey] = useState("")

      // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Email Checking Errors
      const [EmailKey, setEmailKey] = useState("")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                           Password Visibility
    const [PasswordVisibility, setPasswordVisibility] = useState("password")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                       Password Button Availability
    const [FirstButton, setFirstButton] = useState("block")
    const [SecondButton, setSecondButton] = useState("none")






    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                        Submission to Backend



    const SubmitionCharacteristics = (event: any) => {
        event.preventDefault();

        var specialChars = "<>@!#%^&*() +[]{}?:;|'\"\\,./~`-=";
        var checkForSpecialChar = function (string: string) {
            for (let i = 0; i < specialChars.length; i++) {
                if (string.indexOf(specialChars[i]) > -1) {
                    return true
                }
            }
            return false;
        }

        var str = event.target.username.value.toLowerCase().trim()


        if (checkForSpecialChar(str)) {
                (window as any).MyNamespace = "Space and Special keys not allowed"
                setUsernameKey("")
                localStorage.setItem('usernameText', "Space and Special keys not allowed");

                localStorage.setItem('EmailValue', event.target.email.value.toLowerCase().trim())
                 var ch= localStorage.getItem('EmailValue')
             
       

            setButtonColor("#545f81")
  

        }
        else {
            if (/\p{Extended_Pictographic}/u.test(str)) {
                setUsernameKey("")
                localStorage.setItem('usernameText', "Space and Special keys not allowed.");
            }
            else {

                if (str.length > 25) {
                    setUsernameKey("")
                    localStorage.setItem('usernameText', "Username is too long.");
                }
            else{

                let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w\w+)+$/;
                if (reg.test(EmailValue.toLocaleLowerCase().trim()) === false) {
                    setEmailKey("")
                    localStorage.setItem('emailText', "This is not a valid Email address.");

                }

                else{
                    if(event.target.password.value.length <= 7){
                        localStorage.setItem('passwordText',"Your Password Length should be at least 8 characters.")
                    }
                    else{
                   if(data[0].includes(event.target.email.value.toLowerCase().trim())){
                    localStorage.setItem('emailText', "This Email has already been used.");
                    navigate(location.pathname)
                   } 
                   else if(data[1].includes(event.target.username.value.toLowerCase().trim())){
                    localStorage.setItem('usernameText', "This Username has already been used.");
                    navigate(location.pathname)
                   } 
                   else{
                    window.open('https://telegram.me/khare_trading_bot', '_blank');
                   navigate("/login")
                    const saltRounds = 10;
                    bcrypt.genSalt(saltRounds, function(err:any, salt:any) {
                      bcrypt.hash(event.target.password.value, salt, function(err:any, hash:any) {

                    Axios.post(backend_Api + location.pathname, {
                        username: event.target.username.value.toLowerCase().trim(),
                        email: event.target.email.value.toLowerCase().trim(),
                        password: hash
                    })
                    setSignupButtonDisplay("none");
                    setLoadingButtonDisplay("block");
                    console.log("yeah1")
                })
            })
                   }       
           
            
            }
            }
        }
            }
        }

    }


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                         Change Button Color

    const changeButtonColor = () => {

        if (UsernameValue != "") {
            localStorage.setItem('usernameText', "");

            var specialChars = "<>@!#%^&*() +[]{}?:;|'\"\\,./~`-=";
            var checkForSpecialChar = function (string: string) {
                for (let i = 0; i < specialChars.length; i++) {
                    if (string.indexOf(specialChars[i]) > -1) {
                        return true
                    }
                }
                return false;
            }

            var str = UsernameValue.toLocaleLowerCase();
            if (checkForSpecialChar(str)) {
                setButtonColor("#545f81")
                setUsernameKey("Space and Special keys not allowed")
            } else {
                if (/\p{Extended_Pictographic}/u.test(str)) {
                    setButtonColor("#545f81")
                    setUsernameKey("Space and Special keys not allowed")
                }
                else {
                    setUsernameKey("")

                    if (str.length > 25) {
                        setButtonColor("#545f81")
                        setUsernameKey("Username is too long.")
                    }
                else{

                    if (EmailValue != "") {
                    localStorage.setItem('emailText', "");
                        let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w\w+)+$/;
                        if (reg.test(EmailValue.toLocaleLowerCase().trim()) === false) {
                            setButtonColor("#545f81")
                            setEmailKey("This is not a valid Email address")
                        }
                        else {
                            setEmailKey("")
                            if (PasswordValue.length >= 8) {

                                setButtonColor("#000")

                            }
                            else {
                                setButtonColor("#545f81")
                            }
                        }
                    }
                    else {
                        setButtonColor("#545f81")
                    }
                }
                }

                // setButtonSubmittion(submit)
            }
        }
        else {
            setButtonColor("#545f81")
            setUsernameKey("")
        }

    }


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                           Password Length
    const passwoordLemghtDetector = (event: any) => {
        if (event.target.value == "") {
            console.log("gggg")
            setPasswordLength("")
        }
        else if (event.target.value.length <= 7) {
            localStorage.setItem('passwordText', "");
            setPasswordLength("Your Password Length should be at least 8 characters.")
        }
        else {
            setPasswordLength("")
        }
    }


    const passwordCall1 = () => {
        setPasswordVisibility("text")
        setFirstButton("none")
        setSecondButton("block")
    }
    const passwordCall2 = () => {
        setPasswordVisibility("password")
        setSecondButton("none")
        setFirstButton("block")

    }

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                         Username Validity
const usernameValidity = (event: any) => {
    if(data[1].includes(event.target.value.toLowerCase().trim())){
        setUsernameKey("")
        localStorage.setItem('usernameText', "This Username has already been used.");
       } 

    else{
        localStorage.setItem('usernameText', "");
        
    }   

}

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                         Email Validity
const emailValidity = (event: any) => {
    if(data[0].includes(event.target.value.toLowerCase().trim())){
        setEmailKey("")
        localStorage.setItem('emailText', "This Email has already been used.");
       } 

    else{
        localStorage.setItem('emailText', "");
        
    }   

}




    return (
        <div className="loginCovering">

            <div className="signupImageCase">
                <img className="loginImage" src="../signupImage.webp" alt="Signup image" />
            </div>
            <div className="signupDetails">
                <div className="iconCase">
                    {/* <li className="iconSeparate"> */}
                    <img src="../icon.png" className="iconImage" alt="Khare Trading Bot icon" />
                    <ul style={{ listStyle: "none" }}>
                        <li className="iconSeparate">
                            <a onClick={(event: any) => navigate('/')} style={{ color: "#213f7d", textDecoration: "none", fontWeight: "700", cursor: "pointer" }} className="headerLink coporateLanguage">Home</a>
                        </li>
                        <li className="iconSeparate">
                            <a style={{ color: "#fff", textDecoration: "none", cursor: "pointer" }} onClick={(event: any) => navigate('/login')} className="headerButton coporateLanguage">Login</a>
                        </li>

                    </ul>
                    {/* </li> */}

                </div>
                <div className="loginTitleCase">
                    <p style={{ color: "#000" }} className="loginTittle">Let's get started</p>
                    <img className="LogingWaving" src="../victory.png" alt="" />
                </div>
                <p className="loginDescription">Signup to enjoy remote crypto trading.</p>
                <form action="" className="loginForm" onSubmit={SubmitionCharacteristics}>
                    <p style={{ color: "#000" }} className="LoginCase coporateLanguage">Email:</p>
                    <input type="email" name="email" id="" style={{textTransform: "capitalize"}} className="loginInput" placeholder="Email" value={EmailValue}
                        onChange={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor(), emailValidity(event))}
                        onKeyDown={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor(), emailValidity(event))}
                        onKeyUp={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor(), emailValidity(event))} required />
                    <p style={{ fontSize: "1vw", color: "red", marginTop: "-1%" }} className="languageStructure">{EmailKey + localStorage.getItem('emailText')}</p>
                    <p style={{ color: "#000" }} className="coporateLanguage LoginCase">Username:</p>
                    <input type="text" name="username" id="" className="loginInput"   maxLength={25}  placeholder="Username" value={UsernameValue}
                        onChange={(event: any) => (setUsernameValue(event.target.value.toLowerCase()), changeButtonColor(), usernameValidity(event))}
                        onKeyDown={(event: any) => (setUsernameValue(event.target.value.toLowerCase()), changeButtonColor(), usernameValidity(event))}
                        onKeyUp={(event: any) => (setUsernameValue(event.target.value.toLowerCase()), changeButtonColor(), usernameValidity(event))}
                        onInput={(event: any) => event.target.value.replace(/[^a-zA-Z0-9 ]/gm, '')}
                        onPaste={(event: any) => event.target.value.replace(/[^a-zA-Z0-9 ]/gm, '')}
                        required />
                    <p style={{ fontSize: "1vw", color: "red", marginTop: "-1%" }}className="languageStructure">{UsernameKey + localStorage.getItem('usernameText')}</p>
                    <p style={{ color: "#000" }} className="coporateLanguage LoginCase">Password:</p>
                    <div className="passwordTogether">
                        <input type={PasswordVisibility} name="password" id="" className="loginInput" style={{ borderRadius: "0", borderRight: "none", borderTopLeftRadius: "5px", borderBottomLeftRadius: "5px" }} placeholder="Password" value={PasswordValue}
                            minLength={8}
                            onChange={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor(), passwoordLemghtDetector(event))}
                            onKeyDown={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor(), passwoordLemghtDetector(event))}
                            onKeyUp={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor(), passwoordLemghtDetector(event))}
                            required />
                        <button type="button" style={{ marginTop: "-0.7vw", marginBottom: "1vw", borderLeft: "none", cursor: "pointer", backgroundColor: "#fff", marginRight: "1.5vw", borderRadius: "0px 5px 5px 0px", display: (FirstButton) }} onClick={passwordCall1} className="visibleClass"><img style={{ width: "1.5vw" }} src="../invisible.png" alt="" /></button>
                        <button type="button" style={{ marginTop: "-0.7vw", marginBottom: "1vw", borderLeft: "none", cursor: "pointer", backgroundColor: "#fff", marginRight: "1.5vw", borderRadius: "0px 5px 5px 0px", display: (SecondButton) }} onClick={passwordCall2} className="visibleClass"><img style={{ width: "1.5vw" }} src="../visible.png" alt="" /></button>

                    </div>
                    <p style={{ fontSize: "1vw", color: "red", marginTop: "-1%" }} className="languageStructure">{PasswordLength + localStorage.getItem('passwordText')}</p>
                    <br />
                    <input type={"checkbox"} required />

                    <label style={{ fontSize: "1.1vw" }} className="languageStructure">

                        <span className={"custom-checkbox"}></span><a style={{ color: "#000", textDecoration: "none" }} href="">I agree with the terms and conditons
                        </a>
                    </label>




                    <button style={{ backgroundColor: "#fbfcff", borderColor: "#598fc4", border: "1px solid #598fc4", display: (LoadingButtonDisplay) }} className="loadingButton" type="button"><img style={{ width: "1.3vw" }} src="loading.gif" alt="" /></button>
                    <button style={{ backgroundColor: (ButtonColor), borderColor: (ButtonColor), border: (ButtonColor), display: (SignupButtonDisplay) }} className="SignupButton" type="submit" >CREATE ACCOUNT</button>
                    <h1 style={{ color: "#545F7D", textAlign: "center" }} className="languageStructure NavigationSignup"> Already have an account? <a style={{ color: "#000", textDecoration: "none", cursor: "pointer" }} onClick={(event: any) => navigate('/login')}>Login</a></h1>
                </form>

            </div>

        </div>
    )

}
