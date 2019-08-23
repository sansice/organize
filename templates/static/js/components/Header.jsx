import React, { Component } from 'react';
class Header extends Component {
    render()
    {
        return(
            <div>
                <h1>This is a simple Flask App with React Front </h1>
                <h2>The current time is {new Date().toLocaleTimeString()}.</h2>
            </div>
       )
    }
}

export default Header
