import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub, faLinkedinIn } from "@fortawesome/free-brands-svg-icons"

import "./Footer.css"

const Footer = () => {



    return (
        <div className="footer-main">
          <div className="credits">
            <h3 className="footer-word">Dusty Mumphrey</h3>
            <div>
              <a href="https://github.com/Dusttoo" rel="noreferrer" target="_blank"><FontAwesomeIcon icon={faGithub} className="media"/></a>
              <a href="https://www.linkedin.com/in/dusty-mumphrey/" rel="noreferrer" target="_blank"><FontAwesomeIcon icon={faLinkedinIn} className="media" /></a>
            </div>
            
          </div>
            
      </div>
    )
}

export default Footer