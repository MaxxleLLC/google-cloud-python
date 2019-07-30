# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/firestore/admin_v1/proto/index.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/firestore/admin_v1/proto/index.proto",
    package="google.firestore.admin.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\035com.google.firestore.admin.v1B\nIndexProtoP\001Z>google.golang.org/genproto/googleapis/firestore/admin/v1;admin\242\002\004GCFS\252\002\037Google.Cloud.Firestore.Admin.V1\312\002\037Google\\Cloud\\Firestore\\Admin\\V1"
    ),
    serialized_pb=_b(
        '\n1google/cloud/firestore/admin_v1/proto/index.proto\x12\x19google.firestore.admin.v1\x1a\x1cgoogle/api/annotations.proto"\x91\x05\n\x05Index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x0bquery_scope\x18\x02 \x01(\x0e\x32+.google.firestore.admin.v1.Index.QueryScope\x12;\n\x06\x66ields\x18\x03 \x03(\x0b\x32+.google.firestore.admin.v1.Index.IndexField\x12\x35\n\x05state\x18\x04 \x01(\x0e\x32&.google.firestore.admin.v1.Index.State\x1a\xbd\x02\n\nIndexField\x12\x12\n\nfield_path\x18\x01 \x01(\t\x12\x42\n\x05order\x18\x02 \x01(\x0e\x32\x31.google.firestore.admin.v1.Index.IndexField.OrderH\x00\x12O\n\x0c\x61rray_config\x18\x03 \x01(\x0e\x32\x37.google.firestore.admin.v1.Index.IndexField.ArrayConfigH\x00"=\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"9\n\x0b\x41rrayConfig\x12\x1c\n\x18\x41RRAY_CONFIG_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43ONTAINS\x10\x01\x42\x0c\n\nvalue_mode"9\n\nQueryScope\x12\x1b\n\x17QUERY_SCOPE_UNSPECIFIED\x10\x00\x12\x0e\n\nCOLLECTION\x10\x01"I\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x10\n\x0cNEEDS_REPAIR\x10\x03\x42\xb8\x01\n\x1d\x63om.google.firestore.admin.v1B\nIndexProtoP\x01Z>google.golang.org/genproto/googleapis/firestore/admin/v1;admin\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1b\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_INDEX_INDEXFIELD_ORDER = _descriptor.EnumDescriptor(
    name="Order",
    full_name="google.firestore.admin.v1.Index.IndexField.Order",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ORDER_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ASCENDING", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DESCENDING", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=500,
    serialized_end=561,
)
_sym_db.RegisterEnumDescriptor(_INDEX_INDEXFIELD_ORDER)

_INDEX_INDEXFIELD_ARRAYCONFIG = _descriptor.EnumDescriptor(
    name="ArrayConfig",
    full_name="google.firestore.admin.v1.Index.IndexField.ArrayConfig",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ARRAY_CONFIG_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTAINS", index=1, number=1, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=563,
    serialized_end=620,
)
_sym_db.RegisterEnumDescriptor(_INDEX_INDEXFIELD_ARRAYCONFIG)

_INDEX_QUERYSCOPE = _descriptor.EnumDescriptor(
    name="QueryScope",
    full_name="google.firestore.admin.v1.Index.QueryScope",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="QUERY_SCOPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="COLLECTION", index=1, number=1, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=636,
    serialized_end=693,
)
_sym_db.RegisterEnumDescriptor(_INDEX_QUERYSCOPE)

_INDEX_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.firestore.admin.v1.Index.State",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CREATING", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="READY", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="NEEDS_REPAIR", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=695,
    serialized_end=768,
)
_sym_db.RegisterEnumDescriptor(_INDEX_STATE)


_INDEX_INDEXFIELD = _descriptor.Descriptor(
    name="IndexField",
    full_name="google.firestore.admin.v1.Index.IndexField",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="field_path",
            full_name="google.firestore.admin.v1.Index.IndexField.field_path",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="order",
            full_name="google.firestore.admin.v1.Index.IndexField.order",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="array_config",
            full_name="google.firestore.admin.v1.Index.IndexField.array_config",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_INDEX_INDEXFIELD_ORDER, _INDEX_INDEXFIELD_ARRAYCONFIG],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="value_mode",
            full_name="google.firestore.admin.v1.Index.IndexField.value_mode",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=317,
    serialized_end=634,
)

_INDEX = _descriptor.Descriptor(
    name="Index",
    full_name="google.firestore.admin.v1.Index",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.firestore.admin.v1.Index.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="query_scope",
            full_name="google.firestore.admin.v1.Index.query_scope",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fields",
            full_name="google.firestore.admin.v1.Index.fields",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.firestore.admin.v1.Index.state",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_INDEX_INDEXFIELD],
    enum_types=[_INDEX_QUERYSCOPE, _INDEX_STATE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=111,
    serialized_end=768,
)

_INDEX_INDEXFIELD.fields_by_name["order"].enum_type = _INDEX_INDEXFIELD_ORDER
_INDEX_INDEXFIELD.fields_by_name[
    "array_config"
].enum_type = _INDEX_INDEXFIELD_ARRAYCONFIG
_INDEX_INDEXFIELD.containing_type = _INDEX
_INDEX_INDEXFIELD_ORDER.containing_type = _INDEX_INDEXFIELD
_INDEX_INDEXFIELD_ARRAYCONFIG.containing_type = _INDEX_INDEXFIELD
_INDEX_INDEXFIELD.oneofs_by_name["value_mode"].fields.append(
    _INDEX_INDEXFIELD.fields_by_name["order"]
)
_INDEX_INDEXFIELD.fields_by_name[
    "order"
].containing_oneof = _INDEX_INDEXFIELD.oneofs_by_name["value_mode"]
_INDEX_INDEXFIELD.oneofs_by_name["value_mode"].fields.append(
    _INDEX_INDEXFIELD.fields_by_name["array_config"]
)
_INDEX_INDEXFIELD.fields_by_name[
    "array_config"
].containing_oneof = _INDEX_INDEXFIELD.oneofs_by_name["value_mode"]
_INDEX.fields_by_name["query_scope"].enum_type = _INDEX_QUERYSCOPE
_INDEX.fields_by_name["fields"].message_type = _INDEX_INDEXFIELD
_INDEX.fields_by_name["state"].enum_type = _INDEX_STATE
_INDEX_QUERYSCOPE.containing_type = _INDEX
_INDEX_STATE.containing_type = _INDEX
DESCRIPTOR.message_types_by_name["Index"] = _INDEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Index = _reflection.GeneratedProtocolMessageType(
    "Index",
    (_message.Message,),
    dict(
        IndexField=_reflection.GeneratedProtocolMessageType(
            "IndexField",
            (_message.Message,),
            dict(
                DESCRIPTOR=_INDEX_INDEXFIELD,
                __module__="google.cloud.firestore.admin_v1.proto.index_pb2",
                __doc__="""A field in an index. The field\_path describes which field is indexed,
    the value\_mode describes how the field value is indexed.
    
    
    Attributes:
        field_path:
            Can be **name**. For single field indexes, this must match the
            name of the field or may be omitted.
        value_mode:
            How the field value is indexed.
        order:
            Indicates that this field supports ordering by the specified
            order or comparing using =, <, <=, >, >=.
        array_config:
            Indicates that this field supports operations on
            ``array_value``\ s.
    """,
                # @@protoc_insertion_point(class_scope:google.firestore.admin.v1.Index.IndexField)
            ),
        ),
        DESCRIPTOR=_INDEX,
        __module__="google.cloud.firestore.admin_v1.proto.index_pb2",
        __doc__="""Cloud Firestore indexes enable simple and complex queries against
  documents in a database.
  
  
  Attributes:
      name:
          Output only. A server defined name for this index. The form of
          this name for composite indexes will be: ``projects/{project_i
          d}/databases/{database_id}/collectionGroups/{collection_id}/in
          dexes/{composite_index_id}`` For single field indexes, this
          field will be empty.
      query_scope:
          Indexes with a collection query scope specified allow queries
          against a collection that is the child of a specific document,
          specified at query time, and that has the same collection id.
          Indexes with a collection group query scope specified allow
          queries against all collections descended from a specific
          document, specified at query time, and that have the same
          collection id as this index.
      fields:
          The fields supported by this index.  For composite indexes,
          this is always 2 or more fields. The last field entry is
          always for the field path ``__name__``. If, on creation,
          ``__name__`` was not specified as the last field, it will be
          added automatically with the same direction as that of the
          last field defined. If the final field in a composite index is
          not directional, the ``__name__`` will be ordered ASCENDING
          (unless explicitly specified).  For single field indexes, this
          will always be exactly one entry with a field path equal to
          the field path of the associated field.
      state:
          Output only. The serving state of the index.
  """,
        # @@protoc_insertion_point(class_scope:google.firestore.admin.v1.Index)
    ),
)
_sym_db.RegisterMessage(Index)
_sym_db.RegisterMessage(Index.IndexField)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
