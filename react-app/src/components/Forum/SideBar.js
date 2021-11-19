import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import { useSelector } from 'react-redux';
import './Forum.css'
import { Link } from 'react-router-dom';

const ForumSidebar = () => {



    return (
        <>
            <div className='sidebar-container'>
                <div className='sidebar-links'>  
                    <Link className='sidebar-link' to='/forum'>Main</Link>   
                    <Link className='sidebar-link' to='/forum'>Sporting</Link>   
                    <Link className='sidebar-link' to='/forum'>Hound</Link>   
                    <Link className='sidebar-link' to='/forum'>Working</Link>   
                    <Link className='sidebar-link' to='/forum'>Terrier</Link>   
                    <Link className='sidebar-link' to='/forum'>Toy</Link>   
                    <Link className='sidebar-link' to='/forum'>Non-Sporting</Link>   
                    <Link className='sidebar-link' to='/forum'>Herding</Link> 
                </div>   
                 
            </div> 
        </>
    )
}

export default ForumSidebar