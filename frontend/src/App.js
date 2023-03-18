import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import CustomUserList from './components/customuser';
import ProjectList from './components/project';
import TodoNotesList from './components/todonotes';
import {Route, BrowserRouter, Link, Routes} from 'react-router-dom';

class  App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'custom_user' : [],
            'project' : [],
            'todonotes' : [],

        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/appuser/')
            .then(response => {
                const custom_user = response.data
                    this.setState(
                    {
                        'custom_user': custom_user
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/project/')
            .then(response => {
                const project = response.data
                    this.setState(
                    {
                        'project': project
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/todonotes/')
            .then(response => {
                const todonotes = response.data
                    this.setState(
                    {
                        'todonotes': todonotes
                    }
                )
            })
            .catch(error => console.log(error))
        
        
    }
    render() {
        return(
            <div>
                <BrowserRouter>
                <nav>
                    <li> <Link to='/custom_user'>CustomUser</Link></li>
                    <li> <Link to='/project'>Project</Link></li>
                    <li> <Link to='/todonotes'>TodoNotes</Link></li>
                </nav>
                    <Routes>
                        <Route exact path='/custom_user' element={<CustomUserList custom_user={this.state.custom_user}/>} />
                        <Route exact path='/project' element={<ProjectList project={this.state.project}/>} />
                        <Route exact path='/todonotes' element={<TodoNotesList todonotes={this.state.todonotes}/>} />
                    </Routes>
                </BrowserRouter>    
            </div>
        )
    }
}

export default App;
