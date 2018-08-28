import { createStore } from 'redux'
import { reducer } from './reducer'
import { initialState } from './testData'

export const store = createStore(reducer, initialState)