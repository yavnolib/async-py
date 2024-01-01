import abc
import asyncio
from concurrent.futures import ThreadPoolExecutor


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model

        # ThreadPool, max_workers=10: (0.368881478700132, 0.5446164381010021, rel_tol=0.3)
        # ThreadPool, max_workers=2: (0.4007899753003585, 0.5349969280996447, rel_tol=0.3)
        self.executor = ThreadPoolExecutor(max_workers=2)

    async def handle_request(self) -> None:
        # Модель выполняет некий тяжёлый код (ознакомьтесь с ним в файле тестов),
        # вам необходимо добиться его эффективного конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины handle_request не слишком сильно
        # отличается от времени исполнения нескольких таких корутин, запущенных конкурентно.
        #
        # YOU CODE GOES HERE

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(self.executor, self._model.compute)
