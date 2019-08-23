import React, { Component } from 'react';

export default class GetInput extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.homeCallBack = props.homeCallBack
    }

    handleSubmit(event) {

        let input_text = document.getElementById("input_textarea").value;
        input_text = input_text.replace(/\n/g, " ");
        input_text = input_text.replace(/[^0-9a-zA-Z]/g, " ");
        let proceesed_text = [];
        console.log("The text area data is captured");
        console.log(this.props.homeCallBack)
        fetch("http://"+this.props.url+":"+this.props.port+"/result?place=" + input_text).then(function (response) {
            console.log(response);
            return response.text();

        }).then(function (text) {
            console.log("The text is " + text);
            this.props.homeCallBack(text)
        }.bind(this));
        console.log("Text is " + proceesed_text)

        event.preventDefault();
    }

    render()
    {
        const element = (
            <div>
              <form onSubmit={this.handleSubmit}>
                  <textarea id="input_textarea" rows = "10" cols = "100"></textarea>
                  <input type="submit" value="Submit"/>
              </form>
            </div>
        );

        return element
    }
}