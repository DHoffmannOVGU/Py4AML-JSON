from dataclasses import field
from enum import Enum
from pydantic.dataclasses import dataclass
from typing import List, Optional

__NAMESPACE__ = "https://admin-shell.io/aas/3/0"


class AasSubmodelElementsT(Enum):
    ANNOTATED_RELATIONSHIP_ELEMENT = "AnnotatedRelationshipElement"
    BASIC_EVENT_ELEMENT = "BasicEventElement"
    BLOB = "Blob"
    CAPABILITY = "Capability"
    DATA_ELEMENT = "DataElement"
    ENTITY = "Entity"
    EVENT_ELEMENT = "EventElement"
    FILE = "File"
    MULTI_LANGUAGE_PROPERTY = "MultiLanguageProperty"
    OPERATION = "Operation"
    PROPERTY = "Property"
    RANGE = "Range"
    REFERENCE_ELEMENT = "ReferenceElement"
    RELATIONSHIP_ELEMENT = "RelationshipElement"
    SUBMODEL_ELEMENT = "SubmodelElement"
    SUBMODEL_ELEMENT_LIST = "SubmodelElementList"
    SUBMODEL_ELEMENT_COLLECTION = "SubmodelElementCollection"


@dataclass
class AbstractLangStringT:
    class Meta:
        name = "abstractLangString_t"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){2})?|[a-zA-Z]{4}|[a-zA-Z]{5,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-(([a-zA-Z0-9]){5,8}|[0-9]([a-zA-Z0-9]){3}))*(-[0-9A-WY-Za-wy-z](-([a-zA-Z0-9]){2,8})+)*(-[xX](-([a-zA-Z0-9]){1,8})+)?|[xX](-([a-zA-Z0-9]){1,8})+|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


class AssetKindT(Enum):
    TYPE = "Type"
    INSTANCE = "Instance"
    NOT_APPLICABLE = "NotApplicable"


@dataclass
class DataSpecificationContentT:
    class Meta:
        name = "dataSpecificationContent_t"


class DataTypeDefXsdT(Enum):
    XS_ANY_URI = "xs:anyURI"
    XS_BASE64_BINARY = "xs:base64Binary"
    XS_BOOLEAN = "xs:boolean"
    XS_BYTE = "xs:byte"
    XS_DATE = "xs:date"
    XS_DATE_TIME = "xs:dateTime"
    XS_DECIMAL = "xs:decimal"
    XS_DOUBLE = "xs:double"
    XS_DURATION = "xs:duration"
    XS_FLOAT = "xs:float"
    XS_G_DAY = "xs:gDay"
    XS_G_MONTH = "xs:gMonth"
    XS_G_MONTH_DAY = "xs:gMonthDay"
    XS_G_YEAR = "xs:gYear"
    XS_G_YEAR_MONTH = "xs:gYearMonth"
    XS_HEX_BINARY = "xs:hexBinary"
    XS_INT = "xs:int"
    XS_INTEGER = "xs:integer"
    XS_LONG = "xs:long"
    XS_NEGATIVE_INTEGER = "xs:negativeInteger"
    XS_NON_NEGATIVE_INTEGER = "xs:nonNegativeInteger"
    XS_NON_POSITIVE_INTEGER = "xs:nonPositiveInteger"
    XS_POSITIVE_INTEGER = "xs:positiveInteger"
    XS_SHORT = "xs:short"
    XS_STRING = "xs:string"
    XS_TIME = "xs:time"
    XS_UNSIGNED_BYTE = "xs:unsignedByte"
    XS_UNSIGNED_INT = "xs:unsignedInt"
    XS_UNSIGNED_LONG = "xs:unsignedLong"
    XS_UNSIGNED_SHORT = "xs:unsignedShort"


class DataTypeIec61360T(Enum):
    DATE = "DATE"
    STRING = "STRING"
    STRING_TRANSLATABLE = "STRING_TRANSLATABLE"
    INTEGER_MEASURE = "INTEGER_MEASURE"
    INTEGER_COUNT = "INTEGER_COUNT"
    INTEGER_CURRENCY = "INTEGER_CURRENCY"
    REAL_MEASURE = "REAL_MEASURE"
    REAL_COUNT = "REAL_COUNT"
    REAL_CURRENCY = "REAL_CURRENCY"
    BOOLEAN = "BOOLEAN"
    IRI = "IRI"
    IRDI = "IRDI"
    RATIONAL = "RATIONAL"
    RATIONAL_MEASURE = "RATIONAL_MEASURE"
    TIME = "TIME"
    TIMESTAMP = "TIMESTAMP"
    FILE = "FILE"
    HTML = "HTML"
    BLOB = "BLOB"


class DirectionT(Enum):
    INPUT = "input"
    OUTPUT = "output"


class EntityTypeT(Enum):
    CO_MANAGED_ENTITY = "CoManagedEntity"
    SELF_MANAGED_ENTITY = "SelfManagedEntity"


class KeyTypesT(Enum):
    ANNOTATED_RELATIONSHIP_ELEMENT = "AnnotatedRelationshipElement"
    ASSET_ADMINISTRATION_SHELL = "AssetAdministrationShell"
    BASIC_EVENT_ELEMENT = "BasicEventElement"
    BLOB = "Blob"
    CAPABILITY = "Capability"
    CONCEPT_DESCRIPTION = "ConceptDescription"
    DATA_ELEMENT = "DataElement"
    ENTITY = "Entity"
    EVENT_ELEMENT = "EventElement"
    FILE = "File"
    FRAGMENT_REFERENCE = "FragmentReference"
    GLOBAL_REFERENCE = "GlobalReference"
    IDENTIFIABLE = "Identifiable"
    MULTI_LANGUAGE_PROPERTY = "MultiLanguageProperty"
    OPERATION = "Operation"
    PROPERTY = "Property"
    RANGE = "Range"
    REFERABLE = "Referable"
    REFERENCE_ELEMENT = "ReferenceElement"
    RELATIONSHIP_ELEMENT = "RelationshipElement"
    SUBMODEL = "Submodel"
    SUBMODEL_ELEMENT = "SubmodelElement"
    SUBMODEL_ELEMENT_COLLECTION = "SubmodelElementCollection"
    SUBMODEL_ELEMENT_LIST = "SubmodelElementList"


@dataclass
class LangStringDefinitionTypeIec61360T:
    class Meta:
        name = "langStringDefinitionTypeIec61360_t"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){2})?|[a-zA-Z]{4}|[a-zA-Z]{5,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-(([a-zA-Z0-9]){5,8}|[0-9]([a-zA-Z0-9]){3}))*(-[0-9A-WY-Za-wy-z](-([a-zA-Z0-9]){2,8})+)*(-[xX](-([a-zA-Z0-9]){1,8})+)?|[xX](-([a-zA-Z0-9]){1,8})+|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class LangStringNameTypeT:
    class Meta:
        name = "langStringNameType_t"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){2})?|[a-zA-Z]{4}|[a-zA-Z]{5,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-(([a-zA-Z0-9]){5,8}|[0-9]([a-zA-Z0-9]){3}))*(-[0-9A-WY-Za-wy-z](-([a-zA-Z0-9]){2,8})+)*(-[xX](-([a-zA-Z0-9]){1,8})+)?|[xX](-([a-zA-Z0-9]){1,8})+|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class LangStringPreferredNameTypeIec61360T:
    class Meta:
        name = "langStringPreferredNameTypeIec61360_t"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){2})?|[a-zA-Z]{4}|[a-zA-Z]{5,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-(([a-zA-Z0-9]){5,8}|[0-9]([a-zA-Z0-9]){3}))*(-[0-9A-WY-Za-wy-z](-([a-zA-Z0-9]){2,8})+)*(-[xX](-([a-zA-Z0-9]){1,8})+)?|[xX](-([a-zA-Z0-9]){1,8})+|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class LangStringShortNameTypeIec61360T:
    class Meta:
        name = "langStringShortNameTypeIec61360_t"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){2})?|[a-zA-Z]{4}|[a-zA-Z]{5,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-(([a-zA-Z0-9]){5,8}|[0-9]([a-zA-Z0-9]){3}))*(-[0-9A-WY-Za-wy-z](-([a-zA-Z0-9]){2,8})+)*(-[xX](-([a-zA-Z0-9]){1,8})+)?|[xX](-([a-zA-Z0-9]){1,8})+|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class LangStringTextTypeT:
    class Meta:
        name = "langStringTextType_t"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){2})?|[a-zA-Z]{4}|[a-zA-Z]{5,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-(([a-zA-Z0-9]){5,8}|[0-9]([a-zA-Z0-9]){3}))*(-[0-9A-WY-Za-wy-z](-([a-zA-Z0-9]){2,8})+)*(-[xX](-([a-zA-Z0-9]){1,8})+)?|[xX](-([a-zA-Z0-9]){1,8})+|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class LevelTypeT:
    class Meta:
        name = "levelType_t"

    min: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    nom: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    typ: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    max: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


class ModellingKindT(Enum):
    TEMPLATE = "Template"
    INSTANCE = "Instance"


class QualifierKindT(Enum):
    VALUE_QUALIFIER = "ValueQualifier"
    CONCEPT_QUALIFIER = "ConceptQualifier"
    TEMPLATE_QUALIFIER = "TemplateQualifier"


class ReferenceTypesT(Enum):
    EXTERNAL_REFERENCE = "ExternalReference"
    MODEL_REFERENCE = "ModelReference"


@dataclass
class ResourceT:
    class Meta:
        name = "resource_t"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"file:(//((localhost|(\[((([0-9A-Fa-f]{1,4}:){6}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::([0-9A-Fa-f]{1,4}:){5}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|([0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){4}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:)?[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){3}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){2}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){2}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){4}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(([0-9A-Fa-f]{1,4}:){6}[0-9A-Fa-f]{1,4})?::)|[vV][0-9A-Fa-f]+\.([a-zA-Z0-9\-._~]|[!$&'()*+,;=]|:)+)\]|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])|([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=])*)))?/((([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?|/((([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?)",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"([!#$%&'*+\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\-.^_`|~0-9a-zA-Z])+([ \t]*;[ \t]*([!#$%&'*+\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\-.^_`|~0-9a-zA-Z])+|\"(([\t !#-\[\]-~]|[-ÿ])|\\([\t !-~]|[-ÿ]))*\"))*",
        }
    )


class StateOfEventT(Enum):
    ON = "on"
    OFF = "off"


@dataclass
class AnnotatedRelationshipElementTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AnnotatedRelationshipElementTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AssetAdministrationShellTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AssetAdministrationShellTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BasicEventElementTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BasicEventElementTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BlobTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BlobTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class CapabilityTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class CapabilityTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ConceptDescriptionTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ConceptDescriptionTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataElementTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataElementTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataSpecificationIec61360TDefinition:
    class Meta:
        global_type = False

    lang_string_definition_type_iec61360: List[LangStringDefinitionTypeIec61360T] = field(
        default_factory=list,
        metadata={
            "name": "langStringDefinitionTypeIec61360",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataSpecificationIec61360TPreferredName:
    class Meta:
        global_type = False

    lang_string_preferred_name_type_iec61360: List[LangStringPreferredNameTypeIec61360T] = field(
        default_factory=list,
        metadata={
            "name": "langStringPreferredNameTypeIec61360",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataSpecificationIec61360TShortName:
    class Meta:
        global_type = False

    lang_string_short_name_type_iec61360: List[LangStringShortNameTypeIec61360T] = field(
        default_factory=list,
        metadata={
            "name": "langStringShortNameTypeIec61360",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EventElementTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EventElementTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class FileTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class FileTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class HasKindT:
    class Meta:
        name = "hasKind_t"

    kind: Optional[ModellingKindT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class IdentifiableTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class IdentifiableTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class KeyT:
    class Meta:
        name = "key_t"

    type_value: Optional[KeyTypesT] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class MultiLanguagePropertyTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class MultiLanguagePropertyTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class MultiLanguagePropertyTValue:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class PropertyTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class PropertyTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RangeTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RangeTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferableTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferableTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceElementTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceElementTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RelationshipElementTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RelationshipElementTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementCollectionTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementCollectionTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementListTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementListTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelTDescription:
    class Meta:
        global_type = False

    lang_string_text_type: List[LangStringTextTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringTextType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelTDisplayName:
    class Meta:
        global_type = False

    lang_string_name_type: List[LangStringNameTypeT] = field(
        default_factory=list,
        metadata={
            "name": "langStringNameType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceTKeys:
    class Meta:
        global_type = False

    key: List[KeyT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceT:
    class Meta:
        name = "reference_t"

    type_value: Optional[ReferenceTypesT] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    referred_semantic_id: Optional["ReferenceT"] = field(
        default=None,
        metadata={
            "name": "referredSemanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    keys: Optional[ReferenceTKeys] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class AnnotatedRelationshipElementTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AssetAdministrationShellTSubmodels:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BasicEventElementTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BlobTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class CapabilityTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ConceptDescriptionTIsCaseOf:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataElementTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EventElementTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EventPayloadT:
    class Meta:
        name = "eventPayload_t"

    source: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    source_semantic_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "sourceSemanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    observable_reference: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "observableReference",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    observable_semantic_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "observableSemanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    topic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    subject_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "subjectId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    time_stamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"-?(([1-9][0-9][0-9][0-9]+)|(0[0-9][0-9][0-9]))-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01]))T(((([01][0-9])|(2[0-3])):[0-5][0-9]:([0-5][0-9])(\.[0-9]+)?)|24:00:00(\.0+)?)(Z|\+00:00|-00:00)",
        }
    )
    payload: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "format": "base64",
        }
    )


@dataclass
class ExtensionTRefersTo:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ExtensionTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class FileTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class HasSemanticsTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class MultiLanguagePropertyTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class PropertyTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class QualifierTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RangeTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceElementTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RelationshipElementTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SpecificAssetIdTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementCollectionTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementListTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelTSupplementalSemanticIds:
    class Meta:
        global_type = False

    reference: List[ReferenceT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ValueReferencePairT:
    class Meta:
        name = "valueReferencePair_t"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "valueId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class ExtensionT:
    class Meta:
        name = "extension_t"

    semantic_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "semanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    supplemental_semantic_ids: Optional[ExtensionTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value_type: Optional[DataTypeDefXsdT] = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    refers_to: Optional[ExtensionTRefersTo] = field(
        default=None,
        metadata={
            "name": "refersTo",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class HasSemanticsT:
    class Meta:
        name = "hasSemantics_t"

    semantic_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "semanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    supplemental_semantic_ids: Optional[HasSemanticsTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class QualifierT:
    class Meta:
        name = "qualifier_t"

    semantic_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "semanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    supplemental_semantic_ids: Optional[QualifierTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    kind: Optional[QualifierKindT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value_type: Optional[DataTypeDefXsdT] = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "valueId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class SpecificAssetIdT:
    class Meta:
        name = "specificAssetId_t"

    semantic_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "semanticId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    supplemental_semantic_ids: Optional[SpecificAssetIdTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    external_subject_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "externalSubjectId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class ValueListTValueReferencePairs:
    class Meta:
        global_type = False

    value_reference_pair: List[ValueReferencePairT] = field(
        default_factory=list,
        metadata={
            "name": "valueReferencePair",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AnnotatedRelationshipElementTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AnnotatedRelationshipElementTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AssetAdministrationShellTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AssetInformationTSpecificAssetIds:
    class Meta:
        global_type = False

    specific_asset_id: List[SpecificAssetIdT] = field(
        default_factory=list,
        metadata={
            "name": "specificAssetId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BasicEventElementTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BasicEventElementTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BlobTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BlobTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class CapabilityTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class CapabilityTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ConceptDescriptionTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataElementTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataElementTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityTSpecificAssetIds:
    class Meta:
        global_type = False

    specific_asset_id: List[SpecificAssetIdT] = field(
        default_factory=list,
        metadata={
            "name": "specificAssetId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EventElementTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EventElementTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class FileTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class FileTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class HasExtensionsTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class IdentifiableTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class MultiLanguagePropertyTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class MultiLanguagePropertyTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class PropertyTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class PropertyTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class QualifiableTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RangeTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RangeTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferableTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceElementTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceElementTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RelationshipElementTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RelationshipElementTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementCollectionTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementCollectionTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementListTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementListTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelTExtensions:
    class Meta:
        global_type = False

    extension: List[ExtensionT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelTQualifiers:
    class Meta:
        global_type = False

    qualifier: List[QualifierT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ValueListT:
    class Meta:
        name = "valueList_t"

    value_reference_pairs: Optional[ValueListTValueReferencePairs] = field(
        default=None,
        metadata={
            "name": "valueReferencePairs",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class AssetInformationT:
    class Meta:
        name = "assetInformation_t"

    asset_kind: Optional[AssetKindT] = field(
        default=None,
        metadata={
            "name": "assetKind",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    global_asset_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "globalAssetId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    specific_asset_ids: Optional[AssetInformationTSpecificAssetIds] = field(
        default=None,
        metadata={
            "name": "specificAssetIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    asset_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "assetType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    default_thumbnail: Optional[ResourceT] = field(
        default=None,
        metadata={
            "name": "defaultThumbnail",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class DataSpecificationIec61360T:
    class Meta:
        name = "dataSpecificationIec61360_t"

    preferred_name: Optional[DataSpecificationIec61360TPreferredName] = field(
        default=None,
        metadata={
            "name": "preferredName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    short_name: Optional[DataSpecificationIec61360TShortName] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    unit_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "unitId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    source_of_definition: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceOfDefinition",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    symbol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    data_type: Optional[DataTypeIec61360T] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    definition: Optional[DataSpecificationIec61360TDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueFormat",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value_list: Optional[ValueListT] = field(
        default=None,
        metadata={
            "name": "valueList",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    level_type: Optional[LevelTypeT] = field(
        default=None,
        metadata={
            "name": "levelType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class HasExtensionsT:
    class Meta:
        name = "hasExtensions_t"

    extensions: Optional[HasExtensionsTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class QualifiableT:
    class Meta:
        name = "qualifiable_t"

    qualifiers: Optional[QualifiableTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class ReferableT:
    class Meta:
        name = "referable_t"

    extensions: Optional[ReferableTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[ReferableTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[ReferableTDescription] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class EmbeddedDataSpecificationTDataSpecificationContent:
    class Meta:
        global_type = False

    data_specification_iec61360: Optional[DataSpecificationIec61360T] = field(
        default=None,
        metadata={
            "name": "dataSpecificationIec61360",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class EmbeddedDataSpecificationT:
    class Meta:
        name = "embeddedDataSpecification_t"

    data_specification: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "dataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    data_specification_content: Optional[EmbeddedDataSpecificationTDataSpecificationContent] = field(
        default=None,
        metadata={
            "name": "dataSpecificationContent",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class AdministrativeInformationTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AnnotatedRelationshipElementTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AssetAdministrationShellTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BasicEventElementTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class BlobTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class CapabilityTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ConceptDescriptionTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class DataElementTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EventElementTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class FileTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class HasDataSpecificationTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class MultiLanguagePropertyTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class PropertyTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RangeTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class ReferenceElementTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class RelationshipElementTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementCollectionTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementListTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelTEmbeddedDataSpecifications:
    class Meta:
        global_type = False

    embedded_data_specification: List[EmbeddedDataSpecificationT] = field(
        default_factory=list,
        metadata={
            "name": "embeddedDataSpecification",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class AdministrativeInformationT:
    class Meta:
        name = "administrativeInformation_t"

    embedded_data_specifications: Optional[AdministrativeInformationTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    creator: Optional[ReferenceT] = field(
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


@dataclass
class BasicEventElementT:
    class Meta:
        name = "basicEventElement_t"

    extensions: Optional[BasicEventElementTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[BasicEventElementTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[BasicEventElementTDescription] = field(
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
    supplemental_semantic_ids: Optional[BasicEventElementTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[BasicEventElementTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[BasicEventElementTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    observed: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    direction: Optional[DirectionT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    state: Optional[StateOfEventT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    message_topic: Optional[str] = field(
        default=None,
        metadata={
            "name": "messageTopic",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    message_broker: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "messageBroker",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    last_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastUpdate",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"-?(([1-9][0-9][0-9][0-9]+)|(0[0-9][0-9][0-9]))-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01]))T(((([01][0-9])|(2[0-3])):[0-5][0-9]:([0-5][0-9])(\.[0-9]+)?)|24:00:00(\.0+)?)(Z|\+00:00|-00:00)",
        }
    )
    min_interval: Optional[str] = field(
        default=None,
        metadata={
            "name": "minInterval",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"-?P((([0-9]+Y([0-9]+M)?([0-9]+D)?|([0-9]+M)([0-9]+D)?|([0-9]+D))(T(([0-9]+H)([0-9]+M)?([0-9]+(\.[0-9]+)?S)?|([0-9]+M)([0-9]+(\.[0-9]+)?S)?|([0-9]+(\.[0-9]+)?S)))?)|(T(([0-9]+H)([0-9]+M)?([0-9]+(\.[0-9]+)?S)?|([0-9]+M)([0-9]+(\.[0-9]+)?S)?|([0-9]+(\.[0-9]+)?S))))",
        }
    )
    max_interval: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxInterval",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"-?P((([0-9]+Y([0-9]+M)?([0-9]+D)?|([0-9]+M)([0-9]+D)?|([0-9]+D))(T(([0-9]+H)([0-9]+M)?([0-9]+(\.[0-9]+)?S)?|([0-9]+M)([0-9]+(\.[0-9]+)?S)?|([0-9]+(\.[0-9]+)?S)))?)|(T(([0-9]+H)([0-9]+M)?([0-9]+(\.[0-9]+)?S)?|([0-9]+M)([0-9]+(\.[0-9]+)?S)?|([0-9]+(\.[0-9]+)?S))))",
        }
    )


@dataclass
class BlobT:
    class Meta:
        name = "blob_t"

    extensions: Optional[BlobTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[BlobTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[BlobTDescription] = field(
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
    supplemental_semantic_ids: Optional[BlobTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[BlobTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[BlobTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "format": "base64",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"([!#$%&'*+\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\-.^_`|~0-9a-zA-Z])+([ \t]*;[ \t]*([!#$%&'*+\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\-.^_`|~0-9a-zA-Z])+|\"(([\t !#-\[\]-~]|[-ÿ])|\\([\t !-~]|[-ÿ]))*\"))*",
        }
    )


@dataclass
class CapabilityT:
    class Meta:
        name = "capability_t"

    extensions: Optional[CapabilityTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[CapabilityTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[CapabilityTDescription] = field(
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
    supplemental_semantic_ids: Optional[CapabilityTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[CapabilityTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[CapabilityTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class DataElementT:
    class Meta:
        name = "dataElement_t"

    extensions: Optional[DataElementTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[DataElementTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[DataElementTDescription] = field(
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
    supplemental_semantic_ids: Optional[DataElementTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[DataElementTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[DataElementTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class EventElementT:
    class Meta:
        name = "eventElement_t"

    extensions: Optional[EventElementTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[EventElementTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[EventElementTDescription] = field(
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
    supplemental_semantic_ids: Optional[EventElementTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[EventElementTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[EventElementTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class FileT:
    class Meta:
        name = "file_t"

    extensions: Optional[FileTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[FileTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[FileTDescription] = field(
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
    supplemental_semantic_ids: Optional[FileTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[FileTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[FileTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "pattern": r"file:(//((localhost|(\[((([0-9A-Fa-f]{1,4}:){6}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::([0-9A-Fa-f]{1,4}:){5}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|([0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){4}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:)?[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){3}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){2}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){2}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){4}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(([0-9A-Fa-f]{1,4}:){6}[0-9A-Fa-f]{1,4})?::)|[vV][0-9A-Fa-f]+\.([a-zA-Z0-9\-._~]|[!$&'()*+,;=]|:)+)\]|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])|([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=])*)))?/((([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?|/((([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?)",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
            "pattern": r"([!#$%&'*+\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\-.^_`|~0-9a-zA-Z])+([ \t]*;[ \t]*([!#$%&'*+\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\-.^_`|~0-9a-zA-Z])+|\"(([\t !#-\[\]-~]|[-ÿ])|\\([\t !-~]|[-ÿ]))*\"))*",
        }
    )


@dataclass
class HasDataSpecificationT:
    class Meta:
        name = "hasDataSpecification_t"

    embedded_data_specifications: Optional[HasDataSpecificationTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class MultiLanguagePropertyT:
    class Meta:
        name = "multiLanguageProperty_t"

    extensions: Optional[MultiLanguagePropertyTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[MultiLanguagePropertyTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[MultiLanguagePropertyTDescription] = field(
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
    supplemental_semantic_ids: Optional[MultiLanguagePropertyTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[MultiLanguagePropertyTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[MultiLanguagePropertyTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[MultiLanguagePropertyTValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "valueId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class PropertyT:
    class Meta:
        name = "property_t"

    extensions: Optional[PropertyTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[PropertyTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[PropertyTDescription] = field(
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
    supplemental_semantic_ids: Optional[PropertyTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[PropertyTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[PropertyTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value_type: Optional[DataTypeDefXsdT] = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value_id: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "valueId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class RangeT:
    class Meta:
        name = "range_t"

    extensions: Optional[RangeTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[RangeTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[RangeTDescription] = field(
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
    supplemental_semantic_ids: Optional[RangeTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[RangeTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[RangeTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value_type: Optional[DataTypeDefXsdT] = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    min: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    max: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class ReferenceElementT:
    class Meta:
        name = "referenceElement_t"

    extensions: Optional[ReferenceElementTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[ReferenceElementTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[ReferenceElementTDescription] = field(
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
    supplemental_semantic_ids: Optional[ReferenceElementTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[ReferenceElementTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[ReferenceElementTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class RelationshipElementT:
    class Meta:
        name = "relationshipElement_t"

    extensions: Optional[RelationshipElementTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[RelationshipElementTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[RelationshipElementTDescription] = field(
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
    supplemental_semantic_ids: Optional[RelationshipElementTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[RelationshipElementTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[RelationshipElementTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    first: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    second: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class SubmodelElementT:
    class Meta:
        name = "submodelElement_t"

    extensions: Optional[SubmodelElementTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[SubmodelElementTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[SubmodelElementTDescription] = field(
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
    supplemental_semantic_ids: Optional[SubmodelElementTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[SubmodelElementTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[SubmodelElementTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class AnnotatedRelationshipElementTAnnotations:
    class Meta:
        global_type = False

    blob: List[BlobT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    file: List[FileT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    multi_language_property: List[MultiLanguagePropertyT] = field(
        default_factory=list,
        metadata={
            "name": "multiLanguageProperty",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    property: List[PropertyT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    range: List[RangeT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    reference_element: List[ReferenceElementT] = field(
        default_factory=list,
        metadata={
            "name": "referenceElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class AssetAdministrationShellT:
    class Meta:
        name = "assetAdministrationShell_t"

    extensions: Optional[AssetAdministrationShellTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[AssetAdministrationShellTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[AssetAdministrationShellTDescription] = field(
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
class ConceptDescriptionT:
    class Meta:
        name = "conceptDescription_t"

    extensions: Optional[ConceptDescriptionTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[ConceptDescriptionTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[ConceptDescriptionTDescription] = field(
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
    embedded_data_specifications: Optional[ConceptDescriptionTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    is_case_of: Optional[ConceptDescriptionTIsCaseOf] = field(
        default=None,
        metadata={
            "name": "isCaseOf",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class IdentifiableT:
    class Meta:
        name = "identifiable_t"

    extensions: Optional[IdentifiableTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[IdentifiableTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[IdentifiableTDescription] = field(
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


@dataclass
class AnnotatedRelationshipElementT:
    class Meta:
        name = "annotatedRelationshipElement_t"

    extensions: Optional[AnnotatedRelationshipElementTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[AnnotatedRelationshipElementTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[AnnotatedRelationshipElementTDescription] = field(
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
    supplemental_semantic_ids: Optional[AnnotatedRelationshipElementTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[AnnotatedRelationshipElementTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[AnnotatedRelationshipElementTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    first: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    second: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    annotations: Optional[AnnotatedRelationshipElementTAnnotations] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class EnvironmentTAssetAdministrationShells:
    class Meta:
        global_type = False

    asset_administration_shell: List[AssetAdministrationShellT] = field(
        default_factory=list,
        metadata={
            "name": "assetAdministrationShell",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EnvironmentTConceptDescriptions:
    class Meta:
        global_type = False

    concept_description: List[ConceptDescriptionT] = field(
        default_factory=list,
        metadata={
            "name": "conceptDescription",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class SubmodelElementListTValue:
    class Meta:
        global_type = False

    relationship_element: List[RelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "relationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    annotated_relationship_element: List[AnnotatedRelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "annotatedRelationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    basic_event_element: List[BasicEventElementT] = field(
        default_factory=list,
        metadata={
            "name": "basicEventElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    blob: List[BlobT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    capability: List[CapabilityT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    entity: List["EntityT"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    file: List[FileT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    multi_language_property: List[MultiLanguagePropertyT] = field(
        default_factory=list,
        metadata={
            "name": "multiLanguageProperty",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    operation: List["OperationT"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    property: List[PropertyT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    range: List[RangeT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    reference_element: List[ReferenceElementT] = field(
        default_factory=list,
        metadata={
            "name": "referenceElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_collection: List["SubmodelElementCollectionT"] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementCollection",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_list: List["SubmodelElementListT"] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementList",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class SubmodelElementListT:
    class Meta:
        name = "submodelElementList_t"

    extensions: Optional[SubmodelElementListTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[SubmodelElementListTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[SubmodelElementListTDescription] = field(
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
    supplemental_semantic_ids: Optional[SubmodelElementListTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[SubmodelElementListTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[SubmodelElementListTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    order_relevant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "orderRelevant",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    semantic_id_list_element: Optional[ReferenceT] = field(
        default=None,
        metadata={
            "name": "semanticIdListElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    type_value_list_element: Optional[AasSubmodelElementsT] = field(
        default=None,
        metadata={
            "name": "typeValueListElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    value_type_list_element: Optional[DataTypeDefXsdT] = field(
        default=None,
        metadata={
            "name": "valueTypeListElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[SubmodelElementListTValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class SubmodelElementCollectionTValue:
    class Meta:
        global_type = False

    relationship_element: List[RelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "relationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    annotated_relationship_element: List[AnnotatedRelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "annotatedRelationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    basic_event_element: List[BasicEventElementT] = field(
        default_factory=list,
        metadata={
            "name": "basicEventElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    blob: List[BlobT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    capability: List[CapabilityT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    entity: List["EntityT"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    file: List[FileT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    multi_language_property: List[MultiLanguagePropertyT] = field(
        default_factory=list,
        metadata={
            "name": "multiLanguageProperty",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    operation: List["OperationT"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    property: List[PropertyT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    range: List[RangeT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    reference_element: List[ReferenceElementT] = field(
        default_factory=list,
        metadata={
            "name": "referenceElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_collection: List["SubmodelElementCollectionT"] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementCollection",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_list: List[SubmodelElementListT] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementList",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class SubmodelElementCollectionT:
    class Meta:
        name = "submodelElementCollection_t"

    extensions: Optional[SubmodelElementCollectionTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[SubmodelElementCollectionTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[SubmodelElementCollectionTDescription] = field(
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
    supplemental_semantic_ids: Optional[SubmodelElementCollectionTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[SubmodelElementCollectionTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[SubmodelElementCollectionTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    value: Optional[SubmodelElementCollectionTValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class OperationVariableTValue:
    class Meta:
        global_type = False

    relationship_element: Optional[RelationshipElementT] = field(
        default=None,
        metadata={
            "name": "relationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    annotated_relationship_element: Optional[AnnotatedRelationshipElementT] = field(
        default=None,
        metadata={
            "name": "annotatedRelationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    basic_event_element: Optional[BasicEventElementT] = field(
        default=None,
        metadata={
            "name": "basicEventElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    blob: Optional[BlobT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    capability: Optional[CapabilityT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    entity: Optional["EntityT"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    file: Optional[FileT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    multi_language_property: Optional[MultiLanguagePropertyT] = field(
        default=None,
        metadata={
            "name": "multiLanguageProperty",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    operation: Optional["OperationT"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    property: Optional[PropertyT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    range: Optional[RangeT] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    reference_element: Optional[ReferenceElementT] = field(
        default=None,
        metadata={
            "name": "referenceElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_collection: Optional[SubmodelElementCollectionT] = field(
        default=None,
        metadata={
            "name": "submodelElementCollection",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_list: Optional[SubmodelElementListT] = field(
        default=None,
        metadata={
            "name": "submodelElementList",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class OperationVariableT:
    class Meta:
        name = "operationVariable_t"

    value: Optional[OperationVariableTValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )


@dataclass
class OperationTInoutputVariables:
    class Meta:
        global_type = False

    operation_variable: List[OperationVariableT] = field(
        default_factory=list,
        metadata={
            "name": "operationVariable",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTInputVariables:
    class Meta:
        global_type = False

    operation_variable: List[OperationVariableT] = field(
        default_factory=list,
        metadata={
            "name": "operationVariable",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationTOutputVariables:
    class Meta:
        global_type = False

    operation_variable: List[OperationVariableT] = field(
        default_factory=list,
        metadata={
            "name": "operationVariable",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class OperationT:
    class Meta:
        name = "operation_t"

    extensions: Optional[OperationTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[OperationTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[OperationTDescription] = field(
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
    supplemental_semantic_ids: Optional[OperationTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[OperationTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[OperationTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    input_variables: Optional[OperationTInputVariables] = field(
        default=None,
        metadata={
            "name": "inputVariables",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    output_variables: Optional[OperationTOutputVariables] = field(
        default=None,
        metadata={
            "name": "outputVariables",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    inoutput_variables: Optional[OperationTInoutputVariables] = field(
        default=None,
        metadata={
            "name": "inoutputVariables",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class EntityTStatements:
    class Meta:
        global_type = False

    relationship_element: List[RelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "relationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    annotated_relationship_element: List[AnnotatedRelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "annotatedRelationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    basic_event_element: List[BasicEventElementT] = field(
        default_factory=list,
        metadata={
            "name": "basicEventElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    blob: List[BlobT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    capability: List[CapabilityT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    entity: List["EntityT"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    file: List[FileT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    multi_language_property: List[MultiLanguagePropertyT] = field(
        default_factory=list,
        metadata={
            "name": "multiLanguageProperty",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    operation: List[OperationT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    property: List[PropertyT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    range: List[RangeT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    reference_element: List[ReferenceElementT] = field(
        default_factory=list,
        metadata={
            "name": "referenceElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_collection: List[SubmodelElementCollectionT] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementCollection",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_list: List[SubmodelElementListT] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementList",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class EntityT:
    class Meta:
        name = "entity_t"

    extensions: Optional[EntityTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[EntityTDisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    description: Optional[EntityTDescription] = field(
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
    supplemental_semantic_ids: Optional[EntityTSupplementalSemanticIds] = field(
        default=None,
        metadata={
            "name": "supplementalSemanticIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    qualifiers: Optional[EntityTQualifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    embedded_data_specifications: Optional[EntityTEmbeddedDataSpecifications] = field(
        default=None,
        metadata={
            "name": "embeddedDataSpecifications",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    statements: Optional[EntityTStatements] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    entity_type: Optional[EntityTypeT] = field(
        default=None,
        metadata={
            "name": "entityType",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "required": True,
        }
    )
    global_asset_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "globalAssetId",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    specific_asset_ids: Optional[EntityTSpecificAssetIds] = field(
        default=None,
        metadata={
            "name": "specificAssetIds",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class SubmodelTSubmodelElements:
    class Meta:
        global_type = False

    relationship_element: List[RelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "relationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    annotated_relationship_element: List[AnnotatedRelationshipElementT] = field(
        default_factory=list,
        metadata={
            "name": "annotatedRelationshipElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    basic_event_element: List[BasicEventElementT] = field(
        default_factory=list,
        metadata={
            "name": "basicEventElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    blob: List[BlobT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    capability: List[CapabilityT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    entity: List[EntityT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    file: List[FileT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    multi_language_property: List[MultiLanguagePropertyT] = field(
        default_factory=list,
        metadata={
            "name": "multiLanguageProperty",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    operation: List[OperationT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    property: List[PropertyT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    range: List[RangeT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    reference_element: List[ReferenceElementT] = field(
        default_factory=list,
        metadata={
            "name": "referenceElement",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_collection: List[SubmodelElementCollectionT] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementCollection",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodel_element_list: List[SubmodelElementListT] = field(
        default_factory=list,
        metadata={
            "name": "submodelElementList",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class SubmodelT:
    class Meta:
        name = "submodel_t"

    extensions: Optional[SubmodelTExtensions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
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
    display_name: Optional[SubmodelTDisplayName] = field(
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
class EnvironmentTSubmodels:
    class Meta:
        global_type = False

    submodel: List[SubmodelT] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
            "min_occurs": 1,
        }
    )


@dataclass
class EnvironmentT:
    class Meta:
        name = "environment_t"

    asset_administration_shells: Optional[EnvironmentTAssetAdministrationShells] = field(
        default=None,
        metadata={
            "name": "assetAdministrationShells",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    submodels: Optional[EnvironmentTSubmodels] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )
    concept_descriptions: Optional[EnvironmentTConceptDescriptions] = field(
        default=None,
        metadata={
            "name": "conceptDescriptions",
            "type": "Element",
            "namespace": "https://admin-shell.io/aas/3/0",
        }
    )


@dataclass
class Environment(EnvironmentT):
    class Meta:
        name = "environment"
        namespace = "https://admin-shell.io/aas/3/0"
