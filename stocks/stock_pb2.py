# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstock.proto\x12\x05stock\x1a\x1fgoogle/protobuf/timestamp.proto\"P\n\x05Stock\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x01\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3')



_STOCK = DESCRIPTOR.message_types_by_name['Stock']
Stock = _reflection.GeneratedProtocolMessageType('Stock', (_message.Message,), {
  'DESCRIPTOR' : _STOCK,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.Stock)
  })
_sym_db.RegisterMessage(Stock)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STOCK._serialized_start=55
  _STOCK._serialized_end=135
# @@protoc_insertion_point(module_scope)
