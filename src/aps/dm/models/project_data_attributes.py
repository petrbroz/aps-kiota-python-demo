from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .project_extension_with_schema_link import Project_extension_with_schema_link

@dataclass
class ProjectData_attributes(AdditionalDataHolder, Parsable):
    """
    The properties of the project.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container of additional properties that extends the default properties of this resource.
    extension: Optional[Project_extension_with_schema_link] = None
    # A human friendly name to identify the project.
    name: Optional[str] = None
    # The array of scopes that apply to this project.
    scopes: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProjectData_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProjectData_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProjectData_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .project_extension_with_schema_link import Project_extension_with_schema_link

        from .project_extension_with_schema_link import Project_extension_with_schema_link

        fields: dict[str, Callable[[Any], None]] = {
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Project_extension_with_schema_link)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scopes": lambda n : setattr(self, 'scopes', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("extension", self.extension)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("scopes", self.scopes)
        writer.write_additional_data_value(self.additional_data)
    

