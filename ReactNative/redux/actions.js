import { currentUser } from './testData'

export const actionTypes = {
  PROJECT_ADDED: 'PROJECT_ADDED',
  PROJECT_REMOVED: 'PROJECT_REMOVED',

  NOTE_ADDED: 'NOTE_ADDED',
  NOTE_EDITED: 'NOTE_EDITED',
  NOTE_REMOVED: 'NOTE_REMOVED'
}

export const actions = {
  addProject: (id, name) => ({
    type: actionTypes.PROJECT_ADDED,
    payload: { id, name }
  }),

  removeProject: (id) => ({
    type: actionTypes.PROJECT_REMOVED,
    payload: { id }
  }),

  addNote: (projectId, noteId, text = '') => ({
    type: actionTypes.NOTE_ADDED,
    payload: {
      projectId,
      note: {
        id: noteId,
        ...currentUser,
        editTime: new Date().toDateString(),
        text
      }
    }
  }),

  editNote: (projectId, noteId, text) => ({
    type: actionTypes.NOTE_EDITED,
    payload: {
      projectId,
      note: {
        id: noteId,
        ...currentUser,
        editTime: new Date().toDateString(),
        text
      }
    }
  }),

  removeNote: (projectId, noteId) => ({
    type: actionTypes.NOTE_REMOVED,
    payload: { projectId, noteId }
  })

}