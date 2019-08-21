import React, { Component } from 'react';
import WordCloud from './WordCloud';

export default class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        event.preventDefault();
    }
    render()
    {
        const element = (
            <div>
              <WordCloud />
              <form action="http://localhost:5000/result" method="get">
                  <textarea rows = "20" cols = "100" name = "place">
                  I hate google chome as the chrome is horrible at times
                  </textarea>
                  <input type="submit" value="Submit"/>
              </form>


            </div>
        );

        return element
    }
}