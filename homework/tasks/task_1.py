from asyncio import Task
from typing import Any, Callable, Coroutine


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        # YOUR CODE GOES HERE
        return await f()
    elif isinstance(f, Task):
        # YOUR CODE GOES HERE
        return await f
    elif isinstance(f, Coroutine):
        # YOUR CODE GOES HERE
        return await f
    else:
        raise ValueError('invalid argument')
