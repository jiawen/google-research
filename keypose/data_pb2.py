# coding=utf-8
# Copyright 2021 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Compiled protobuf code."""
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keypose/data.proto

# pylint: disable=bad-continuation

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='keypose/data.proto',
    package='',
    syntax='proto2',
    serialized_options=None,
    serialized_pb=b'\n\x12keypose/data.proto\"\x1c\n\tTransform\x12\x0f\n\x07\x65lement\x18\x01 \x03(\x02\"f\n\x06\x43\x61mera\x12\n\n\x02\x66x\x18\x01 \x01(\x02\x12\n\n\x02\x66y\x18\x02 \x01(\x02\x12\n\n\x02\x63x\x18\x03 \x01(\x02\x12\n\n\x02\x63y\x18\x04 \x01(\x02\x12\x10\n\x08\x62\x61seline\x18\x05 \x01(\x02\x12\x0c\n\x04resx\x18\x06 \x01(\x02\x12\x0c\n\x04resy\x18\x07 \x01(\x02\"\xbc\x01\n\x06Target\x12\x1d\n\ttransform\x18\x01 \x01(\x0b\x32\n.Transform\x12\x17\n\x06\x63\x61mera\x18\x02 \x01(\x0b\x32\x07.Camera\x12#\n\tkeypoints\x18\x03 \x03(\x0b\x32\x10.Target.KeyPoint\x1aU\n\x08KeyPoint\x12\t\n\x01u\x18\x01 \x01(\x02\x12\t\n\x01v\x18\x02 \x01(\x02\x12\t\n\x01x\x18\x03 \x01(\x02\x12\t\n\x01y\x18\x04 \x01(\x02\x12\t\n\x01z\x18\x05 \x01(\x02\x12\x12\n\x07visible\x18\x06 \x01(\x02:\x01\x31\"`\n\nKeyTargets\x12\x1a\n\tkp_target\x18\x01 \x01(\x0b\x32\x07.Target\x12\x1d\n\x0cproj_targets\x18\x02 \x03(\x0b\x32\x07.Target\x12\x17\n\x08mirrored\x18\x03 \x01(\x08:\x05\x66\x61lse\"Q\n\nDataParams\x12\x0c\n\x04resx\x18\x01 \x01(\x05\x12\x0c\n\x04resy\x18\x02 \x01(\x05\x12\x0e\n\x06num_kp\x18\x03 \x01(\x05\x12\x17\n\x06\x63\x61mera\x18\x04 \x01(\x0b\x32\x07.Camera'
)

_TRANSFORM = _descriptor.Descriptor(
    name='Transform',
    full_name='Transform',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='element',
            full_name='Transform.element',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=22,
    serialized_end=50,
)

_CAMERA = _descriptor.Descriptor(
    name='Camera',
    full_name='Camera',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='fx',
            full_name='Camera.fx',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='fy',
            full_name='Camera.fy',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cx',
            full_name='Camera.cx',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cy',
            full_name='Camera.cy',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='baseline',
            full_name='Camera.baseline',
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='resx',
            full_name='Camera.resx',
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='resy',
            full_name='Camera.resy',
            index=6,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=52,
    serialized_end=154,
)

_TARGET_KEYPOINT = _descriptor.Descriptor(
    name='KeyPoint',
    full_name='Target.KeyPoint',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='u',
            full_name='Target.KeyPoint.u',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='v',
            full_name='Target.KeyPoint.v',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='x',
            full_name='Target.KeyPoint.x',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='y',
            full_name='Target.KeyPoint.y',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='z',
            full_name='Target.KeyPoint.z',
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='visible',
            full_name='Target.KeyPoint.visible',
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=True,
            default_value=float(1),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=260,
    serialized_end=345,
)

_TARGET = _descriptor.Descriptor(
    name='Target',
    full_name='Target',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='transform',
            full_name='Target.transform',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='camera',
            full_name='Target.camera',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='keypoints',
            full_name='Target.keypoints',
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
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[
        _TARGET_KEYPOINT,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=157,
    serialized_end=345,
)

_KEYTARGETS = _descriptor.Descriptor(
    name='KeyTargets',
    full_name='KeyTargets',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='kp_target',
            full_name='KeyTargets.kp_target',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='proj_targets',
            full_name='KeyTargets.proj_targets',
            index=1,
            number=2,
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
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='mirrored',
            full_name='KeyTargets.mirrored',
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=347,
    serialized_end=443,
)

_DATAPARAMS = _descriptor.Descriptor(
    name='DataParams',
    full_name='DataParams',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='resx',
            full_name='DataParams.resx',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='resy',
            full_name='DataParams.resy',
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_kp',
            full_name='DataParams.num_kp',
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='camera',
            full_name='DataParams.camera',
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[],
    serialized_start=445,
    serialized_end=526,
)

_TARGET_KEYPOINT.containing_type = _TARGET
_TARGET.fields_by_name['transform'].message_type = _TRANSFORM
_TARGET.fields_by_name['camera'].message_type = _CAMERA
_TARGET.fields_by_name['keypoints'].message_type = _TARGET_KEYPOINT
_KEYTARGETS.fields_by_name['kp_target'].message_type = _TARGET
_KEYTARGETS.fields_by_name['proj_targets'].message_type = _TARGET
_DATAPARAMS.fields_by_name['camera'].message_type = _CAMERA
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['Camera'] = _CAMERA
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
DESCRIPTOR.message_types_by_name['KeyTargets'] = _KEYTARGETS
DESCRIPTOR.message_types_by_name['DataParams'] = _DATAPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transform = _reflection.GeneratedProtocolMessageType(
    'Transform',
    (_message.Message,),
    {
        'DESCRIPTOR': _TRANSFORM,
        '__module__': 'keypose.data_pb2'
        # @@protoc_insertion_point(class_scope:Transform)
    })
_sym_db.RegisterMessage(Transform)

Camera = _reflection.GeneratedProtocolMessageType(
    'Camera',
    (_message.Message,),
    {
        'DESCRIPTOR': _CAMERA,
        '__module__': 'keypose.data_pb2'
        # @@protoc_insertion_point(class_scope:Camera)
    })
_sym_db.RegisterMessage(Camera)

Target = _reflection.GeneratedProtocolMessageType(
    'Target',
    (_message.Message,),
    {
        'KeyPoint':
            _reflection.GeneratedProtocolMessageType(
                'KeyPoint',
                (_message.Message,),
                {
                    'DESCRIPTOR': _TARGET_KEYPOINT,
                    '__module__': 'keypose.data_pb2'
                    # @@protoc_insertion_point(class_scope:Target.KeyPoint)
                }),
        'DESCRIPTOR':
            _TARGET,
        '__module__':
            'keypose.data_pb2'
        # @@protoc_insertion_point(class_scope:Target)
    })
_sym_db.RegisterMessage(Target)
_sym_db.RegisterMessage(Target.KeyPoint)

KeyTargets = _reflection.GeneratedProtocolMessageType(
    'KeyTargets',
    (_message.Message,),
    {
        'DESCRIPTOR': _KEYTARGETS,
        '__module__': 'keypose.data_pb2'
        # @@protoc_insertion_point(class_scope:KeyTargets)
    })
_sym_db.RegisterMessage(KeyTargets)

DataParams = _reflection.GeneratedProtocolMessageType(
    'DataParams',
    (_message.Message,),
    {
        'DESCRIPTOR': _DATAPARAMS,
        '__module__': 'keypose.data_pb2'
        # @@protoc_insertion_point(class_scope:DataParams)
    })
_sym_db.RegisterMessage(DataParams)

# @@protoc_insertion_point(module_scope)
