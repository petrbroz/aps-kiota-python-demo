from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .type_folder_items_for_storage import Type_folder_items_for_storage

@dataclass
class StoragePayload_data_relationships_target_data(AdditionalDataHolder, Parsable):
    """
    Contains information about the resources related to the item or version the storage location will contain.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ID to uniquely identify the resource.
    id: Optional[str] = None
    # The type of resource the storage location is related to. Possible values are:- ``folders`` - The storage location is for a new item. - ``items``   -  The storage location is for a new version of an existing item.
    type: Optional[Type_folder_items_for_storage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StoragePayload_data_relationships_target_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StoragePayload_data_relationships_target_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StoragePayload_data_relationships_target_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .type_folder_items_for_storage import Type_folder_items_for_storage

        from .type_folder_items_for_storage import Type_folder_items_for_storage

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_folder_items_for_storage)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("id", self.id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

