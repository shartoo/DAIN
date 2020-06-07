#!/usr/bin/env python3
import os
import torch

from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

cxx_args = ['-std=c++11']

from nvcc_args import nvcc_args

setup(
    name='depthflowprojection_cuda',
    ext_modules=[
        CUDAExtension('depthflowprojection_cuda', [
            'depthflowprojection_cuda.cc',
            'depthflowprojection_cuda_kernel.cu'
        ], extra_compile_args={'cxx': cxx_args, 'nvcc': nvcc_args})
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
