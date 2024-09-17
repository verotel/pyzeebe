from typing import Awaitable, Callable, Union, Any

from pyzeebe import Job
from pyzeebe.job.job import JobController

DecoratorRunner = Callable[[Job, Any], Awaitable[Job]]
JobHandler = Callable[[Job, JobController], Awaitable[Job]]

SyncTaskDecorator = Callable[[Job], Job]
AsyncTaskDecorator = Callable[[Job, Any], Awaitable[Job]]
TaskDecorator = Union[SyncTaskDecorator, AsyncTaskDecorator]
