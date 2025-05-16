from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .modify_folder_payload_data_relationships_parent_data import ModifyFolderPayload_data_relationships_parent_data

@dataclass
class ModifyFolderPayload_data_relationships_parent(AdditionalDataHolder, Parsable):
    """
    Information about the parent folder of this folder.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container for the data that defines the parent of this folder.
    data: Optional[ModifyFolderPayload_data_relationships_parent_data] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModifyFolderPayload_data_relationships_parent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModifyFolderPayload_data_relationships_parent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModifyFolderPayload_data_relationships_parent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .modify_folder_payload_data_relationships_parent_data import ModifyFolderPayload_data_relationships_parent_data

        from .modify_folder_payload_data_relationships_parent_data import ModifyFolderPayload_data_relationships_parent_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(ModifyFolderPayload_data_relationships_parent_data)),
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
        writer.write_object_value("data", self.data)
        writer.write_additional_data_value(self.additional_data)
    

