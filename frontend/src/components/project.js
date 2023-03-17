import React from 'react';

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.link_to_repository}</td>
            <td>{project.user_set}</td>
        </tr>
    )
}

const ProjectList = ({project}) => {
    return(
        <table>
            <th>NAME</th>
            <th>LINK_TO_REPOSITORY</th>
            <th>USER_SET</th>
            {project.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;