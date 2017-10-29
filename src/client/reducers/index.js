import { combineReducers } from 'redux';
import { documents, document } from './documentReducer';
import access from './accessReducer';
import users from './userReducer';
import roles from './roleReducer';
import categories from './categoryReducer';
import pagination from './paginationReducer';
import ajaxCallsInProgress from './ajaxStatusReducer';

const rootReducer = combineReducers({
  documents,
  access,
  users,
  roles,
  categories,
  document,
  pagination,
  ajaxCallsInProgress,
});

export default rootReducer;
