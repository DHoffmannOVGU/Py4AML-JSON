from dataclasses import field
from enum import Enum
from pydantic.dataclasses import dataclass
from typing import List, Optional

__NAMESPACE__ = "https://admin-shell.io/aas/3/0"

@dataclass
class AssetAdministrationShellT:
    class Meta:
        name = "assetAdministrationShell_t"

    extensions = field(default=None)
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    id_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "idShort",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"[a-zA-Z][a-zA-Z0-9_]*",
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    administration: Optional[AdministrativeInformationT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    embedded_data_specifications: Optional[AssetAdministrationShellTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    derived_from: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "derivedFrom",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    asset_information: Optional[AssetInformationT] = field(
        default=None,
        metadata={
            "name": "assetInformation",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    submodels: Optional[AssetAdministrationShellTSubmodels] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )



@dataclass
class SubmodelT:
    class Meta:
        name = "submodel_t"

    #extensions = field(default=None)
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    id_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "idShort",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"[a-zA-Z][a-zA-Z0-9_]*",
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[SubmodelTDescription] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    administration: Optional[AdministrativeInformationT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    kind: Optional[ModellingKindT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    semantic_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "semanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    supplemental_semantic_ids: Optional[SubmodelTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[SubmodelTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[SubmodelTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_elements: Optional[SubmodelTSubmodelElements] = field(
        default=None,
        metadata={
            "name": "submodelElements",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )

@dataclass
class AdministrativeInformationT:
    class Meta:
        name = "administrativeInformation_t"

    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"(0|[1-9][0-9]*)",
        }
    )
    revision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"(0|[1-9][0-9]*)",
        }
    )
    creator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    template_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )

