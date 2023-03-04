import React from "react";

const CustomUserItem = ({custom_user}) => {
    return (
        <tr>
            <td>
                {custom_user.username}
            </td>
            <td>
                {custom_user.firstname}
            </td>
            <td>
                {custom_user.lastname}
            </td>
            <td>
                {custom_user.email}
            </td>
        </tr>
    )
}

const CustomUserList = ({custom_user}) => {
    return (
        <table>
            <th>
                username
            </th>
            <th>
                firstname
            </th>
            <th>
                lastname
            </th>
            <th>
                email
            </th>
            {custom_user.map((custom_user) => <CustomUserItem custom_user={custom_user} />)}
        </table>
    )
}

export default CustomUserList