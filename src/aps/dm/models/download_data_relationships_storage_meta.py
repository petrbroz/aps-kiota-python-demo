from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_link import Json_api_link

@dataclass
class DownloadData_relationships_storage_meta(AdditionalDataHolder, Parsable):
    """
    Meta information about the storage location of the download.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object containing the hyperlink to the referenced resource.
    link: Optional[Json_api_link] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadData_relationships_storage_meta:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadData_relationships_storage_meta
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadData_relationships_storage_meta()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_link import Json_api_link

        from .json_api_link import Json_api_link

        fields: dict[str, Callable[[Any], None]] = {
            "link": lambda n : setattr(self, 'link', n.get_object_value(Json_api_link)),
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
        writer.write_object_value("link", self.link)
        writer.write_additional_data_value(self.additional_data)
    

