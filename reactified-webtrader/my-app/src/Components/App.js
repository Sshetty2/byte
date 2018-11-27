import React, { Component } from 'react';
import logo from '../static/logo.svg';
import '../css/App.css';
import { Container, Row, Col } from 'reactstrap';
import BGvid  from './BGvid' 
import Navbar from './NavBar'



export default class App extends Component {
  render() {
    return (
      <div>
      <Navbar />
      <div className="container-fluid text-center">    
        <div className="row content">
          <div className="col-sm-2 sidenav col-sm-2-left">
            <a href="/buy"><button className="button button5"><p>Buy</p></button></a>
            <a href="/sell"><button className="button button5"><p>Sell</p></button></a>
            <a href="/check_stock_price"><button className="button button5"><p>Check Stock Price</p></button></a>
            <a href="/trade_history"><button className="button button5"><p>See Trade History</p></button></a>
            <a href="/deposit_funds"><button className="button button5"><p>Deposit Funds</p></button></a>
          </div>
          <div className="col-sm-8 text-left" styles = {{boxShadow: '0 8px 16px 0', paddingRight: '5px', PaddingLeft: '5px'}}> 
          </div>
          <div className="col-sm-2 sidenav col-sm-2-right" styles = {{paddingLeft: '5px', paddingTop: '5px'}}>
              <div id="news_iframe_scroll">
              <h1>News Scroll PlaceHolder</h1>
              </div>
          </div>
        </div>
      </div>
      <footer className="container-fluid text-center">
      <p>Webtrader &#169 2018 Byte Academy - SShetty</p>
      </footer>
      </div>
    );
  }
}
