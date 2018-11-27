import React, { Component } from 'react';

export default class CentralBox extends Component {
  render() {
    return (
      <div className="col-sm-8 text-left" styles = {{boxShadow: '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)', paddingRight: '5px', paddingLeft: '5px'}}> 
         <div id="video-container">
          <video className="fillWidth" loop autoPlay>
              <source id="mp4" src={require("../static/bullbear.mp4")} type="video/mp4"/>
          </video>
              <div className = "bg_content">     
                  <form action="/login" method="post" className="form-signin">
                      <h1 className="h3 mb-3 font-weight-normal">Please sign in</h1>
                      <label htmlFor="username" className="sr-only">Username</label>
                      <input name="username" type="text" id="username" className="form-control" placeholder="Username" required autoFocus />
                      <label htmlFor="password" className="sr-only">Password</label>
                      <input name="password" type="password" id="password" className="form-control" placeholder="Password" required />
                      <button id="myBtn" style = {{fontSize: '15px'}} type="submit">Login</button>
                  </form>
                  <form action="/create_account">
                      <button id="myBtn" style = {{fontSize: '15px'}} type="submit">Create New Account</button>
                  </form>
                </div>
            </div>
        </div>

      )
    }
  }
  