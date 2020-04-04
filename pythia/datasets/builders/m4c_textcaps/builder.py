# Copyright (c) Facebook, Inc. and its affiliates.
from pythia.common.registry import Registry
from pythia.datasets.builders.m4c_textcaps.dataset import M4CTextCapsDataset
from pythia.datasets.builders.m4c_textvqa.builder import M4CTextVQABuilder


@Registry.register_builder("m4c_textcaps")
class M4CTextCapsBuilder(M4CTextVQABuilder):
    def __init__(self):
        super().__init__()
        self.dataset_name = "m4c_textcaps"
        self.set_dataset_class(M4CTextCapsDataset)

    @classmethod
    def config_path(cls):
        return "configs/datasets/m4c_textcaps/defaults.yaml"