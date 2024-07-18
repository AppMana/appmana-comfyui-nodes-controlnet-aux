from setuptools import setup, find_packages
import os.path

packages = find_packages(where='src')
setup(
    name="comfyui_controlnet_aux",
    version="0.0.1",
    packages=packages,
    package_dir={"": "src"},
    install_requires=open(os.path.join(os.path.dirname(__file__), "requirements.txt")).readlines(),
    author='',
    author_email='',
    description='',
    entry_points={
        'comfyui.custom_nodes': [
            'comfyui_controlnet_aux = comfyui_controlnet_aux.nodes',
        ],
        'comfyui.custom_config': [
            'comfyui_controlnet_aux = controlnet_aux_config.add_configuration:add_configuration',
        ]
    },
    include_package_data=True,
    package_data={
        package_or_module: ['*.json'] for package_or_module in packages
    },
)
