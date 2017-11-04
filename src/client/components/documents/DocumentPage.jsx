import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router';
import renderHTML from 'react-render-html';
import { getDocument } from '../../actions/documentActions';

/**
 * Document Page container
 *
 * @class DocumentPage
 * @extends {React.Component}
 */
class DocumentPage extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.state = {};
  }

  /**
  * Retrieves the document before rendering the component
  *
  * @returns {Undefined} nothing
  */
  componentWillMount() {
    this.props.getDocument(this.props.params.id).catch((error) => {
      if (error.response) {
        Materialize.toast('Invalid document id', 2000);
      }
      this.context.router.push('/');
    });
  }

  /**
  * Render the component
  *
  * @returns {Object} jsx object
  */
  render() {
    const { document, user } = this.props;

    return (
      <div className="document-div">
        <div className="document container">
          <h3>{document.title}</h3>
          <p className="meta-info">
            posted on: {new Date(document.createdAt).toDateString()}, by:{' '}
            <span className="teal-text">{document.user ? document.user.username : ''}</span>
          </p>
          <div>{document.content && renderHTML(document.content)}</div>
        </div>

        {user &&
          user.id === document.authorId && (
            <div className="container">
              <Link
                to={`document/${document.id}`}
                className="btn-floating waves-effect waves-light right edit-btn"
              >
                <i className="material-icons">edit</i>
              </Link>
            </div>
          )}
      </div>
    );
  }
}

DocumentPage.propTypes = {
  document: PropTypes.object.isRequired,
  getDocument: PropTypes.func.isRequired,
  params: PropTypes.object,
  user: PropTypes.object.isRequired,
};

DocumentPage.contextTypes = {
  router: PropTypes.object.isRequired,
};

export default connect(state => ({ document: state.document, user: state.access.user }), {
  getDocument,
})(DocumentPage);
