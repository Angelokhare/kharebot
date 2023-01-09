import React, { useState, useEffect } from "react";
import { Link, Routes, Route, useNavigate, redirect, useLocation  } from 'react-router-dom'
import Axios from "axios"
import bcrypt from 'bcryptjs';
import backend_Api from "../services/config"
import '../fonts/HelveticaHigh/HelveticaHigh.ttf'
import '../fonts/HelveticaLow/HelveticaLow.ttf'
import "../style.scss"
import { responseInterceptor } from "http-proxy-middleware";

export default function LoginPage() {

    const navigate = useNavigate();
    const location = useLocation();
    console.log(location.pathname);


// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk        Setting Query Messages
    localStorage.setItem('usernameText', "");
    localStorage.setItem('emailText', "");
    localStorage.setItem('passwordText', "");
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
        fetch(backend_Api + "/login")
        .then(res => res.json())
        .then(data => setData(data))
    }, [])
    console.log(data)

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                Button Transformation
    const [LoginButtonDisplay, setLoginButtonDisplay]= useState("block")
    const [LoadingButtonDisplay, setLoadingButtonDisplay]= useState("none")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                               Input Value
    const [EmailValue, setEmailValue]= useState("")
    const [PasswordValue, setPasswordValue]= useState("")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Button Color
const [ButtonColor, setButtonColor]= useState("#545f81")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                       Password Button Availability
const [FirstButton, setFirstButton]= useState("block")
const [SecondButton, setSecondButton]= useState("none")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                           Password Visibility
const [PasswordVisibility, setPasswordVisibility]= useState("password")





    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                        Submission to Backend

const SubmitionCharacteristics= (event : any)=>{
        event.preventDefault();

        if(data[0].includes(event.target.email.value.toLowerCase().trim())){

       var userPassword= data[1][data[0].indexOf(event.target.email.value.toLowerCase().trim())]


       bcrypt.compare(event.target.password.value, userPassword, (err:any, got:any)=>{
        console.log("zz")

        if(got){
          navigate("/signup")
          window.open('https://telegram.me/khare_trading_bot', '_blank');
          localStorage.setItem('passwordValidText', "");
          console.log("qq")
          setLoginButtonDisplay("none");
          setLoadingButtonDisplay("block");
        }
        else{
            navigate(location.pathname)
            localStorage.setItem('passwordValidText', "Password is incorrect.");
        }
      })



           } 
         else{
            localStorage.setItem('emailValidText', "This Email address is invalid.");
            localStorage.setItem('passwordValidText', "");
            navigate(location.pathname)

         }  


}

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                  Button Changing Event
const changeButtonColor=()=>{

    if(EmailValue!=""){
        localStorage.setItem('emailValidText', "");
        setButtonColor("#000")
        if(PasswordValue!=""){
            setButtonColor("#000")
        }
        else{
    setButtonColor("#545f81")

        }
    }
    else{
        setButtonColor("#545f81")
    }
}



const passwordCall1=()=>{
    setPasswordVisibility("text")
    setFirstButton("none")
    setSecondButton("block")
}
const passwordCall2=()=>{
    setPasswordVisibility("password")
    setSecondButton("none")
    setFirstButton("block")

}







    return (
        <div className="loginCovering">

            <div className="loginImageCase">
                <img className="loginImage" src="../loginImage.webp" alt="login image" />
            </div>
            <div className="loginDetails">
                <div className="iconCase">
                {/* <li className="iconSeparate"> */}
                <img src="../icon.png" className="iconImage" alt="Khare Trading Bot icon" />
                <ul style={{listStyle: "none"}}>
                <li className="iconSeparate">
            <a  onClick={(event: any) => navigate('/signup')} style={{color:"#213f7d", textDecoration:"none", fontWeight: "700", cursor: "pointer"}} className="headerLink coporateLanguage">Home</a>
                </li>
         <li className="iconSeparate">
            <a  onClick={(event: any) => navigate('/signup')} style={{color:"#fff", textDecoration:"none", cursor: "pointer"}} className="headerButton coporateLanguage">Signup</a>
                </li>

                </ul>
                {/* </li> */}
    
                </div>
                <div className="loginTitleCase">
                <p style={{ color: "#000" }} className="loginTittle">Hey, hello</p>
                <img className="LogingWaving" src="../wavinghand.png" alt="" />
                </div>
                <p className="loginDescription">Please enter your information to login.</p>
                <form action="" className="loginForm" onSubmit={SubmitionCharacteristics}>
                  <p style={{color: "#000"}} className="coporateLanguage LoginCase">Email:</p>
                    <input type="email" name="email" id="" className="loginInput" placeholder="Email"  value={EmailValue}  
                   onChange={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor()) }
                    onKeyDown={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor() )} 
                    onKeyUp={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor())} required />
                    <p style={{ fontSize: "1vw", color: "red", marginTop: "-1%" }} className="languageStructure">{localStorage.getItem('emailValidText')}</p>
                    <p style={{color: "#000"}} className="coporateLanguage LoginCase">Password:</p>
                    <div className="passwordTogether">
                    <input  type={PasswordVisibility} name="password" id="" className="loginInput" style={{borderRadius:"0"  ,borderRight:"none", borderTopLeftRadius: "5px", borderBottomLeftRadius: "5px"}}   placeholder="Password"  value={PasswordValue}
                                    onChange={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor())}  
                                    onKeyDown={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor())}  
                                    onKeyUp={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor())} 
                    required />
                    <button type="button" style={{ borderLeft:"none",  cursor: "pointer", backgroundColor: "#fff", marginRight: "1.5vw", borderRadius: "0px 5px 5px 0px", display:(FirstButton)}} onClick={passwordCall1} className="visibleClass"><img className="loginEye" src="../invisible.png" alt="" /></button>
                    <button type="button" style={{marginTop: "-0.7vw", marginBottom: "1vw", borderLeft:"none",  cursor: "pointer", backgroundColor: "#fff", marginRight: "1.5vw", borderRadius: "0px 5px 5px 0px", display:(SecondButton)}} onClick={passwordCall2} className="visibleClass"><img className="loginEye" src="../visible.png" alt="" /></button>
                  </div>
                  <p style={{ fontSize: "1vw", color: "red", marginTop: "-1%" }} className="languageStructure">{localStorage.getItem('passwordValidText')}</p>

                    <h1 className="forgotPassword languageStructure">Forgot password?</h1>
                    <button style={{backgroundColor: (ButtonColor), borderColor: (ButtonColor), border: (ButtonColor), display: (LoginButtonDisplay)}}  className="loginButton" type="submit"> LOG IN </button>
                    {/* style={{backgroundColor: (ButtonColor), borderColor: (ButtonColor), border: (ButtonColor), display: (LoginButtonDisplay)}} */}


                    <button style={{backgroundColor: "#fbfcff", borderColor: "#598fc4", border: "1px solid #598fc4", display: (LoadingButtonDisplay)}} className="loadingButton" type="button"><img style={{width:"1.3vw"}} src="loading.gif" alt="" /></button>

                </form>
                <h1 style={{color: "#545F7D", textAlign: "center"}} className="languageStructure NavigationSignup"> Don't have an account? <a style={{color:"#000", textDecoration:"none", cursor: "pointer"}}   onClick={(event: any) => navigate('/signup')} >Sign up for free</a></h1>
            </div>

        </div>
    )

}
