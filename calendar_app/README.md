
# Calendar app 

Микросевис для взаимдейства с онлайн календарем


## Features

- Просмотр всех доступных заметок
- Создание заметки
- Обновление заметки
- Удаление заметки
- Просмотре всех доступных календарей



## Running

Для запуска проекта запустите. P.S порт 80 должен быть свободный

```bash
  docker-compose up
```


## API Reference

#### Возращает все календари

```http
  GET /api/calendar/all
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |

#### Возращает все задчаи

```http
  GET /api/calendar/events
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |


#### Создает новую задачу

```http
  POST /api/calendar/events
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |

#### Удаляет задчу

```http
  DELETE /api/calendar/events/{eventId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `eventId` | `string` | **Required**. ID ивента |


```http
  PATCH /api/calendar/events/{eventId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `eventId` | `string` | **Required**. ID ивента |