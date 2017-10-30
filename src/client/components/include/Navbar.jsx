import React, { PropTypes } from 'react';
import { Link } from 'react-router';

/**
 * Navigation Bar
 *
 * @param {Object} props {
 *   username, logout, accessClass, getDocuments, getProfile, getUserDocuments }
 * @returns {Object} jsx object
 */
const Navbar = ({
  username,
  logout,
  accessClass,
  getDocuments,
  getProfile,
  getUserDocuments,
  categories,
  getCategoryDocuments,
}) => (
  <header className={`navbar-fixed ${accessClass}`}>
    <nav>
      <div className="nav-wrapper container">
        <Link to="" onClick={getDocuments} className="brand-logo hide-on-med-and-down">
          PyDMS
        </Link>

        <ul className="right">
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link className="dropdown-button" to="" data-activates="category-dropdown">
              categories<i className="material-icons right">arrow_drop_down</i>
            </Link>
          </li>
          <span className="notLoggedIn">
            <li>
              <Link id="login" to="login">
                Login
              </Link>
            </li>
            <li>
              <Link id="signup" to="signup">
                SignUp
              </Link>
            </li>
          </span>
          <span className="forAdmin">
            <li>
              <Link to="user">Users</Link>
            </li>
            <li>
              <Link to="role">Roles</Link>
            </li>
          </span>
          <span className="loggedIn">
            <li>
              <Link className="dropdown-button" to="" data-activates="documents-dropdown">
                Documents<i className="material-icons right">arrow_drop_down</i>
              </Link>
            </li>
            <li>
              <Link className="dropdown-button" to="" data-activates="profile-dropdown">
                <span id="userName">{username}</span>
                <i className="material-icons left">person_pin</i>
              </Link>
            </li>
          </span>
        </ul>
      </div>
    </nav>

    <div>
      <ul id="profile-dropdown" className="dropdown-content">
        <li>
          <Link to="" onClick={getProfile}>
            <i className="fa fa-user" />Profile
          </Link>
        </li>
        <li className="divider" />
        <li>
          <Link to="" onClick={logout}>
            <i className="fa fa-sign-out" />Logout
          </Link>
        </li>
      </ul>

      <ul id="documents-dropdown" className="dropdown-content">
        <li>
          <Link to="document/new">
            <i className="fa fa-plus-circle" />New Document
          </Link>
        </li>
        <li className="divider" />
        <li>
          <Link to="" onClick={getDocuments}>
            <i className="fa fa-folder-open" />View Documents
          </Link>
        </li>
        <li>
          <Link to="" onClick={getUserDocuments}>
            <i className="fa fa-book" />My Documents
          </Link>
        </li>
      </ul>

      <ul id="category-dropdown" className={`dropdown-content ${accessClass}`}>
        <span className="forAdmin">
          <li>
            <Link to="categories">Manage categories</Link>
          </li>
        </span>
        <li className="divider"/>
        <li>
          {categories.map(category => (
            <Link key={category.id} to="" onClick={() => getCategoryDocuments(category.id)}>
              {category.name}
            </Link>
          ))}
        </li>
      </ul>
    </div>
  </header>
);

Navbar.propTypes = {
  logout: PropTypes.func.isRequired,
  getProfile: PropTypes.func.isRequired,
  getDocuments: PropTypes.func.isRequired,
  getUserDocuments: PropTypes.func.isRequired,
  getCategoryDocuments: PropTypes.func.isRequired,
  username: PropTypes.string,
  accessClass: PropTypes.string.isRequired,
  categories: PropTypes.array.isRequired,
};

export default Navbar;
