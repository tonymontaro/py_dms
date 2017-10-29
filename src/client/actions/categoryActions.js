import axios from 'axios';
import * as types from './types';
import { beginAjaxCall } from './ajaxStatusActions';
import { handleError, throwError } from '../utilities/errorHandler';

/**
* get categories
*
* @returns {Object} dispatch object
*/
export function getCategories() {
  return (dispatch) => {
    dispatch(beginAjaxCall());

    return axios
      .get(`${types.URL}/categories`)
      .then((res) => {
        dispatch({
          type: types.LOAD_CATEGORIES_SUCCESS,
          categories: res.data,
        });
      })
      .catch(error => handleError(error, dispatch));
  };
}

/**
* Save a category
*
* @param {String} category
* @returns {Object} dispatch object
*/
export function saveCategory(category) {
  if (category.id) {
    return (dispatch) => {
      dispatch(beginAjaxCall());

      return axios
        .put(`${types.URL}/categories/${category.id}`, category)
        .then((res) => {
          dispatch({ type: types.UPDATE_CATEGORY_SUCCESS, category: res.data });
        })
        .catch(error => throwError(error, dispatch));
    };
  }

  return (dispatch) => {
    dispatch(beginAjaxCall());

    return axios
      .post(`${types.URL}/categories`, category)
      .then((res) => {
        dispatch({ type: types.CREATE_CATEGORY_SUCCESS, category: res.data });
      })
      .catch(error => throwError(error, dispatch));
  };
}

/**
* Delete a category
*
* @param {String} id category id
* @returns {Object} dispatch object
*/
export function deletecategory(id) {
  return (dispatch) => {
    dispatch(beginAjaxCall());

    return axios
      .delete(`${types.URL}categories/${id}`)
      .then(() => {
        dispatch({
          type: types.DELETE_CATEGORY_SUCCESS,
        });
      })
      .catch(error => handleError(error, dispatch));
  };
}
