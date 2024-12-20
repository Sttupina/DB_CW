from database.connect import create_connection, create_slave_connection, close_connection
from schemas.type import Brand
import asyncio

async def get_all_types():
    conn = await create_slave_connection()
    try:
        query = """
            SELECT name FROM type
        """
        types = await conn.fetch(query)
        result = [type['name'] for type in types]
        return result
    finally:
        await close_connection(conn)

async def add_new_type(type: Brand):
    conn = await create_connection()
    try:
        query = """
            INSERT INTO type (name, description) VALUES ($1, $2)
        """
        await conn.execute(query, type.name, type.description)
    finally:
        await close_connection(conn)

async def type_unique_checking(type: Brand) -> bool:
    conn = await create_slave_connection()
    try:
        query = """
            SELECT type_id FROM type WHERE name = $1
        """
        result = await conn.fetchrow(query, type.name)
        if result is not None:
            return False
        return True
    finally:
        await close_connection(conn)

