import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import CustomUserList from './components/customuser';

class  App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'custom_user' : []
        }
    }

    componentDidMount() {
      axios.get('http://127.0.0.1:8000/appuser/')
          .then(response => {
              const custom_user = response.data
                  this.setState(
                  {
                      'custom_user': custom_user
                  }
              )
          }).catch(error => console.log(error))
    }
    render() {
        return(
          <div>
              <CustomUserList custom_user={this.state.custom_user}/>
          </div>
        )
    }
}

export default App;
