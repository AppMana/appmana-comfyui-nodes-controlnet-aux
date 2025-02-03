import logging

from comfy.cli_args import args
from .add_configuration import PreprocessorsConfiguration

logger = logging.getLogger(__name__)
typed_args: PreprocessorsConfiguration = args

use_symlinks = typed_args.use_symlinks or False

ort_providers = typed_args.ort_providers.split(",") if typed_args.ort_providers is not None else [
    "CUDAExecutionProvider", "DirectMLExecutionProvider",
    "OpenVINOExecutionProvider", "ROCMExecutionProvider",
    "CPUExecutionProvider", "CoreMLExecutionProvider"]
