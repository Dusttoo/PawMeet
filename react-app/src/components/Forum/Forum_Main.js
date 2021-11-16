import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPosts } from '../../store/forum';
import './Forum.css'

const ForumHome = () => {
    const dispatch = useDispatch()

    useEffect(() => {
      dispatch(allPosts())
  }, [dispatch]);

    return (
        <h1>Forum</h1>
    )
}

export default ForumHome