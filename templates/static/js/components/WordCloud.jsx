import React, { Component } from 'react';
class WordCloud extends Component {
    render()
    {
        let temp = '{{input}}'
        console.log(temp)
        return(
            <div>
                <h2>The current time is {new Date().toLocaleTimeString()}.</h2>
            </div>
       )
    }
}

export default WordCloud
