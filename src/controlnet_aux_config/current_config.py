import os
from comfy.cli_args import args
from comfy.cmd import folder_paths
from .add_configuration import PreprocessorsConfiguration

typed_args: PreprocessorsConfiguration = args

annotator_checkpoints_path = typed_args.annotator_ckpts_path
if annotator_checkpoints_path is None:
    annotator_checkpoints_path = folder_paths.add_model_folder_path("annotator_checkpoints")

use_symlinks = typed_args.use_symlinks or False

ort_providers = typed_args.ort_providers.split(",") if typed_args.ort_providers is not None else [
    "CUDAExecutionProvider", "DirectMLExecutionProvider",
    "OpenVINOExecutionProvider", "ROCMExecutionProvider",
    "CPUExecutionProvider", "CoreMLExecutionProvider"]
os.makedirs(annotator_checkpoints_path, exist_ok=True)
