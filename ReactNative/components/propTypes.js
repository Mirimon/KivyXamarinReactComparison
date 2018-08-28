import PropTypes from 'prop-types'

export const NoteType = PropTypes.shape({
  userName: PropTypes.string,
  avatar: PropTypes.any,
  editTime: PropTypes.string,
  text: PropTypes.string
})

export const ProjectType = PropTypes.shape({
  name: PropTypes.string,
  notes: PropTypes.arrayOf(NoteType)
})

export const ProjectsType = PropTypes.arrayOf(ProjectType)