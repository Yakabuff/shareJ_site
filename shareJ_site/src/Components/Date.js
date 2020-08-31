import React, { Component } from 'react';
import ReactDOM from "react-dom";

class Date extends Component{

    constructor(props){
        super(props)
    }


    render(){
        return(
            <h4>{this.props.value}</h4>
        );
    }

}

export default Date;