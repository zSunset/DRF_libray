import React from 'react';

const TodoNotesItem = ({todonotes, deleteToDoNotes}) => {
    return (
        <tr>
            <td>{todonotes.id}</td>
            <td>{todonotes.header}</td>
            <td>{todonotes.body}</td>
            <td>{todonotes.user_set}</td>
            <td><button onClick={() => deleteToDoNotes(todonotes.id)} type='button'>DELETE</button></td>
        </tr>
    )
}

const TodoNotesList = ({todonotes, deleteToDoNotes}) => {
    return(
        <table>
            <th>ID</th>
            <th>HEADER</th>
            <th>BODY</th>
            <th>USER_SET</th>
            {todonotes.map((todonotes) => <TodoNotesItem todonotes={todonotes} deleteToDoNotes={deleteToDoNotes}/>)}
        </table>
    )
}

export default TodoNotesList;