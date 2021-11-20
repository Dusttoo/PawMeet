import React, { useEffect, useState }  from 'react';
import { useDispatch } from 'react-redux';
import { allPostsForGroup } from '../../store/group_posts';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import './Forum.css'
import DisplayPosts from './DisplayPost';
import { allUsers } from '../../store/users';
import { allComments } from '../../store/comments';
import ForumSidebar from './SideBar';
import { useParams } from 'react-router';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleLeft, faAngleRight } from '@fortawesome/free-solid-svg-icons';
const MainNext = ({index}) => {
    const dispatch = useDispatch()
    const {id} = useParams()
    const posts = useSelector(state => state.forum)
    const remove = 10;


    useEffect(() => {
      dispatch(allPostsForGroup(id))
      dispatch(allUsers())
      dispatch(allComments())
  }, [dispatch, id]);

    const sortedByTime = Object.values(posts).sort(function(a,b){
      return new Date(b.posted) - new Date(a.posted) 
  })

  const nextTenPosts = () => {
      return sortedByTime.splice(index, remove)

  }


    return (
        <>
            {nextTenPosts().map((post) => {
                return (
                    <DisplayPosts post={post}/>
                )
            })}
        </>
    )
}

export default MainNext