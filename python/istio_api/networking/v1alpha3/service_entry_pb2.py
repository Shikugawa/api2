# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networking/v1alpha3/service_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from networking.v1alpha3 import gateway_pb2 as networking_dot_v1alpha3_dot_gateway__pb2
from networking.v1alpha3 import sidecar_pb2 as networking_dot_v1alpha3_dot_sidecar__pb2
from networking.v1alpha3 import workload_entry_pb2 as networking_dot_v1alpha3_dot_workload__entry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='networking/v1alpha3/service_entry.proto',
  package='istio.networking.v1alpha3',
  syntax='proto3',
  serialized_options=_b('Z github.com/Shikugawa/api2/networking/v1alpha3'),
  serialized_pb=_b('\n\'networking/v1alpha3/service_entry.proto\x12\x19istio.networking.v1alpha3\x1a\x1fgoogle/api/field_behavior.proto\x1a!networking/v1alpha3/gateway.proto\x1a!networking/v1alpha3/sidecar.proto\x1a(networking/v1alpha3/workload_entry.proto\"\xf7\x04\n\x0cServiceEntry\x12\x1a\n\x05hosts\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\x05hosts\x12\x1c\n\taddresses\x18\x02 \x03(\tR\taddresses\x12;\n\x05ports\x18\x03 \x03(\x0b\x32\x1f.istio.networking.v1alpha3.PortB\x04\xe2\x41\x01\x02R\x05ports\x12L\n\x08location\x18\x04 \x01(\x0e\x32\x30.istio.networking.v1alpha3.ServiceEntry.LocationR\x08location\x12X\n\nresolution\x18\x05 \x01(\x0e\x32\x32.istio.networking.v1alpha3.ServiceEntry.ResolutionB\x04\xe2\x41\x01\x02R\nresolution\x12\x46\n\tendpoints\x18\x06 \x03(\x0b\x32(.istio.networking.v1alpha3.WorkloadEntryR\tendpoints\x12X\n\x11workload_selector\x18\t \x01(\x0b\x32+.istio.networking.v1alpha3.WorkloadSelectorR\x10workloadSelector\x12\x1b\n\texport_to\x18\x07 \x03(\tR\x08\x65xportTo\x12*\n\x11subject_alt_names\x18\x08 \x03(\tR\x0fsubjectAltNames\"0\n\x08Location\x12\x11\n\rMESH_EXTERNAL\x10\x00\x12\x11\n\rMESH_INTERNAL\x10\x01\"+\n\nResolution\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06STATIC\x10\x01\x12\x07\n\x03\x44NS\x10\x02\x42\"Z github.com/Shikugawa/api2/networking/v1alpha3b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,networking_dot_v1alpha3_dot_gateway__pb2.DESCRIPTOR,networking_dot_v1alpha3_dot_sidecar__pb2.DESCRIPTOR,networking_dot_v1alpha3_dot_workload__entry__pb2.DESCRIPTOR,])



_SERVICEENTRY_LOCATION = _descriptor.EnumDescriptor(
  name='Location',
  full_name='istio.networking.v1alpha3.ServiceEntry.Location',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MESH_EXTERNAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESH_INTERNAL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=754,
  serialized_end=802,
)
_sym_db.RegisterEnumDescriptor(_SERVICEENTRY_LOCATION)

_SERVICEENTRY_RESOLUTION = _descriptor.EnumDescriptor(
  name='Resolution',
  full_name='istio.networking.v1alpha3.ServiceEntry.Resolution',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATIC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DNS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=804,
  serialized_end=847,
)
_sym_db.RegisterEnumDescriptor(_SERVICEENTRY_RESOLUTION)


_SERVICEENTRY = _descriptor.Descriptor(
  name='ServiceEntry',
  full_name='istio.networking.v1alpha3.ServiceEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='istio.networking.v1alpha3.ServiceEntry.hosts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342A\001\002'), json_name='hosts', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='istio.networking.v1alpha3.ServiceEntry.addresses', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='addresses', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='istio.networking.v1alpha3.ServiceEntry.ports', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342A\001\002'), json_name='ports', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='istio.networking.v1alpha3.ServiceEntry.location', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='location', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='istio.networking.v1alpha3.ServiceEntry.resolution', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342A\001\002'), json_name='resolution', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='istio.networking.v1alpha3.ServiceEntry.endpoints', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='endpoints', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workload_selector', full_name='istio.networking.v1alpha3.ServiceEntry.workload_selector', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='workloadSelector', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='export_to', full_name='istio.networking.v1alpha3.ServiceEntry.export_to', index=7,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='exportTo', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject_alt_names', full_name='istio.networking.v1alpha3.ServiceEntry.subject_alt_names', index=8,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='subjectAltNames', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVICEENTRY_LOCATION,
    _SERVICEENTRY_RESOLUTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=847,
)

_SERVICEENTRY.fields_by_name['ports'].message_type = networking_dot_v1alpha3_dot_gateway__pb2._PORT
_SERVICEENTRY.fields_by_name['location'].enum_type = _SERVICEENTRY_LOCATION
_SERVICEENTRY.fields_by_name['resolution'].enum_type = _SERVICEENTRY_RESOLUTION
_SERVICEENTRY.fields_by_name['endpoints'].message_type = networking_dot_v1alpha3_dot_workload__entry__pb2._WORKLOADENTRY
_SERVICEENTRY.fields_by_name['workload_selector'].message_type = networking_dot_v1alpha3_dot_sidecar__pb2._WORKLOADSELECTOR
_SERVICEENTRY_LOCATION.containing_type = _SERVICEENTRY
_SERVICEENTRY_RESOLUTION.containing_type = _SERVICEENTRY
DESCRIPTOR.message_types_by_name['ServiceEntry'] = _SERVICEENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceEntry = _reflection.GeneratedProtocolMessageType('ServiceEntry', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEENTRY,
  '__module__' : 'networking.v1alpha3.service_entry_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.ServiceEntry)
  })
_sym_db.RegisterMessage(ServiceEntry)


DESCRIPTOR._options = None
_SERVICEENTRY.fields_by_name['hosts']._options = None
_SERVICEENTRY.fields_by_name['ports']._options = None
_SERVICEENTRY.fields_by_name['resolution']._options = None
# @@protoc_insertion_point(module_scope)
