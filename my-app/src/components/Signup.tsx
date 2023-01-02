import React, { useState, useEffect } from "react";
import { Link, Routes, Route, useNavigate } from 'react-router-dom'
import '../fonts/HelveticaHigh/HelveticaHigh.ttf'
import '../fonts/HelveticaLow/HelveticaLow.ttf'
import "../style.scss"







export default function SignupPage() {

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                                Button Transformation
    const [SignupButtonDisplay, setSignupButtonDisplay]= useState("block")
    const [LoadingButtonDisplay, setLoadingButtonDisplay]= useState("none")

    // kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                               Input Value
    const [EmailValue, setEmailValue]= useState("")
    const [UsernameValue, setUsernameValue]= useState("")
    const [PasswordValue, setPasswordValue]= useState("")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Button Color
const [ButtonColor, setButtonColor]= useState("#545f81")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Button Submittion


const ButtonTypes =[
    "button",
    "submit",
    "reset",
    // undefined
]
// const [ButtonSubmittion, setButtonSubmittion]= useState("")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Password Length Answer
const [PasswordLength, setPasswordLength]= useState("")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                            Username Special Characteers
const [UsernameKey, setUsernameKey]= useState("")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                           Password Visibility
const [PasswordVisibility, setPasswordVisibility]= useState("password")

// kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk                       Password Button Availability
const [FirstButton, setFirstButton]= useState("block")
const [SecondButton, setSecondButton]= useState("none")







const SubmitionCharacteristics= (event : any)=>{

    // event.preventDefault();
        setSignupButtonDisplay("none");
        setLoadingButtonDisplay("block");

}

const changeButtonColor=()=>{

              if(UsernameValue!=""){

                var specialChars = "<>@!#%^&*() +[]{}?:;|'\"\\,./~`-=";
                var checkForSpecialChar = function(string :string){
                 for(let i = 0; i < specialChars.length;i++){
                   if(string.indexOf(specialChars[i]) > -1){
                       return true
                    }
                 }
                 return false;
                }
                
                var str = UsernameValue;
                if(checkForSpecialChar(str)){
                    setButtonColor("#545f81")
                    setUsernameKey("Space and Special keys not allowed")
                } else {
                    if(/\p{Extended_Pictographic}/u.test(str)){
                        setButtonColor("#545f81")
                        setUsernameKey("Space and Special keys not allowed")
                    }
                    else{
                   setUsernameKey("")


                    if(EmailValue!=""){
                        let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w\w+)+$/;
                        if(reg.test(EmailValue.trim()) === false){
                            setButtonColor("#545f81")
                        }
                        else{

                        if(PasswordValue.length >=8){

                    setButtonColor("#000")

                        }
                    else{
                        setButtonColor("#545f81")
                    }
                }
                }
                else{
                    setButtonColor("#545f81")
                }
                }

                // setButtonSubmittion(submit)
            }
        }
            else{
                setButtonColor("#545f81")
                setUsernameKey("")
            }
    
}


const passwoordLemghtDetector=(event : any)=>{
    if(event.target.value==""){
        console.log("gggg")
        setPasswordLength("")
    }
    else if(event.target.value.length <=7){
        setPasswordLength("Your Password Length should be at least 8 characters.")
    }
    else{
        setPasswordLength("")
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

            <div className="signupImageCase">
                <img className="loginImage" src="../signupImage.webp" alt="Signup image" />
            </div>
            <div className="signupDetails">
                <div className="iconCase">
                {/* <li className="iconSeparate"> */}
                <img src="../icon.png" className="iconImage" alt="Khare Trading Bot icon" />
                <ul style={{listStyle: "none"}}>
                <li className="iconSeparate">
            <a href="/"style={{color:"#213f7d", textDecoration:"none", fontWeight: "700"}} className="headerLink coporateLanguage">Home</a>
                </li>
         <li className="iconSeparate">
            <a href="/login"style={{color:"#fff", textDecoration:"none"}} className="headerButton coporateLanguage">Login</a>
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
                  <p style={{color: "#000"}} className="LoginCase coporateLanguage">Email:</p>
                    <input type="email" name="email" id="" className="loginInput" placeholder="Email" value={EmailValue} 
                    onChange={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor()) }
                    onKeyDown={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor() )} 
                    onKeyUp={(event: any) => (setEmailValue(event.target.value.toLowerCase()), changeButtonColor())}  required />
                    <p style={{color: "#000"}} className="coporateLanguage LoginCase">Username:</p>
                    <input type="text" name="username" id="" className="loginInput" placeholder="Username" value={UsernameValue} 
                    onChange={(event: any) => (setUsernameValue(event.target.value.toLowerCase()), changeButtonColor())} 
                    onKeyDown={(event: any) => (setUsernameValue(event.target.value.toLowerCase()), changeButtonColor())}
                    onKeyUp={(event: any) => (setUsernameValue(event.target.value.toLowerCase()), changeButtonColor())}
                    onInput={(event: any)=> event.target.value.replace( /[^a-zA-Z0-9 ]/gm, '')}
                    onPaste={(event: any)=> event.target.value.replace( /[^a-zA-Z0-9 ]/gm, '')}
                    required />
                    <p style={{fontSize: "1vw", color: "red", marginTop: "-1%"}} className="languageStructure">{UsernameKey}</p>
                    <p style={{color: "#000"}} className="coporateLanguage LoginCase">Password:</p>
                    <div className="passwordTogether">
                    <input type={PasswordVisibility} name="password" id=""  className="loginInput" style={{borderRadius:"0"  ,borderRight:"none", borderTopLeftRadius: "5px", borderBottomLeftRadius: "5px"}} placeholder="Password" value={PasswordValue} 
                     minLength={8}
                    onChange={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor(), passwoordLemghtDetector(event))}  
                    onKeyDown={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor(), passwoordLemghtDetector(event))}  
                    onKeyUp={(event: any) => (setPasswordValue(event.target.value.toLowerCase()), changeButtonColor(), passwoordLemghtDetector(event))}  
                    required />
                    <button type="button" style={{marginTop: "-0.7vw", marginBottom: "1vw", borderLeft:"none",  cursor: "pointer", backgroundColor: "#fff", marginRight: "1.5vw", borderRadius: "0px 5px 5px 0px", display:(FirstButton)}} onClick={passwordCall1} className="visibleClass"><img style={{width:"1.5vw"}} src="../invisible.png" alt="" /></button>
                    <button type="button" style={{marginTop: "-0.7vw", marginBottom: "1vw", borderLeft:"none",  cursor: "pointer", backgroundColor: "#fff", marginRight: "1.5vw", borderRadius: "0px 5px 5px 0px", display:(SecondButton)}} onClick={passwordCall2} className="visibleClass"><img style={{width:"1.5vw"}} src="../visible.png" alt="" /></button>

                    </div>
                    <p style={{fontSize: "1vw", color: "red", marginTop: "-1%"}} className="languageStructure">{PasswordLength}</p>
                  <br />
                    <input type={"checkbox"} required />
                    
<label style={{fontSize: "1.1vw"}} className="languageStructure">

  <span className={"custom-checkbox"}></span><a style={{color:"#000", textDecoration:"none"}} href="">I agree with the terms and conditons
  </a>
</label>




                    <button style={{backgroundColor: "#fbfcff", borderColor: "#598fc4", border: "1px solid #598fc4", display: (LoadingButtonDisplay)}} className="loadingButton" type="button"><img style={{width:"1.3vw"}} src="loading.gif" alt="" /></button>
                    <button style={{backgroundColor: (ButtonColor), borderColor: (ButtonColor), border: (ButtonColor), display: (SignupButtonDisplay)}} className="SignupButton" type="submit" >CREATE ACCOUNT</button>
                    <h1 style={{color: "#545F7D", textAlign: "center"}} className="languageStructure NavigationSignup"> Already have an account? <a style={{color:"#000", textDecoration:"none"}} href="/login">Login</a></h1>
                </form>

            </div>

        </div>
    )

}
