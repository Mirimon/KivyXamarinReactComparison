import { actionTypes } from './actions'
import { combineReducers } from 'redux'

function updateProject(projects, projectId, updater) {
  return projects.map(project => {
    if (project.id === projectId) {
      return updater(project)
    }
    return project
  })
}

function updateNotes(projects, projectId, updater) {
  return updateProject(projects, projectId, project => ({
    ...project,
    notes: updater(project.notes)
  }))
}

export function user(state = {}, action) {
  switch (action.type) {
    default:
      return state
  }
}

export function projects(state = [], action) {
  switch (action.type) {
    case actionTypes.PROJECT_ADDED: {
      const { id, name } = action.payload
      return state.concat({ id, name, notes: [] })
    }
    case actionTypes.PROJECT_REMOVED: {
      return state.filter(project => project.id !== action.payload.id)
    }
    case actionTypes.NOTE_ADDED: {
      const { projectId, note } = action.payload
      return updateNotes(state, projectId, notes =>
        notes.concat(note)
      )
    }
    case actionTypes.NOTE_EDITED: {
      const { projectId, note: changedNote } = action.payload
      return updateNotes(state, projectId, notes =>
        notes.map(note => note.id === changedNote.id ? changedNote : note)
      )
    }
    case actionTypes.NOTE_REMOVED: {
      const { projectId, noteId } = action.payload
      return updateNotes(state, projectId, notes =>
        notes.filter(note => note.id !== noteId)
      )
    }
    default:
      return state
  }
}

export const reducer = combineReducers({
  projects,
  user
})