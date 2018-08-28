import React, { PureComponent } from 'react';
import PropTypes from 'prop-types'
import { ProjectsType } from './propTypes'
import { FlatList } from 'react-native';
import { ProjectListItem } from './ProjectListItem'

export class ProjectList extends PureComponent {
  static propTypes = {
    projects: ProjectsType,
    onPressProject: PropTypes.func
  }

  renderItem = ({ item }) => (
    <ProjectListItem
      project={item}
      onPressProject={this.props.onPressProject}
    />
  )

  render() {
    return (
      <FlatList
        data={this.props.projects}
        keyExtractor={item => item.id}
        renderItem={this.renderItem}
      />
    )
  }
}