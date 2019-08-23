import React, { Component } from 'react';
import ReactWordcloud from 'react-wordcloud';
class WordCloud extends Component {
    render()
    {
        let output_text = this.props.processed_text

        var output_text_json = JSON.parse(output_text);
        console.log("Greetings from wordCloud " + output_text_json)
        return(
            <div style={{backgroundColor: 'white'}}>
              <ReactWordcloud words={output_text_json} />
            </div>
       )
    }
}

export default WordCloud
