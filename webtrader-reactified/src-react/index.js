import React from 'react'
import { render } from 'react-dom'
// import './stylesheets/ui.scss'
// import './stylesheets/index.scss'

import { Router, Route, hashHistory } from 'react-router'


// import { SkiDayList } from './components/SkiDayList'
// import { SkiDayCount } from './components/SkiDayCount'

//main rendering file

// window.React = React

// render(
	// <Router history= {hashHistory}> 
	// 	<Route path="/" component={App} />
	// 	<Route path="list-days" component = {App} >
	// 		<Route path = ":filter" component = {App} />
	// 	</Route>
	// 	<Route path="add-day" component = {App} />
	// 	<Route path="*" component={Whoops404} />
	// </Router>,
// 	<h1>Hello World</h1>,	
// 	document.getElementById('col-sm-8 text-left')
// )

// render(
// 	<SkiDayCount total = {50} />, 
// 	document.getElementById('react-container')
// )



// SkiDayList days= {
// 	[
// 		{
// 			resort: "Squaw Valley",
// 			date: new Date("1/2/2016"),
// 			powder: true,
// 			backcountry: false
// 		},
// 		{
// 			resort: "Kirkwood",
// 			date: new Date("3/28/2016"),
// 			powder: false,
// 			backcountry: false
// 		},
// 		{
// 			resort: "Mt. Tallac",
// 			date: new Date("4/2/2016"),
// 			powder: false,
// 			backcountry: true
// 		}
// 	]
// }

'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}


const domContainer = document.querySelector('#col-sm-8 text-left');
ReactDOM.render(e(LikeButton), domContainer);