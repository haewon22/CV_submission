# Ultralytics YOLO 🚀, AGPL-3.0 license
"""
Ultralytics modules. Visualize with:

from models.FLDetn.pkgs.ultralytics.nn.modules import *
import torch
import os

x = torch.ones(1, 128, 40, 40)
m = Conv(128, 128)
f = f'{m._get_name()}.onnx'
torch.onnx.export(m, x, f)
os.system(f'onnxsim {f} {f} && open {f}')
"""

from .block import (C1, C2, C3, C3TR, DFL, SPP, SPPF,PSPPF, Bottleneck, BottleneckCSP, C2f, C2f_OneConv, C3Ghost, C3x, GhostBottleneck,
                    HGBlock, HGStem, Proto, RepC3)
from .conv import (CBAM, ChannelAttention, Concat, Conv, Conv2, ConvTranspose, DWConv, DWConvTranspose2d, Focus,
                   GhostConv, LightConv, RepConv, SpatialAttention, RepDWConv, RepConv2, Conv2x2Sp, SpaceToDepthModule,
                   Down_SpaceToDepthModule, RepOrthoConv, ConvRepbn)
from .head import Classify, Detect, Pose, RTDETRDecoder, Segment
from .transformer import (AIFI, MLP, DeformableTransformerDecoder, DeformableTransformerDecoderLayer, LayerNorm2d,
                          MLPBlock, MSDeformAttn, TransformerBlock, TransformerEncoderLayer, TransformerLayer)
from .csdet_block import (conv_bn,IEPR,RepBlock3, CSNeck3in, ECM)

__all__ = ('Conv', 'Conv2', 'conv_bn', 'LightConv', 'RepConv', 'DWConv', 'DWConvTranspose2d', 'ConvTranspose', 'Focus',
           'GhostConv', 'ChannelAttention', 'SpatialAttention', 'CBAM', 'Concat', 'TransformerLayer','Conv2x2Sp',
           'SpaceToDepthModule','Down_SpaceToDepthModule','RepOrthoConv', 'ConvRepbn',
           'TransformerBlock', 'MLPBlock', 'LayerNorm2d', 'DFL', 'HGBlock', 'HGStem', 'SPP', 'SPPF', 'PSPPF','C1', 'C2', 'C3',
           'C2f','C2f_OneConv', 'C3x', 'C3TR', 'C3Ghost', 'GhostBottleneck', 'Bottleneck', 'BottleneckCSP', 'Proto', 'Detect',
           'Segment', 'Pose', 'Classify', 'TransformerEncoderLayer', 'RepC3', 'RTDETRDecoder', 'AIFI',
           'DeformableTransformerDecoder', 'DeformableTransformerDecoderLayer', 'MSDeformAttn', 'MLP',
           'RepBlock3', 'RepDWConv', 'IEPR', 'ECM')
