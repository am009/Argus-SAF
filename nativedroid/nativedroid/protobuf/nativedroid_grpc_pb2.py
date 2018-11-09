# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nativedroid/protobuf/nativedroid_grpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nativedroid.protobuf import java_signatures_pb2 as nativedroid_dot_protobuf_dot_java__signatures__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nativedroid/protobuf/nativedroid_grpc.proto',
  package='nativedroid_server',
  syntax='proto3',
  serialized_pb=_b('\n+nativedroid/protobuf/nativedroid_grpc.proto\x12\x12nativedroid_server\x1a*nativedroid/protobuf/java_signatures.proto\"\xa9\x01\n\x11GenSummaryRequest\x12\x12\n\napk_digest\x18\x01 \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\x02 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\x05\x12\x11\n\tso_digest\x18\x04 \x01(\t\x12\x10\n\x08jni_func\x18\x05 \x01(\t\x12\x34\n\x10method_signature\x18\x06 \x01(\x0b\x32\x1a.jawa_core.MethodSignature\"S\n\x12GenSummaryResponse\x12\r\n\x05taint\x18\x01 \x01(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x1d\n\x15\x61nalyzed_instructions\x18\x03 \x01(\x03\"5\n\x10HasSymbolRequest\x12\x11\n\tso_digest\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\"\'\n\x11HasSymbolResponse\x12\x12\n\nhas_symbol\x18\x01 \x01(\x08\"s\n\x1c\x41nalyseNativeActivityRequest\x12\x12\n\napk_digest\x18\x01 \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\x02 \x01(\t\x12\x11\n\tso_digest\x18\x03 \x01(\t\x12\x14\n\x0c\x63ustom_entry\x18\x04 \x01(\t\";\n\x1d\x41nalyseNativeActivityResponse\x12\x1a\n\x12total_instructions\x18\x01 \x01(\x03\"#\n\x11LoadBinaryRequest\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\"7\n\x12LoadBinaryResponse\x12\x11\n\tso_digest\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x05\x32\xa1\x03\n\x0bNativeDroid\x12[\n\nGenSummary\x12%.nativedroid_server.GenSummaryRequest\x1a&.nativedroid_server.GenSummaryResponse\x12X\n\tHasSymbol\x12$.nativedroid_server.HasSymbolRequest\x1a%.nativedroid_server.HasSymbolResponse\x12|\n\x15\x41nalyseNativeActivity\x12\x30.nativedroid_server.AnalyseNativeActivityRequest\x1a\x31.nativedroid_server.AnalyseNativeActivityResponse\x12]\n\nLoadBinary\x12%.nativedroid_server.LoadBinaryRequest\x1a&.nativedroid_server.LoadBinaryResponse(\x01\x42\x1e\n\x1corg.argus.nativedroid.serverb\x06proto3')
  ,
  dependencies=[nativedroid_dot_protobuf_dot_java__signatures__pb2.DESCRIPTOR,])




_GENSUMMARYREQUEST = _descriptor.Descriptor(
  name='GenSummaryRequest',
  full_name='nativedroid_server.GenSummaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apk_digest', full_name='nativedroid_server.GenSummaryRequest.apk_digest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_name', full_name='nativedroid_server.GenSummaryRequest.component_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='nativedroid_server.GenSummaryRequest.depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='so_digest', full_name='nativedroid_server.GenSummaryRequest.so_digest', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jni_func', full_name='nativedroid_server.GenSummaryRequest.jni_func', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method_signature', full_name='nativedroid_server.GenSummaryRequest.method_signature', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=281,
)


_GENSUMMARYRESPONSE = _descriptor.Descriptor(
  name='GenSummaryResponse',
  full_name='nativedroid_server.GenSummaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taint', full_name='nativedroid_server.GenSummaryResponse.taint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary', full_name='nativedroid_server.GenSummaryResponse.summary', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='analyzed_instructions', full_name='nativedroid_server.GenSummaryResponse.analyzed_instructions', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=366,
)


_HASSYMBOLREQUEST = _descriptor.Descriptor(
  name='HasSymbolRequest',
  full_name='nativedroid_server.HasSymbolRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='so_digest', full_name='nativedroid_server.HasSymbolRequest.so_digest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='nativedroid_server.HasSymbolRequest.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=421,
)


_HASSYMBOLRESPONSE = _descriptor.Descriptor(
  name='HasSymbolResponse',
  full_name='nativedroid_server.HasSymbolResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_symbol', full_name='nativedroid_server.HasSymbolResponse.has_symbol', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=462,
)


_ANALYSENATIVEACTIVITYREQUEST = _descriptor.Descriptor(
  name='AnalyseNativeActivityRequest',
  full_name='nativedroid_server.AnalyseNativeActivityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apk_digest', full_name='nativedroid_server.AnalyseNativeActivityRequest.apk_digest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_name', full_name='nativedroid_server.AnalyseNativeActivityRequest.component_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='so_digest', full_name='nativedroid_server.AnalyseNativeActivityRequest.so_digest', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_entry', full_name='nativedroid_server.AnalyseNativeActivityRequest.custom_entry', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=579,
)


_ANALYSENATIVEACTIVITYRESPONSE = _descriptor.Descriptor(
  name='AnalyseNativeActivityResponse',
  full_name='nativedroid_server.AnalyseNativeActivityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_instructions', full_name='nativedroid_server.AnalyseNativeActivityResponse.total_instructions', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=640,
)


_LOADBINARYREQUEST = _descriptor.Descriptor(
  name='LoadBinaryRequest',
  full_name='nativedroid_server.LoadBinaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='nativedroid_server.LoadBinaryRequest.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=642,
  serialized_end=677,
)


_LOADBINARYRESPONSE = _descriptor.Descriptor(
  name='LoadBinaryResponse',
  full_name='nativedroid_server.LoadBinaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='so_digest', full_name='nativedroid_server.LoadBinaryResponse.so_digest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='nativedroid_server.LoadBinaryResponse.length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=679,
  serialized_end=734,
)

_GENSUMMARYREQUEST.fields_by_name['method_signature'].message_type = nativedroid_dot_protobuf_dot_java__signatures__pb2._METHODSIGNATURE
DESCRIPTOR.message_types_by_name['GenSummaryRequest'] = _GENSUMMARYREQUEST
DESCRIPTOR.message_types_by_name['GenSummaryResponse'] = _GENSUMMARYRESPONSE
DESCRIPTOR.message_types_by_name['HasSymbolRequest'] = _HASSYMBOLREQUEST
DESCRIPTOR.message_types_by_name['HasSymbolResponse'] = _HASSYMBOLRESPONSE
DESCRIPTOR.message_types_by_name['AnalyseNativeActivityRequest'] = _ANALYSENATIVEACTIVITYREQUEST
DESCRIPTOR.message_types_by_name['AnalyseNativeActivityResponse'] = _ANALYSENATIVEACTIVITYRESPONSE
DESCRIPTOR.message_types_by_name['LoadBinaryRequest'] = _LOADBINARYREQUEST
DESCRIPTOR.message_types_by_name['LoadBinaryResponse'] = _LOADBINARYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenSummaryRequest = _reflection.GeneratedProtocolMessageType('GenSummaryRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENSUMMARYREQUEST,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.GenSummaryRequest)
  ))
_sym_db.RegisterMessage(GenSummaryRequest)

GenSummaryResponse = _reflection.GeneratedProtocolMessageType('GenSummaryResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENSUMMARYRESPONSE,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.GenSummaryResponse)
  ))
_sym_db.RegisterMessage(GenSummaryResponse)

HasSymbolRequest = _reflection.GeneratedProtocolMessageType('HasSymbolRequest', (_message.Message,), dict(
  DESCRIPTOR = _HASSYMBOLREQUEST,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.HasSymbolRequest)
  ))
_sym_db.RegisterMessage(HasSymbolRequest)

HasSymbolResponse = _reflection.GeneratedProtocolMessageType('HasSymbolResponse', (_message.Message,), dict(
  DESCRIPTOR = _HASSYMBOLRESPONSE,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.HasSymbolResponse)
  ))
_sym_db.RegisterMessage(HasSymbolResponse)

AnalyseNativeActivityRequest = _reflection.GeneratedProtocolMessageType('AnalyseNativeActivityRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSENATIVEACTIVITYREQUEST,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.AnalyseNativeActivityRequest)
  ))
_sym_db.RegisterMessage(AnalyseNativeActivityRequest)

AnalyseNativeActivityResponse = _reflection.GeneratedProtocolMessageType('AnalyseNativeActivityResponse', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSENATIVEACTIVITYRESPONSE,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.AnalyseNativeActivityResponse)
  ))
_sym_db.RegisterMessage(AnalyseNativeActivityResponse)

LoadBinaryRequest = _reflection.GeneratedProtocolMessageType('LoadBinaryRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOADBINARYREQUEST,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.LoadBinaryRequest)
  ))
_sym_db.RegisterMessage(LoadBinaryRequest)

LoadBinaryResponse = _reflection.GeneratedProtocolMessageType('LoadBinaryResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOADBINARYRESPONSE,
  __module__ = 'nativedroid.protobuf.nativedroid_grpc_pb2'
  # @@protoc_insertion_point(class_scope:nativedroid_server.LoadBinaryResponse)
  ))
_sym_db.RegisterMessage(LoadBinaryResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034org.argus.nativedroid.server'))

_NATIVEDROID = _descriptor.ServiceDescriptor(
  name='NativeDroid',
  full_name='nativedroid_server.NativeDroid',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=737,
  serialized_end=1154,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenSummary',
    full_name='nativedroid_server.NativeDroid.GenSummary',
    index=0,
    containing_service=None,
    input_type=_GENSUMMARYREQUEST,
    output_type=_GENSUMMARYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HasSymbol',
    full_name='nativedroid_server.NativeDroid.HasSymbol',
    index=1,
    containing_service=None,
    input_type=_HASSYMBOLREQUEST,
    output_type=_HASSYMBOLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AnalyseNativeActivity',
    full_name='nativedroid_server.NativeDroid.AnalyseNativeActivity',
    index=2,
    containing_service=None,
    input_type=_ANALYSENATIVEACTIVITYREQUEST,
    output_type=_ANALYSENATIVEACTIVITYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LoadBinary',
    full_name='nativedroid_server.NativeDroid.LoadBinary',
    index=3,
    containing_service=None,
    input_type=_LOADBINARYREQUEST,
    output_type=_LOADBINARYRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NATIVEDROID)

DESCRIPTOR.services_by_name['NativeDroid'] = _NATIVEDROID

# @@protoc_insertion_point(module_scope)
