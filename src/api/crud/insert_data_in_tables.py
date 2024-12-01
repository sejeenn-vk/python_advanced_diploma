from sqlalchemy import text


data = ["insert into users (name, api_key) values ('Евгений Воронцов', 'test')",
        "insert into users (name, api_key) values ('Владимир Ульянов', 'lenin')",
        "insert into users (name, api_key) values ('Александр Пушкин', 'pushkin')",
        "insert into tweets (content, user_id, created_at) values ('Будь здоров!', 1, current_timestamp)",
        "insert into tweets (content, user_id, created_at) values ('Всегда здоров!', 3, current_timestamp)",
        "insert into tweets (content, user_id, created_at) values "
        "('Ленин жил, Ленин жив, Ленин будет жить!', 2, current_timestamp)",
        ]


async def insert_data(conn):
    for query in data:
        await conn.execute(text(query))
