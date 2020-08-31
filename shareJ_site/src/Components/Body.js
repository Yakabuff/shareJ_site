import React, { Component } from 'react';
import ReactDOM from "react-dom";

class Body extends Component{

    constructor(props){
        super(props)
    }


    render(){
        return(
            <p>{this.props.value}</p>
        );
    }

}

export default Body;