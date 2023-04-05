import React from 'react';

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.link_to_repository}</td>
            <td>{project.user_set}</td>
            <td><button onClick={() => deleteProject(project.id)} type='button'>DELETE</button></td>
        </tr>
    )
}

const ProjectList = ({project, deleteProject}) => {
    return(
        <table>
            <th>ID</th>
            <th>NAME</th>
            <th>LINK_TO_REPOSITORY</th>
            <th>USER_SET</th>
            {project.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
    )
}

export default ProjectList;