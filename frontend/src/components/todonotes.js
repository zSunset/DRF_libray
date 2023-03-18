import React from 'react';

const TodoNotesItem = ({todonotes}) => {
    return (
        <tr>
            <td>{todonotes.header}</td>
            <td>{todonotes.body}</td>
            <td>{todonotes.user_set}</td>
        </tr>
    )
}

const TodoNotesList = ({todonotes}) => {
    return(
        <table>
            <th>HEADER</th>
            <th>BODY</th>
            <th>USER_SET</th>
            {todonotes.map((todonotes) => <TodoNotesItem todonotes={todonotes} />)}
        </table>
    )
}

export default TodoNotesList;