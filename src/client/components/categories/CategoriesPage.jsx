import React, { PropTypes } from 'react';
import TextInput from '../common/TextInput';
import DeleteModal from '../common/DeleteModal';

/**
 * CategoriesPage
 *
 * @param {Object} props { categories,
 * editCategory, newCategory, onClick, onChange, onSave, deleteCategory }
 * @returns {Object} jsx object
 */
const CategoriesPage = ({
  categories,
  editCategory,
  newCategory,
  onClick,
  onChange,
  onSave,
  deleteCategory,
}) => (
  <div className="form-div">
    <div className="container">
      <h3 className="center">Categories</h3>

      <ul className="collection">
        {categories.map(category => (
          <li className="collection-item" key={category.id}>
            {category.name}
            <span>
              <a
                href="#deleteModal"
                className="secondary-content delete-role"
                onClick={e => onClick(e, category)}
              >
                <i className="material-icons">delete</i>
              </a>
              <a
                href="#roleModal"
                onClick={e => onClick(e, category)}
                className="secondary-content edit-role"
              >
                <i className="material-icons">edit</i>
              </a>
            </span>
          </li>
        ))}
      </ul>

      <h3 className="center">Add Category</h3>
      <form onSubmit={e => onSave(e, 'new')}>
        <div className="input-field">
          <i className="fa fa-user-secret prefix" />
          <input
            id="newCategory"
            type="text"
            name="name"
            value={newCategory.name}
            onChange={e => onChange(e, 'new')}
            placeholder="Category Name"
          />
        </div>
        {newCategory.error && (
          <div className="card-panel error white-text">{newCategory.error}</div>
        )}

        <div className="input-field center">
          <button className="waves-effect btn">Submit</button>
        </div>
      </form>
    </div>

    <div id="roleModal" className="modal">
      <div className="modal-content">
        <h3 className="center">Edit Category</h3>
        <form onSubmit={onSave}>
          <TextInput
            name="name"
            label="Edit Category"
            value={editCategory.name}
            onChange={onChange}
            error={editCategory.error}
          />

          <div className="input-field center">
            <button className="waves-effect btn">Submit</button>
          </div>
        </form>
      </div>
    </div>

    <DeleteModal
      toBeDeleted={{ id: editCategory.id, title: editCategory.name }}
      deleteItem={deleteCategory}
    />
  </div>
);

CategoriesPage.propTypes = {
  categories: PropTypes.array.isRequired,
  newCategory: PropTypes.object.isRequired,
  editCategory: PropTypes.object.isRequired,
  onChange: PropTypes.func.isRequired,
  onClick: PropTypes.func.isRequired,
  onSave: PropTypes.func.isRequired,
  deleteCategory: PropTypes.func.isRequired,
};

export default CategoriesPage;
