const avatar_1 = require('../images/avatar_1.jpg')
const avatar_2 = require('../images/avatar_2.jpg')
const avatar_3 = require('../images/avatar_3.jpg')

const user_1 = {
  userName: 'Мурзик',
  avatar: avatar_2
}

const user_2 = {
  userName: 'Томас',
  avatar: avatar_3
}

export const currentUser = {
  userName: 'Корнелиус',
  avatar: avatar_1
}

export const initialState = {
  projects: [
    {
      id: 'project_1',
      name: 'Первый тестовый проект',
      notes: [
        {
          id: '1',
          ...user_2,
          editTime: 'Mon Aug 27 2018',
          text: 'Тестирую возможности приложения'
        }
      ]
    },
    {
      id: 'project_2',
      name: 'Кража сосиски',
      notes: [
        {
          id: '1',
          ...user_1,
          editTime: 'Sat Aug 25 2018',
          text: 'Активные действия беру на себя!'
        },
        {
          id: '2',
          ...user_2,
          editTime: 'Sun Aug 26 2018',
          text: 'Я отвлеку хозяина'
        },
        {
          id: '3',
          ...currentUser,
          editTime: 'Mon Aug 27 2018',
          text: 'Парни, в этот раз без меня. Я пока отлежусь. Позовите, если у вас все получится'
        }
      ]
    }
  ]
}