import React, { PureComponent } from 'react'
import shortid from 'shortid'
import { NoteList } from '../components/NoteList'
import { AddButton } from '../components/Buttons'
import { ProjectNameInput } from "../components/ProjectNameInput";
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import { actions } from '../redux/actions'

export class Project extends PureComponent {
  static navigationOptions = ({ navigation }) => {
    const projectId = navigation.getParam('projectId')
    return {
      title: navigation.getParam('name', ''),
      headerRight: (
        <AddButton
          onPress={() => navigation.navigate('Note', { projectId })}
        />
      )
    }
  }

  removeNote = noteId => {
    const { projectId, removeNote } = this.props
    removeNote(projectId, noteId)
  }

  navigateNote = noteId => {
    const { projectId, navigation } = this.props
    navigation.navigate('Note', { noteId, projectId })
  }

  createProject = name => {
    const newProjectId = shortid.generate()
    this.props.navigation.setParams({ projectId: newProjectId, name })
    this.props.addProject(newProjectId, name)
  }

  render() {
    const { projectId, project } = this.props

    if (!projectId) {
      return (
        <ProjectNameInput
          onSubmitEditing={this.createProject}
        />
      )
    }

    return (
      <NoteList
        notes={project.notes}
        onNavigateNote={this.navigateNote}
        onRemoveNote={this.removeNote}
      />
    )
  }
}

const mapStateToProps = (state, ownProps) => {
  const projectId = ownProps.navigation.getParam('projectId', null)
  const project = projectId ?
    state.projects.find(project => projectId === project.id) :
    null

  return {
    projectId,
    project
  }
}

const mapDispatchToProps = dispatch =>
  bindActionCreators(actions, dispatch)

export default connect(mapStateToProps, mapDispatchToProps)(Project)