import React from 'react';

class  ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'name': '', 
            'link_to_repository': [], 
            'custom_user': []

        }
    }
    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value,
        })
    }
    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.link_to_repository, this.state.custom_user)
        console.log(this.state.name, this.state.link_to_repository, this.state.custom_user)
        event.preventDefault()
    }

    handleProjectSelect(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'custom_user': []
            })
            return;
        }

        let custom_user = {}
        for(let option of event.target.selectedOptions) {
            custom_user.push(option.index)
        }
        this.setState({
            'custom_user': custom_user
        })
    }

    render() {
        return(
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type='text' name='name' placeholder='name' value={this.state.name} onChange={(event) => this.handleChange(event)}/>
                    <input type='text' name='link_to_repository' placeholder='link_to_repository' value={this.state.link_to_repository} onChange={(event) => this.handleChange(event)}/>
                    <select multiple onChange={(event) => this.handleProjectSelect(event)}>
                        {this.props.custom_user.map((custom_user) => <option value={custom_user.id}>{custom_user.first_name} {custom_user.last_name}</option>)}
                    </select>
                    <input type='submit' value='Create'/>
                </form>
            </div>
        )
    }
}

export default ProjectForm;
