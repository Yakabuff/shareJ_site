
import axios from 'axios';
import React, { Component } from 'react';
import Body from './Body';
import Date from './Date';
import Files from './Files';
import Version from './Version';
import '../entry.css';

class Entry extends Component{
    
    constructor(props){
        super(props)
        
        this.state = {
            date: '',
            body: '',
            version: '',
            file: ''
          };
    }

    componentDidMount(){
        axios
          .get('/api')
          .then(({ data })=> {
              this.setState({ 
              date: data.date, 
              body: data.body,
              version:data.version,
              file:data.file
            });
          })
          .catch((err)=> {});
          
      }

    render(){
        return(
            <React.Fragment>
            <p>
            <Version value = {this.state.version}></Version>
            </p>
            <p>
            <Date value = {this.state.date}></Date>
            </p>
            
            <p>
            <Body value = {this.state.body}></Body>
            <Files value = {this.state.file}></Files>
            </p>
            </React.Fragment>
            
        );
    }
}

export default Entry;