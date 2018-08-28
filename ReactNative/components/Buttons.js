import React, { PureComponent } from 'react';
import Icon from '@expo/vector-icons/Ionicons'
import { StyleSheet, TouchableOpacity } from 'react-native';
import { MAX_SWIPE_DISTANCE } from "../constants";

const styles = StyleSheet.create({
  headerButton: {
    height: '100%',
    paddingHorizontal: 15,
    justifyContent: 'center'
  },

  swipeButton: {
    width: MAX_SWIPE_DISTANCE,
    height: '100%',
    alignItems: 'center',
    justifyContent: 'center'
  }
})

export class IconButton extends PureComponent {
  render() {
    const { iconName, size = 32, color, style, onPress } = this.props
    return (
      <TouchableOpacity style={style} activeOpacity={0.8} onPress={onPress}>
        <Icon name={iconName} size={size} color={color} />
      </TouchableOpacity>
    )
  }
}

export class AddButton extends PureComponent {
  render() {
    return (
      <IconButton
        style={styles.headerButton}
        iconName="md-add"
        color="white"
        onPress={this.props.onPress}
      />
    )
  }
}

export class SaveButton extends PureComponent {
  render() {
    return (
      <IconButton
        style={styles.headerButton}
        iconName="md-checkmark"
        color="white"
        onPress={this.props.onPress}
      />
    )
  }
}

export class MenuButton extends PureComponent {
  render() {
    const { style, onPress } = this.props
    return (
      <IconButton
        style={style}
        iconName="md-more"
        color="black"
        onPress={onPress}
      />
    )
  }
}

export class RemoveButton extends PureComponent {
  render() {
    return (
      <IconButton
        style={styles.swipeButton}
        iconName="md-trash"
        color="red"
        onPress={this.props.onPress}
      />
    )
  }
}