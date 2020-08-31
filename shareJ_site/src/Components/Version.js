import React, { Component } from 'react';
import ReactDOM from "react-dom";

class Version extends Component{

    constructor(props){
        super(props)
    }


    render(){
        return(
            <h1>{this.props.value}</h1>
        );
    }

}

export default Version;