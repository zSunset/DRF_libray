import React from "react";

const CustomUserItem = ({custom_user}) => {
    return (
        <tr>
            <td>
                {custom_user.username}
            </td>
            <td>
                {custom_user.first_name}
            </td>
            <td>
                {custom_user.last_name}
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
                first_name
            </th>
            <th>
                last_name
            </th>
            <th>
                email
            </th>
            {custom_user.map((custom_user) => <CustomUserItem custom_user={custom_user} />)}
        </table>
    )
}

export default CustomUserList