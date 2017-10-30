import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import CategoriesPage from './CategoriesPage';
import { saveCategory, deleteCategory, getCategories } from '../../actions/categoryActions';
import { validateRequiredFields } from '../../utilities/validator';
import { handleError } from '../../utilities/errorHandler';

/**
 * Manage category container
 *
 * @class ManageCategories
 * @extends {React.Component}
 */
class ManageCategories extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      categories: [...props.categories],
      editCategory: { name: '', id: '', error: '' },
      newCategory: { name: '', error: '' },
    };
    this.deleteCategory = this.deleteCategory.bind(this);
    this.onSave = this.onSave.bind(this);
    this.onChange = this.onChange.bind(this);
    this.onClick = this.onClick.bind(this);
  }

  /**
  * Assigns updated categories state to class state
  *
  * @param {Object} nextProps
  * @returns {Undefined} nothing
  */
  componentWillReceiveProps(nextProps) {
    if (this.props.categories !== nextProps.categories) {
      this.setState({ categories: [...nextProps.categories] });
    }
  }

  /**
  * Initiates the modal after rendering the component
  *
  * @returns {Undefined} nothing
  */
  componentDidMount() {
    $('.modal').modal();
  }

  /**
  * Retrieve categories before redering the component
  *
  * @returns {Undefined} nothing
  */
  componentWillMount() {
    this.props.getCategories();
  }

  /**
  * Delete the category
  *
   @param {Object} id category id
  * @returns {Undefined} nothing
  */
  deleteCategory(id) {
    this.props.deleteCategory(id).then(() => {
      this.props.getCategories().then(() => Materialize.toast('Category deleted', 2000));
    });
  }

  /**
  * Control input fields
  *
  * @param {Object} event
  * @param {String} type type of change
  * @returns {Undefined} nothing
  */
  onChange(event, type) {
    if (type === 'new') return this.setState({ newCategory: { name: event.target.value } });
    return this.setState({
      editCategory: Object.assign({}, this.state.editCategory, { name: event.target.value }),
    });
  }

  /**
  * Set the category to be edited to state
  *
  * @param {Object} event
  * @param {String} category
  * @returns {Undefined} nothing
  */
  onClick(event, category) {
    this.setState({ editCategory: category });
  }

  /**
  * Validate input fields and submit the form
  *
  * @param {Object} event
  * @param {String} type type of change
  * @returns {Object} state
  */
  onSave(event, type) {
    event.preventDefault();
    if (type === 'new') {
      const { valid, errors } = validateRequiredFields([this.state.newCategory.name], ['name']);

      if (valid) {
        return this.props
          .saveCategory(this.state.newCategory)
          .then(() => {
            this.setState({ newCategory: { name: '' } });
            Materialize.toast('Category created', 2000);
          })
          .catch(error => handleError(error));
      }
      return this.setState({ newCategory: { name: '', error: errors.name } });
    }

    const { valid, errors } = validateRequiredFields([this.state.editCategory.name], ['name']);

    if (valid) {
      return this.props
        .saveCategory(this.state.editCategory)
        .then(() => {
          $('#roleModal').modal('close');
          Materialize.toast('Category updated', 2000);
        })
        .catch(error => handleError(error));
    }

    return this.setState({
      editCategory: Object.assign({}, this.state.editCategory, { error: errors.name }),
    });
  }

  /**
  * Render the component
  *
  * @returns {Object} jsx component
   */
  render() {
    const { categories, editCategory, newCategory } = this.state;

    return (
      <CategoriesPage
        categories={categories}
        editCategory={editCategory}
        onClick={this.onClick}
        onChange={this.onChange}
        newCategory={newCategory}
        onSave={this.onSave}
        deleteCategory={this.deleteCategory}
      />
    );
  }
}

ManageCategories.propTypes = {
  categories: PropTypes.array.isRequired,
  deleteCategory: PropTypes.func.isRequired,
  getCategories: PropTypes.func.isRequired,
  saveCategory: PropTypes.func.isRequired,
};

export default connect(
  state => ({
    access: state.access,
    categories: state.categories,
  }),
  { saveCategory, deleteCategory, getCategories },
)(ManageCategories);
