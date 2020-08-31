import React, { Component } from 'react';
import ReactDOM from "react-dom";

class File extends Component{

    constructor(props){
        super(props)
    }


    render(){
        return(
            <p>{this.props.value}</p>
        );
    }
}

export default File;