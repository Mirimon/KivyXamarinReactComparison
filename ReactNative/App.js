import React, { Component } from 'react';
import { createStackNavigator } from 'react-navigation'
import { Provider } from 'react-redux'
import Projects from './containers/Projects'
import Project from './containers/Project'
import Note from './containers/Note'
import { store } from './redux/store'

const Navigator = createStackNavigator({
    Projects: {
      screen: Projects
    },
    Project: {
      screen: Project
    },
    Note: {
      screen: Note
    }
  },
  {
    navigationOptions: {
      headerStyle: {
        backgroundColor: '#f4511e',
      },
      headerTintColor: '#fff'
    }
  })

export default class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Navigator />
      </Provider>
    )
  }
}