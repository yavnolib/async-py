import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины, затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    # YOUR CODE GOES HERE

    # coros - list of coroutins
    result = await asyncio.gather(*coros)
    # print(f'{len(result)} {result[0]=} {result[0].number=}')

    result = sorted(result, key=lambda x: x.number)
    result = "".join([i.key for i in result])
    # print(f'{result=}')

    return result
