from setuptools import setup

setup(
    name="tf-retinanet-backbones-resnet101v2",
    version="1",
    description="Resnet101V2 backbone for Retinanet",
    long_description="",
    author="Jokke Ruokolainen",
    author_email="jokke.ruokolainen@vaisto.io",
    license="",
    packages=["tf_retinanet_backbones.resnet101v2"],
    install_requires=["tf-retinanet"],
    zip_safe=False,
)
