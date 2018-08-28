import React, { PureComponent } from 'react'
import { ProjectList } from '../components/ProjectList'
import { AddButton } from '../components/Buttons'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import { actions } from '../redux/actions'

export class Projects extends PureComponent {
  static navigationOptions = ({ navigation }) => ({
    headerRight: (
      <AddButton onPress={() => navigation.navigate('Project')} />
    )
  })

  navigateProject = project => {
    this.props.navigation.navigate('Project', {
      projectId: project.id,
      name: project.name
    })
  }

  render() {
    return (
      <ProjectList
        projects={this.props.projects}
        onPressProject={this.navigateProject}
      />
    )
  }
}

const mapStateToProps = state => ({
  projects: state.projects
})

const mapDispatchToProps = dispatch =>
  bindActionCreators(actions, dispatch)

export default connect(mapStateToProps, mapDispatchToProps)(Projects)