import React from 'react';

class  TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'header': '', 
            'body': '',
            'custom_user': []

        }
    }
    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value,
        })
    }
    handleSubmit(event) {
        this.props.createTodoNotes(this.state.header, this.state.body, this.state.custom_user)
        console.log(this.state.header, this.state.body, this.state.custom_user);
        event.preventDefault()
    }

    handleTodoSelect(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'custom_user': []
            })
            return;
        }

        let custom_user = []
        for(let option of event.target.selectedOptions) {
            custom_user.push(option.value)
        }
        this.setState({
            'custom_user': custom_user
        })
    }

    render() {
        return(
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type='text' name='header' placeholder='header' value={this.state.header} onChange={(event) => this.handleChange(event)}/>
                    <input type='text' name='body' placeholder='body' value={this.state.body} onChange={(event) => this.handleChange(event)}/>
                    <select onChange={(event) => this.handleTodoSelect(event)}>
                        {this.props.custom_user.map((custom_user) => <option value={custom_user.id}>{custom_user.username}</option>)}
                    </select>
                    <input type='submit' value='Create'/>
                </form>
            </div>
        )
    }
}

export default TodoForm;
