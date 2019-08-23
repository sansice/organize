import React, { Component } from 'react';
import Header from './Header';
import GetInput from './GetInput';
import WordCloud from './WordCloud';

export default class Home extends Component {
    constructor(props) {
        super(props);
        this.set_proceesed_text = this.set_proceesed_text.bind(this);
        this.state = {processed_text: '[{"text": "", "value": 11}]'};
    };

    set_proceesed_text(text){
        return this.setState({processed_text : text});
    }
    render()
    {
        let root = document.getElementById('content');
        let url = root.getAttribute('data-url')
        let port = root.getAttribute('data-port')

        console.log(url)

        const element = (
            <div>
                <Header />
                <GetInput url={url} port={port} homeCallBack={this.set_proceesed_text} />
                <WordCloud processed_text={this.state.processed_text} />
            </div>
        );
        return element
    }
}