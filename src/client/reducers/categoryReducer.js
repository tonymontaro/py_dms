import * as types from '../actions/types';
import initialState from './initialState';

/**
* Role reducer
*
* @export
* @param {Object} [state=initialState.categories] initial state
* @param {Array} action action
* @returns {Array} reduced or initial state
*/
export default function categories(state = initialState.categories, action) {
  const category = action.category;
  let newState;

  switch (action.type) {
  case types.LOAD_CATEGORIES_SUCCESS:
    return action.categories;

  case types.CREATE_CATEGORY_SUCCESS:
    newState = [...state, Object.assign({}, category)];
    return newState;

  case types.UPDATE_CATEGORY_SUCCESS:
    return [...state.filter(item => item.id !== category.id), Object.assign({}, category)];

  default:
    return state;
  }
}
