import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'

const DisplayPosts = ({post}) => {
    const authors = useSelector(state => state.users)
    const author = Object.keys(authors).find(thisAuthor => +post.user_id === +thisAuthor)
    console.log(authors)
//     useEffect(() => {
//       dispatch(allPosts())
//   }, [dispatch]);

    const get_date = () => {
        const unformattedDate = post.posted
    }

    get_date()

    return (
        <>
            <tr>  
                <td>{authors[author].first_name}</td>
                <td>{post.title}</td>
                <td>{post.posted}</td>
                <td>comment #</td>
            </tr>  
        </>
    )
}

export default DisplayPosts