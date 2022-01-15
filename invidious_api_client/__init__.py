from typing import TYPE_CHECKING

from .client import InvidiousClient
from .models.instances import get_instances, choose_instance



# To not report "unused import" warnings." by linter:
if TYPE_CHECKING:
    _ = [
        InvidiousClient,
        get_instances, choose_instance
    ]
