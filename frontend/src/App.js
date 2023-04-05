import React from 'react';

import './App.css';
import axios from 'axios';
import CustomUserList from './components/customuser';
import ProjectList from './components/project';
import TodoNotesList from './components/todonotes';
import {Route, BrowserRouter, Link, Routes} from 'react-router-dom';
import Auth from './components/Auth';
import ProjectForm from './components/ProjectForm';
import TodoForm from './components/TodoNotesForms';

class  App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'custom_user': [],
            'project': [],
            'todonotes': [],
            'token': '',

        }
    }

    obtainAuthToken(login, password) {
        console.log('obtainAuthToken:', login, password)
        axios
            .post('http://127.0.0.1:8000/api-token-auth/', {
                
                    "username":login,
                    "password":password,
                
            })
            .then(response => {
                const token = response.data.token
                console.log('token:', token)
                localStorage.setItem('token', token)

                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    isAuth() {
        return !!this.state.token
    }

    componentDidMount(){
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
        
    }
    
    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return console.log('Hueva')
    }

    createProject(name, link_to_repository, user_set) {
        let headers = this.getHeaders()
        
        axios
            .post('http://127.0.0.1:8000/api/project/', {'name': name, 'link_to_repository': link_to_repository, 'user_set': user_set},{headers})
            .then(response => {
                this.getData()
            })
            .catch(error => console.log(error))
        }

    createTodoNotes(header, body, user_set) {
        let headers = this.getHeaders()
        
        axios.post('http://127.0.0.1:8000/api/todonotes/', {'header': header, 'body': body, 'user_set': user_set},{headers})
            .then(response => {
                this.getData()
            })
            .catch(error => console.log(error))
        }
    


    deleteProject(projectId) {
        let headers = this.getHeaders()
        
        axios
            .delete(`http://127.0.0.1:8000/api/project/${projectId}`, {headers})
            .then(response => {
                this.setState({project: this.state.project.filter((item) => item.id !== projectId)})
            }).catch(error => console.log(error))
        }
        
    deleteToDoNotes(todoNotesId) {
        let headers = this.getHeaders()
        axios
            .delete(`http://127.0.0.1:8000/api/todonotes/${todoNotesId}`, {headers})
            .then(response => {
                this.setState({todonotes: this.state.todonotes.filter((item) => item.id !== todoNotesId)})
            }).catch(error => console.log(error))
    }
    
    
    
    getData() {
        let headers = this.getHeaders()
        axios
            .get('http://127.0.0.1:8000/api/authors/', {headers})
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
            .get('http://127.0.0.1:8000/api/project/', {headers})
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
            .get('http://127.0.0.1:8000/api/todonotes/', {headers})
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
    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': '',
        }, this.getData)
    }
    render() {
        return(
            <div>
                <BrowserRouter>
                <nav>
                    <li> <Link to='/custom_user'>CustomUser</Link></li>
                    <li> <Link to='/project'>Project</Link></li>
                    <li> <Link to='/todonotes'>TodoNotes</Link></li>
                    <li> <Link to='/create_project'>Create Project</Link></li>
                    <li> <Link to='/create_todo_notes'>Create TodoNotes</Link></li>
                    <li> {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }</li>
                </nav>
                    <Routes>
                        <Route exact path='/custom_user' element={<CustomUserList custom_user={this.state.custom_user}/>} />
                        <Route exact path='/project' element={<ProjectList project={this.state.project}  deleteProject={(projectId) => this.deleteProject(projectId)}/>}/>
                        <Route exact path='/todonotes' element={<TodoNotesList todonotes={this.state.todonotes} deleteToDoNotes={(todoNotesId) => this.deleteToDoNotes(todoNotesId)}/>}/>
                        <Route exact path='/create_todo_notes' element={<TodoForm custom_user={this.state.custom_user} createTodoNotes={(header, body, custom_user) => this.createTodoNotes(header, body, custom_user)}/>}/>
                        <Route exact path='/create_project' element={<ProjectForm custom_user={this.state.custom_user} createProject={(name, link_to_repository, custom_user) => this.createProject(name, link_to_repository, custom_user)}/>}/>
                        <Route exact path='/login' element={<Auth obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />
                    </Routes>
                </BrowserRouter>    
            </div>
        )
    }
}

export default App;
