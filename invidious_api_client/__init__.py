from typing import TYPE_CHECKING

from .client import InvidiousAPIClient
from .models.instances import get_instances, choose_instance



# To not report "unused import" warnings." by linter:
if TYPE_CHECKING:
    _ = [
        InvidiousAPIClient,
        get_instances, choose_instance
    ]
