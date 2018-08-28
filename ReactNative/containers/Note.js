import shortId from 'shortid'
import React, { PureComponent } from 'react';
import { Keyboard } from 'react-native'
import { NoteDetail } from '../components/NoteDetail'
import { SaveButton } from '../components/Buttons'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import { actions } from '../redux/actions'

export class Note extends PureComponent {
  static navigationOptions = ({ navigation }) => ({
    headerRight: (
      <SaveButton onPress={navigation.getParam('onSaveNote')} />
    )
  })

  state = {
    noteText: ''
  }

  componentDidMount() {
    this.props.navigation.setParams({ onSaveNote: this.onSaveNote })
  }

  onSaveNote = () => {
    Keyboard.dismiss()

    const { projectId, noteId, note, navigation, addNote, editNote } = this.props
    const { noteText } = this.state

    if (!noteId) {
      const newNoteId = shortId.generate()
      navigation.setParams({ noteId: newNoteId })
      addNote(projectId, newNoteId, noteText)
    } else if (noteText && noteText !== note.text) {
      editNote(projectId, noteId, noteText)
    }
  }

  onChangeNote = noteText => {
    this.setState({ noteText })
  }

  render() {
    const initialTextValue = this.props.note ?
      this.props.note.text : ''
    const noteText = this.state.noteText || initialTextValue

    return (
      <NoteDetail
        noteText={noteText}
        onChangeNoteText={this.onChangeNote}
      />
    )
  }
}

const mapStateToProps = (state, ownProps) => {
  const projectId = ownProps.navigation.getParam('projectId')
  const noteId = ownProps.navigation.getParam('noteId', null)

  const project = projectId ?
    state.projects.find(project => project.id === projectId) :
    null

  const note = project ?
    project.notes.find(note => note.id === noteId) :
    null

  return {
    noteId,
    projectId,
    note
  }
}

const mapDispatchToProps = dispatch =>
  bindActionCreators(actions, dispatch)

export default connect(mapStateToProps, mapDispatchToProps)(Note)