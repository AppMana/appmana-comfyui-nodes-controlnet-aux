from typing import Optional

import configargparse

from comfy.cli_args_types import Configuration


def add_configuration(parser: configargparse.ArgParser) -> configargparse.ArgParser:
    parser.add_argument("--annotator-ckpts-path",
                        required=False,
                        type=str,
                        help="Configure the location for HuggingFace model downloads or the pre-existing HuggingFace cache path. Defaults to the `models/huggingface` directory (changed from master)",
                        env_var="AUX_ANNOTATOR_CKPTS_PATH")
    parser.add_argument("--use-symlinks",
                        action="store_true",
                        help="Enables HuggingFace symlinks when building the HuggingFace model cache.",
                        env_var="AUX_USE_SYMLINKS")
    parser.add_argument("--ort-providers",
                        type=str,
                        help=f"Comma-separated list of ONNX Runtime Provider names. Available providers: {','.join(['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'])}",
                        env_var="AUX_ORT_PROVIDERS")
    return parser


class PreprocessorsConfiguration(Configuration):
    def __init__(self):
        super().__init__()
        self.annotator_ckpts_path: Optional[str] = None
        self.use_symlinks: bool = False
        self.ort_providers: Optional[str] = None
