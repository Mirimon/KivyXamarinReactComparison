import React, { PureComponent } from 'react'
import PropTypes from 'prop-types'
import { ProjectType } from './propTypes'
import { StyleSheet, TouchableOpacity, Text, View } from 'react-native';

const styles = StyleSheet.create({
  project: {
    paddingVertical: 30,
    paddingHorizontal: 15,
    backgroundColor: 'white',
    borderBottomWidth: StyleSheet.hairlineWidth,
    borderColor: 'gray'
  },
  name: {
    fontSize: 16
  }
})

export class ProjectListItem extends PureComponent {
  static propTypes = {
    project: ProjectType,
    onPressProject: PropTypes.func
  }

  onPressProject = () => {
    const { project, onPressProject } = this.props
    onPressProject(project)
  }

  render() {
    return (
      <TouchableOpacity onPress={this.onPressProject}>
        <View style={styles.project}>
          <Text style={styles.name}>{this.props.project.name}</Text>
        </View>
      </TouchableOpacity>
    )
  }
}