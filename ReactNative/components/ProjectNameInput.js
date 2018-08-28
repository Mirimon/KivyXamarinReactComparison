import React, { PureComponent } from 'react';
import PropTypes from 'prop-types'
import { View, TextInput, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    paddingVertical: 20,
    paddingHorizontal: 15,
    borderColor: 'black',
    borderBottomWidth: StyleSheet.hairlineWidth,
    backgroundColor: 'white'
  },
  input: {
    fontSize: 16
  }
})

export class ProjectNameInput extends PureComponent {
  static propTypes = {
    onSubmitEditing: PropTypes.func
  }

  onSubmitEditing = e => {
    this.props.onSubmitEditing(e.nativeEvent.text)
  }

  render() {
    return (
      <View style={styles.container}>
        <TextInput
          autoFocus
          placeholder="Type project name here ..."
          placeholderTextColor="gray"
          underlineColorAndroid="transparent"
          onSubmitEditing={this.onSubmitEditing} />
      </View>
    )
  }
}