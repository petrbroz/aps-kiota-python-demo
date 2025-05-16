from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .relationship_links_data_meta import RelationshipLinks_data_meta
    from .type_link import Type_link

@dataclass
class RelationshipLinks_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ID of the resource.
    id: Optional[str] = None
    # The meta-information of the links of this resource.
    meta: Optional[RelationshipLinks_data_meta] = None
    # The type of the resource. Possible values are ``links``.
    type: Optional[Type_link] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelationshipLinks_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelationshipLinks_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelationshipLinks_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .relationship_links_data_meta import RelationshipLinks_data_meta
        from .type_link import Type_link

        from .relationship_links_data_meta import RelationshipLinks_data_meta
        from .type_link import Type_link

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(RelationshipLinks_data_meta)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_link)),
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
        writer.write_object_value("meta", self.meta)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

