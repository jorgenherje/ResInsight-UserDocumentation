# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Case.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PdmObject_pb2 as PdmObject__pb2
import Definitions_pb2 as Definitions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Case.proto',
  package='rips',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nCase.proto\x12\x04rips\x1a\x0fPdmObject.proto\x1a\x11\x44\x65\x66initions.proto\"\x19\n\x0b\x43\x61seRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"D\n\x08\x43\x61seInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08group_id\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\"-\n\rCaseInfoArray\x12\x1c\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0e.rips.CaseInfo\"g\n\x0b\x42oundingBox\x12\r\n\x05min_x\x18\x01 \x01(\x01\x12\r\n\x05max_x\x18\x02 \x01(\x01\x12\r\n\x05min_y\x18\x03 \x01(\x01\x12\r\n\x05max_y\x18\x04 \x01(\x01\x12\r\n\x05min_z\x18\x05 \x01(\x01\x12\r\n\x05max_z\x18\x06 \x01(\x01\"%\n\tCaseGroup\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"2\n\nCaseGroups\x12$\n\x0b\x63\x61se_groups\x18\x01 \x03(\x0b\x32\x0f.rips.CaseGroup\"\x1a\n\tGridCount\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"D\n\tCellCount\x12\x19\n\x11\x61\x63tive_cell_count\x18\x01 \x01(\x05\x12\x1c\n\x14reservoir_cell_count\x18\x02 \x01(\x05\"k\n\x0f\x43\x65llInfoRequest\x12\'\n\x0c\x63\x61se_request\x18\x01 \x01(\x0b\x32\x11.rips.CaseRequest\x12/\n\x0eporosity_model\x18\x02 \x01(\x0e\x32\x17.rips.PorosityModelType\"-\n\rCellInfoArray\x12\x1c\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0e.rips.CellInfo\"\x98\x01\n\x08\x43\x65llInfo\x12\x12\n\ngrid_index\x18\x01 \x01(\x05\x12\x19\n\x11parent_grid_index\x18\x02 \x01(\x05\x12\x1c\n\x14\x63oarsening_box_index\x18\x03 \x01(\x05\x12\x1e\n\tlocal_ijk\x18\x04 \x01(\x0b\x32\x0b.rips.Vec3i\x12\x1f\n\nparent_ijk\x18\x05 \x01(\x0b\x32\x0b.rips.Vec3i\"9\n\x13\x43oarseningInfoArray\x12\"\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x14.rips.CoarseningInfo\"D\n\x0e\x43oarseningInfo\x12\x18\n\x03min\x18\x01 \x01(\x0b\x32\x0b.rips.Vec3i\x12\x18\n\x03max\x18\x02 \x01(\x0b\x32\x0b.rips.Vec3i\"2\n\rTimeStepDates\x12!\n\x05\x64\x61tes\x18\x01 \x03(\x0b\x32\x12.rips.TimeStepDate\"f\n\x0cTimeStepDate\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\x12\x0c\n\x04hour\x18\x04 \x01(\x05\x12\x0e\n\x06minute\x18\x05 \x01(\x05\x12\x0e\n\x06second\x18\x06 \x01(\x05\"&\n\x0e\x44\x61ysSinceStart\x12\x14\n\x0c\x64\x61y_decimals\x18\x01 \x03(\x01\"<\n\x0cSelectedCell\x12\x12\n\ngrid_index\x18\x01 \x01(\x05\x12\x18\n\x03ijk\x18\x02 \x01(\x0b\x32\x0b.rips.Vec3i\"2\n\rSelectedCells\x12!\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x12.rips.SelectedCell*9\n\x11PorosityModelType\x12\x10\n\x0cMATRIX_MODEL\x10\x00\x12\x12\n\x0e\x46RACTURE_MODEL\x10\x01\x32\x94\x06\n\x04\x43\x61se\x12\x34\n\x0cGetGridCount\x12\x11.rips.CaseRequest\x1a\x0f.rips.GridCount\"\x00\x12\x38\n\x0cGetCellCount\x12\x15.rips.CellInfoRequest\x1a\x0f.rips.CellCount\"\x00\x12K\n\x19GetCellInfoForActiveCells\x12\x15.rips.CellInfoRequest\x1a\x13.rips.CellInfoArray\"\x00\x30\x01\x12K\n\x1bGetCellCenterForActiveCells\x12\x15.rips.CellInfoRequest\x1a\x11.rips.CellCenters\"\x00\x30\x01\x12Q\n\x1cGetCellCornersForActiveCells\x12\x15.rips.CellInfoRequest\x1a\x16.rips.CellCornersArray\"\x00\x30\x01\x12H\n\x16GetCoarseningInfoArray\x12\x11.rips.CaseRequest\x1a\x19.rips.CoarseningInfoArray\"\x00\x12\x38\n\x0cGetTimeSteps\x12\x11.rips.CaseRequest\x1a\x13.rips.TimeStepDates\"\x00\x12>\n\x10GetSelectedCells\x12\x11.rips.CaseRequest\x1a\x13.rips.SelectedCells\"\x00\x30\x01\x12>\n\x11GetDaysSinceStart\x12\x11.rips.CaseRequest\x1a\x14.rips.DaysSinceStart\"\x00\x12\x32\n\x0bGetCaseInfo\x12\x11.rips.CaseRequest\x1a\x0e.rips.CaseInfo\"\x00\x12\x34\n\x0cGetPdmObject\x12\x11.rips.CaseRequest\x1a\x0f.rips.PdmObject\"\x00\x12\x41\n\x17GetReservoirBoundingBox\x12\x11.rips.CaseRequest\x1a\x11.rips.BoundingBox\"\x00\x62\x06proto3')
  ,
  dependencies=[PdmObject__pb2.DESCRIPTOR,Definitions__pb2.DESCRIPTOR,])

_POROSITYMODELTYPE = _descriptor.EnumDescriptor(
  name='PorosityModelType',
  full_name='rips.PorosityModelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MATRIX_MODEL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRACTURE_MODEL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1244,
  serialized_end=1301,
)
_sym_db.RegisterEnumDescriptor(_POROSITYMODELTYPE)

PorosityModelType = enum_type_wrapper.EnumTypeWrapper(_POROSITYMODELTYPE)
MATRIX_MODEL = 0
FRACTURE_MODEL = 1



_CASEREQUEST = _descriptor.Descriptor(
  name='CaseRequest',
  full_name='rips.CaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rips.CaseRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=56,
  serialized_end=81,
)


_CASEINFO = _descriptor.Descriptor(
  name='CaseInfo',
  full_name='rips.CaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rips.CaseInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='rips.CaseInfo.group_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='rips.CaseInfo.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='rips.CaseInfo.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=83,
  serialized_end=151,
)


_CASEINFOARRAY = _descriptor.Descriptor(
  name='CaseInfoArray',
  full_name='rips.CaseInfoArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='rips.CaseInfoArray.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=153,
  serialized_end=198,
)


_BOUNDINGBOX = _descriptor.Descriptor(
  name='BoundingBox',
  full_name='rips.BoundingBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_x', full_name='rips.BoundingBox.min_x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_x', full_name='rips.BoundingBox.max_x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_y', full_name='rips.BoundingBox.min_y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_y', full_name='rips.BoundingBox.max_y', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_z', full_name='rips.BoundingBox.min_z', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_z', full_name='rips.BoundingBox.max_z', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=200,
  serialized_end=303,
)


_CASEGROUP = _descriptor.Descriptor(
  name='CaseGroup',
  full_name='rips.CaseGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rips.CaseGroup.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='rips.CaseGroup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=305,
  serialized_end=342,
)


_CASEGROUPS = _descriptor.Descriptor(
  name='CaseGroups',
  full_name='rips.CaseGroups',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='case_groups', full_name='rips.CaseGroups.case_groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=344,
  serialized_end=394,
)


_GRIDCOUNT = _descriptor.Descriptor(
  name='GridCount',
  full_name='rips.GridCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='rips.GridCount.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=396,
  serialized_end=422,
)


_CELLCOUNT = _descriptor.Descriptor(
  name='CellCount',
  full_name='rips.CellCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_cell_count', full_name='rips.CellCount.active_cell_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reservoir_cell_count', full_name='rips.CellCount.reservoir_cell_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=424,
  serialized_end=492,
)


_CELLINFOREQUEST = _descriptor.Descriptor(
  name='CellInfoRequest',
  full_name='rips.CellInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='case_request', full_name='rips.CellInfoRequest.case_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='porosity_model', full_name='rips.CellInfoRequest.porosity_model', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=494,
  serialized_end=601,
)


_CELLINFOARRAY = _descriptor.Descriptor(
  name='CellInfoArray',
  full_name='rips.CellInfoArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='rips.CellInfoArray.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=603,
  serialized_end=648,
)


_CELLINFO = _descriptor.Descriptor(
  name='CellInfo',
  full_name='rips.CellInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grid_index', full_name='rips.CellInfo.grid_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_grid_index', full_name='rips.CellInfo.parent_grid_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coarsening_box_index', full_name='rips.CellInfo.coarsening_box_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_ijk', full_name='rips.CellInfo.local_ijk', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_ijk', full_name='rips.CellInfo.parent_ijk', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=651,
  serialized_end=803,
)


_COARSENINGINFOARRAY = _descriptor.Descriptor(
  name='CoarseningInfoArray',
  full_name='rips.CoarseningInfoArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='rips.CoarseningInfoArray.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=805,
  serialized_end=862,
)


_COARSENINGINFO = _descriptor.Descriptor(
  name='CoarseningInfo',
  full_name='rips.CoarseningInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='rips.CoarseningInfo.min', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='rips.CoarseningInfo.max', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=864,
  serialized_end=932,
)


_TIMESTEPDATES = _descriptor.Descriptor(
  name='TimeStepDates',
  full_name='rips.TimeStepDates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dates', full_name='rips.TimeStepDates.dates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=934,
  serialized_end=984,
)


_TIMESTEPDATE = _descriptor.Descriptor(
  name='TimeStepDate',
  full_name='rips.TimeStepDate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='rips.TimeStepDate.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='rips.TimeStepDate.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='rips.TimeStepDate.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='rips.TimeStepDate.hour', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minute', full_name='rips.TimeStepDate.minute', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='rips.TimeStepDate.second', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=986,
  serialized_end=1088,
)


_DAYSSINCESTART = _descriptor.Descriptor(
  name='DaysSinceStart',
  full_name='rips.DaysSinceStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='day_decimals', full_name='rips.DaysSinceStart.day_decimals', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1090,
  serialized_end=1128,
)


_SELECTEDCELL = _descriptor.Descriptor(
  name='SelectedCell',
  full_name='rips.SelectedCell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grid_index', full_name='rips.SelectedCell.grid_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ijk', full_name='rips.SelectedCell.ijk', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1130,
  serialized_end=1190,
)


_SELECTEDCELLS = _descriptor.Descriptor(
  name='SelectedCells',
  full_name='rips.SelectedCells',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='rips.SelectedCells.cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1192,
  serialized_end=1242,
)

_CASEINFOARRAY.fields_by_name['data'].message_type = _CASEINFO
_CASEGROUPS.fields_by_name['case_groups'].message_type = _CASEGROUP
_CELLINFOREQUEST.fields_by_name['case_request'].message_type = _CASEREQUEST
_CELLINFOREQUEST.fields_by_name['porosity_model'].enum_type = _POROSITYMODELTYPE
_CELLINFOARRAY.fields_by_name['data'].message_type = _CELLINFO
_CELLINFO.fields_by_name['local_ijk'].message_type = Definitions__pb2._VEC3I
_CELLINFO.fields_by_name['parent_ijk'].message_type = Definitions__pb2._VEC3I
_COARSENINGINFOARRAY.fields_by_name['data'].message_type = _COARSENINGINFO
_COARSENINGINFO.fields_by_name['min'].message_type = Definitions__pb2._VEC3I
_COARSENINGINFO.fields_by_name['max'].message_type = Definitions__pb2._VEC3I
_TIMESTEPDATES.fields_by_name['dates'].message_type = _TIMESTEPDATE
_SELECTEDCELL.fields_by_name['ijk'].message_type = Definitions__pb2._VEC3I
_SELECTEDCELLS.fields_by_name['cells'].message_type = _SELECTEDCELL
DESCRIPTOR.message_types_by_name['CaseRequest'] = _CASEREQUEST
DESCRIPTOR.message_types_by_name['CaseInfo'] = _CASEINFO
DESCRIPTOR.message_types_by_name['CaseInfoArray'] = _CASEINFOARRAY
DESCRIPTOR.message_types_by_name['BoundingBox'] = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['CaseGroup'] = _CASEGROUP
DESCRIPTOR.message_types_by_name['CaseGroups'] = _CASEGROUPS
DESCRIPTOR.message_types_by_name['GridCount'] = _GRIDCOUNT
DESCRIPTOR.message_types_by_name['CellCount'] = _CELLCOUNT
DESCRIPTOR.message_types_by_name['CellInfoRequest'] = _CELLINFOREQUEST
DESCRIPTOR.message_types_by_name['CellInfoArray'] = _CELLINFOARRAY
DESCRIPTOR.message_types_by_name['CellInfo'] = _CELLINFO
DESCRIPTOR.message_types_by_name['CoarseningInfoArray'] = _COARSENINGINFOARRAY
DESCRIPTOR.message_types_by_name['CoarseningInfo'] = _COARSENINGINFO
DESCRIPTOR.message_types_by_name['TimeStepDates'] = _TIMESTEPDATES
DESCRIPTOR.message_types_by_name['TimeStepDate'] = _TIMESTEPDATE
DESCRIPTOR.message_types_by_name['DaysSinceStart'] = _DAYSSINCESTART
DESCRIPTOR.message_types_by_name['SelectedCell'] = _SELECTEDCELL
DESCRIPTOR.message_types_by_name['SelectedCells'] = _SELECTEDCELLS
DESCRIPTOR.enum_types_by_name['PorosityModelType'] = _POROSITYMODELTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CaseRequest = _reflection.GeneratedProtocolMessageType('CaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _CASEREQUEST,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CaseRequest)
  ))
_sym_db.RegisterMessage(CaseRequest)

CaseInfo = _reflection.GeneratedProtocolMessageType('CaseInfo', (_message.Message,), dict(
  DESCRIPTOR = _CASEINFO,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CaseInfo)
  ))
_sym_db.RegisterMessage(CaseInfo)

CaseInfoArray = _reflection.GeneratedProtocolMessageType('CaseInfoArray', (_message.Message,), dict(
  DESCRIPTOR = _CASEINFOARRAY,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CaseInfoArray)
  ))
_sym_db.RegisterMessage(CaseInfoArray)

BoundingBox = _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.BoundingBox)
  ))
_sym_db.RegisterMessage(BoundingBox)

CaseGroup = _reflection.GeneratedProtocolMessageType('CaseGroup', (_message.Message,), dict(
  DESCRIPTOR = _CASEGROUP,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CaseGroup)
  ))
_sym_db.RegisterMessage(CaseGroup)

CaseGroups = _reflection.GeneratedProtocolMessageType('CaseGroups', (_message.Message,), dict(
  DESCRIPTOR = _CASEGROUPS,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CaseGroups)
  ))
_sym_db.RegisterMessage(CaseGroups)

GridCount = _reflection.GeneratedProtocolMessageType('GridCount', (_message.Message,), dict(
  DESCRIPTOR = _GRIDCOUNT,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.GridCount)
  ))
_sym_db.RegisterMessage(GridCount)

CellCount = _reflection.GeneratedProtocolMessageType('CellCount', (_message.Message,), dict(
  DESCRIPTOR = _CELLCOUNT,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CellCount)
  ))
_sym_db.RegisterMessage(CellCount)

CellInfoRequest = _reflection.GeneratedProtocolMessageType('CellInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _CELLINFOREQUEST,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CellInfoRequest)
  ))
_sym_db.RegisterMessage(CellInfoRequest)

CellInfoArray = _reflection.GeneratedProtocolMessageType('CellInfoArray', (_message.Message,), dict(
  DESCRIPTOR = _CELLINFOARRAY,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CellInfoArray)
  ))
_sym_db.RegisterMessage(CellInfoArray)

CellInfo = _reflection.GeneratedProtocolMessageType('CellInfo', (_message.Message,), dict(
  DESCRIPTOR = _CELLINFO,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CellInfo)
  ))
_sym_db.RegisterMessage(CellInfo)

CoarseningInfoArray = _reflection.GeneratedProtocolMessageType('CoarseningInfoArray', (_message.Message,), dict(
  DESCRIPTOR = _COARSENINGINFOARRAY,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CoarseningInfoArray)
  ))
_sym_db.RegisterMessage(CoarseningInfoArray)

CoarseningInfo = _reflection.GeneratedProtocolMessageType('CoarseningInfo', (_message.Message,), dict(
  DESCRIPTOR = _COARSENINGINFO,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.CoarseningInfo)
  ))
_sym_db.RegisterMessage(CoarseningInfo)

TimeStepDates = _reflection.GeneratedProtocolMessageType('TimeStepDates', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTEPDATES,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.TimeStepDates)
  ))
_sym_db.RegisterMessage(TimeStepDates)

TimeStepDate = _reflection.GeneratedProtocolMessageType('TimeStepDate', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTEPDATE,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.TimeStepDate)
  ))
_sym_db.RegisterMessage(TimeStepDate)

DaysSinceStart = _reflection.GeneratedProtocolMessageType('DaysSinceStart', (_message.Message,), dict(
  DESCRIPTOR = _DAYSSINCESTART,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.DaysSinceStart)
  ))
_sym_db.RegisterMessage(DaysSinceStart)

SelectedCell = _reflection.GeneratedProtocolMessageType('SelectedCell', (_message.Message,), dict(
  DESCRIPTOR = _SELECTEDCELL,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.SelectedCell)
  ))
_sym_db.RegisterMessage(SelectedCell)

SelectedCells = _reflection.GeneratedProtocolMessageType('SelectedCells', (_message.Message,), dict(
  DESCRIPTOR = _SELECTEDCELLS,
  __module__ = 'Case_pb2'
  # @@protoc_insertion_point(class_scope:rips.SelectedCells)
  ))
_sym_db.RegisterMessage(SelectedCells)



_CASE = _descriptor.ServiceDescriptor(
  name='Case',
  full_name='rips.Case',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1304,
  serialized_end=2092,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGridCount',
    full_name='rips.Case.GetGridCount',
    index=0,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=_GRIDCOUNT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCellCount',
    full_name='rips.Case.GetCellCount',
    index=1,
    containing_service=None,
    input_type=_CELLINFOREQUEST,
    output_type=_CELLCOUNT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCellInfoForActiveCells',
    full_name='rips.Case.GetCellInfoForActiveCells',
    index=2,
    containing_service=None,
    input_type=_CELLINFOREQUEST,
    output_type=_CELLINFOARRAY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCellCenterForActiveCells',
    full_name='rips.Case.GetCellCenterForActiveCells',
    index=3,
    containing_service=None,
    input_type=_CELLINFOREQUEST,
    output_type=Definitions__pb2._CELLCENTERS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCellCornersForActiveCells',
    full_name='rips.Case.GetCellCornersForActiveCells',
    index=4,
    containing_service=None,
    input_type=_CELLINFOREQUEST,
    output_type=Definitions__pb2._CELLCORNERSARRAY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCoarseningInfoArray',
    full_name='rips.Case.GetCoarseningInfoArray',
    index=5,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=_COARSENINGINFOARRAY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTimeSteps',
    full_name='rips.Case.GetTimeSteps',
    index=6,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=_TIMESTEPDATES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSelectedCells',
    full_name='rips.Case.GetSelectedCells',
    index=7,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=_SELECTEDCELLS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDaysSinceStart',
    full_name='rips.Case.GetDaysSinceStart',
    index=8,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=_DAYSSINCESTART,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCaseInfo',
    full_name='rips.Case.GetCaseInfo',
    index=9,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=_CASEINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPdmObject',
    full_name='rips.Case.GetPdmObject',
    index=10,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=PdmObject__pb2._PDMOBJECT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetReservoirBoundingBox',
    full_name='rips.Case.GetReservoirBoundingBox',
    index=11,
    containing_service=None,
    input_type=_CASEREQUEST,
    output_type=_BOUNDINGBOX,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CASE)

DESCRIPTOR.services_by_name['Case'] = _CASE

# @@protoc_insertion_point(module_scope)
