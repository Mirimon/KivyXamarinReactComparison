import React, { PureComponent } from 'react'
import PropTypes from 'prop-types'
import { StyleSheet, TextInput, View } from 'react-native'

const styles = StyleSheet.create({
  note: {
    flex: 1,
    backgroundColor: 'white',
    paddingHorizontal: 15,
    paddingVertical: 20
  },

  noteText: {
    fontSize: 16
  }
})

export class NoteDetail extends PureComponent {
  static propTypes = {
    noteText: PropTypes.string,
    onChangeNoteText: PropTypes.func
  }

  render() {
    const { noteText, onChangeNoteText } = this.props
    return (
      <View style={styles.note}>
        <TextInput
          multiline
          style={styles.noteText}
          value={noteText}
          placeholder="Type note text here ..."
          underlineColorAndroid="transparent"
          onChangeText={onChangeNoteText}
        />
      </View>
    )
  }
}