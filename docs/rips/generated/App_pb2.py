# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: App.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Definitions_pb2 as Definitions__pb2
import PdmObject_pb2 as PdmObject__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='App.proto',
  package='rips',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tApp.proto\x12\x04rips\x1a\x11\x44\x65\x66initions.proto\x1a\x0fPdmObject.proto\"N\n\x07Version\x12\x15\n\rmajor_version\x18\x01 \x01(\x05\x12\x15\n\rminor_version\x18\x02 \x01(\x05\x12\x15\n\rpatch_version\x18\x03 \x01(\x05\":\n\x0bRuntimeInfo\x12+\n\x08\x61pp_type\x18\x01 \x01(\x0e\x32\x19.rips.ApplicationTypeEnum*C\n\x13\x41pplicationTypeEnum\x12\x13\n\x0fGUI_APPLICATION\x10\x00\x12\x17\n\x13\x43ONSOLE_APPLICATION\x10\x01\x32\xb9\x01\n\x03\x41pp\x12*\n\nGetVersion\x12\x0b.rips.Empty\x1a\r.rips.Version\"\x00\x12\"\n\x04\x45xit\x12\x0b.rips.Empty\x1a\x0b.rips.Empty\"\x00\x12\x32\n\x0eGetRuntimeInfo\x12\x0b.rips.Empty\x1a\x11.rips.RuntimeInfo\"\x00\x12.\n\x0cGetPdmObject\x12\x0b.rips.Empty\x1a\x0f.rips.PdmObject\"\x00\x62\x06proto3'
  ,
  dependencies=[Definitions__pb2.DESCRIPTOR,PdmObject__pb2.DESCRIPTOR,])

_APPLICATIONTYPEENUM = _descriptor.EnumDescriptor(
  name='ApplicationTypeEnum',
  full_name='rips.ApplicationTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GUI_APPLICATION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONSOLE_APPLICATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=195,
  serialized_end=262,
)
_sym_db.RegisterEnumDescriptor(_APPLICATIONTYPEENUM)

ApplicationTypeEnum = enum_type_wrapper.EnumTypeWrapper(_APPLICATIONTYPEENUM)
GUI_APPLICATION = 0
CONSOLE_APPLICATION = 1



_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='rips.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major_version', full_name='rips.Version.major_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor_version', full_name='rips.Version.minor_version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patch_version', full_name='rips.Version.patch_version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=133,
)


_RUNTIMEINFO = _descriptor.Descriptor(
  name='RuntimeInfo',
  full_name='rips.RuntimeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_type', full_name='rips.RuntimeInfo.app_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=193,
)

_RUNTIMEINFO.fields_by_name['app_type'].enum_type = _APPLICATIONTYPEENUM
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['RuntimeInfo'] = _RUNTIMEINFO
DESCRIPTOR.enum_types_by_name['ApplicationTypeEnum'] = _APPLICATIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'App_pb2'
  # @@protoc_insertion_point(class_scope:rips.Version)
  })
_sym_db.RegisterMessage(Version)

RuntimeInfo = _reflection.GeneratedProtocolMessageType('RuntimeInfo', (_message.Message,), {
  'DESCRIPTOR' : _RUNTIMEINFO,
  '__module__' : 'App_pb2'
  # @@protoc_insertion_point(class_scope:rips.RuntimeInfo)
  })
_sym_db.RegisterMessage(RuntimeInfo)



_APP = _descriptor.ServiceDescriptor(
  name='App',
  full_name='rips.App',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=265,
  serialized_end=450,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetVersion',
    full_name='rips.App.GetVersion',
    index=0,
    containing_service=None,
    input_type=Definitions__pb2._EMPTY,
    output_type=_VERSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Exit',
    full_name='rips.App.Exit',
    index=1,
    containing_service=None,
    input_type=Definitions__pb2._EMPTY,
    output_type=Definitions__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRuntimeInfo',
    full_name='rips.App.GetRuntimeInfo',
    index=2,
    containing_service=None,
    input_type=Definitions__pb2._EMPTY,
    output_type=_RUNTIMEINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPdmObject',
    full_name='rips.App.GetPdmObject',
    index=3,
    containing_service=None,
    input_type=Definitions__pb2._EMPTY,
    output_type=PdmObject__pb2._PDMOBJECT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APP)

DESCRIPTOR.services_by_name['App'] = _APP

# @@protoc_insertion_point(module_scope)
