import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'
import { Link } from 'react-router-dom';

const ForumSidebar = () => {
    const groups = useSelector(state => state.groups)



    return (
        <>
            <div className='sidebar-container'>
                <div className='sidebar-links'>  
                <Link className='sidebar-link' to='/forum'>Main</Link>   
                {Object.values(groups).map((group) => {
                    return(
                        <Link className='sidebar-link' to={`/forum/${group.id}`}>{group.name}</Link>   
                    )

                })}
                </div>   
                 
            </div> 
        </>
    )
}

export default ForumSidebar